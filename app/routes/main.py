from fastapi import APIRouter, Request, Response


__all__ = ("MainRouter",)


MainRouter = APIRouter(tags=["main"])


@MainRouter.get(
    '/',
    status_code=200,
)
async def main(request: Request):
    app_container = request.app.container
    templates = app_container.templates()
    chat_repository = app_container.repository_container.chats()

    user = request.app.user
    chats = await chat_repository.find_by_user(user.id)

    context = {
        "request": request,
        "chats": chats,
        "current_chat": [],
    }

    response = templates.TemplateResponse("pages/chat.html", context=context)
    response.delete_cookie(key="chat_id")
    return response
