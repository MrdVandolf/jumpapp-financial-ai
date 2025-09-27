from app.middlewares.jwt_login_session import JWTSessionMiddleware


__all__ = ("Middlewares",)


Middlewares = [
    JWTSessionMiddleware,
]
