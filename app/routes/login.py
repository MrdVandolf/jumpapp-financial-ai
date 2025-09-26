from fastapi import APIRouter, Request


__all__ = ("LoginRouter",)


LoginRouter = APIRouter(tags=["login"], prefix="/login")


@LoginRouter.get(
    '/',
    status_code=200,
)
async def main(request: Request):
    app_container = request.app.container
    return {"login": True}

