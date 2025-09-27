from app.routes.main import MainRouter
from app.routes.login import LoginRouter, LogoutRouter
from app.routes.auth import AuthRouter
from app.routes.chat import ChatRouter


__all__ = ("Routers",)


Routers = (
    MainRouter,
    LoginRouter,
    LogoutRouter,
    AuthRouter,
    ChatRouter,
)
