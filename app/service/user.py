import hashlib
import jwt

from app.models.data.users import UserModel
from app.models.service.user import UserLoginResponse, UserValidateJWTResponse


__all__ = ("UserService",)

import hmac


class UserService:

    def __init__(self, config, repository_container):
        self.config = config
        self.user_repo = repository_container.users()

    @staticmethod
    def __hash_password(password: str, salt: str) -> str:
        return hashlib.sha512(f"{password}{salt}".encode("utf-8")).hexdigest()

    @staticmethod
    def __compare_password(password1: str, password2: str) -> bool:
        return hmac.compare_digest(password1, password2)

    @staticmethod
    def __generate_jwt(user_data: dict, secret: str) -> str:
        return jwt.encode(user_data, secret, algorithm="HS256")

    @staticmethod
    def __validate_jwt(jwt_token: str, secret: str) -> dict:
        try:
            return jwt.decode(jwt_token, secret, algorithms=["HS256"])
        except (jwt.InvalidSignatureError, jwt.InvalidAlgorithmError):
            return {}

    async def login_user(self, email, password) -> UserLoginResponse:
        user: UserModel|None = await self.user_repo.find_by_email(email)
        if not user:
            return UserLoginResponse(**{"found": False, "logged_in": False})

        logged_in = self.__compare_password(
            self.__hash_password(password, user.salt),
            user.hash,
        )
        if not logged_in:
            return UserLoginResponse(**{"found": True, "logged_in": False})

        jwt_token = self.__generate_jwt({"uid": user.id}, self.config["JWT_KEY"])
        return UserLoginResponse(**{"found": True, "logged_in": True, "user": user, "jwt": jwt_token})

    async def validate_user_jwt(self, jwt_token: str) -> UserValidateJWTResponse:
        decoded_data = self.__validate_jwt(jwt_token, self.config["JWT_KEY"])
        if not decoded_data:
            return UserValidateJWTResponse()

        user = await self.user_repo.find_by_id(decoded_data["uid"])
        if not user:
            return UserValidateJWTResponse()

        return UserValidateJWTResponse(**{"success": True, "user": user})
