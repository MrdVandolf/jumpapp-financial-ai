from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.constants import DEFAULT_JWT_COOKIE
from app.models.service.user import UserValidateJWTResponse


__all__ = ("JWTSessionMiddleware",)


class JWTSessionMiddleware(BaseHTTPMiddleware):

    async def __check_jwt(self):
        if not self.cookies.get(DEFAULT_JWT_COOKIE):
            return False

        jwt = self.cookies[DEFAULT_JWT_COOKIE]
        data: UserValidateJWTResponse = await self.user_service.validate_user_jwt(jwt)
        if not data.success:
            return False

        self.user = data.user
        return True

    async def dispatch(self, request: Request, call_next):
        app_container = request.app.container
        self.user_service = app_container.service_container.user_service()
        self.cookies = request.cookies
        path = request.url.path.rstrip("/")

        if path in ("/login", "/auth"):
            # for login and auth - check that jwt is NOT present or invalid
            if await self.__check_jwt():
                # jwt is present and valid - cancel request, redirect to main
                return RedirectResponse(url="/")
        else:
            # for everything else - check that jwt is present and valid
            if not await self.__check_jwt():
                return RedirectResponse(url="/login")
            request.app.user = self.user
            # jwt is present and valid - proceed

        return await call_next(request)
