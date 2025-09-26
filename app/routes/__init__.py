from app.routes.main import MainRouter
from app.routes.login import LoginRouter
from app.routes.auth import AuthRouter


__all__ = ("Routers",)


Routers = (
    MainRouter,
    LoginRouter,
    AuthRouter,
)
