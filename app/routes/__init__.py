from app.routes.main import MainRouter
from app.routes.login import LoginRouter


__all__ = ("Routers",)


Routers = (
    MainRouter,
    LoginRouter,
)
