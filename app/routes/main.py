from fastapi import APIRouter, Request


__all__ = ("MainRouter",)


MainRouter = APIRouter(tags=["main"])


@MainRouter.get(
    '/',
    status_code=200,
)
async def main(request: Request):
    app_container = request.app.container
    templates = app_container.templates()
    return templates.TemplateResponse("index.html", context={"request": request})
