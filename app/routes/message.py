import logging

from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse
from app.models.routes.message import MessageSendRequest, MessageSendResponse
from app.models.data.chats import ChatModel


__all__ = ("MessageRouter",)


MessageRouter = APIRouter(tags=["message"], prefix="/message")


@MessageRouter.post(
    '/send',
    status_code=200,
    response_model=MessageSendResponse,
)
async def main(message_request: MessageSendRequest, request: Request, response: Response):
    app_container = request.app.container
    chat_repository = app_container.repository_container.chats()
    user = request.app.user

    cookies = request.cookies
    chat_id = cookies.get("chat_id")

    if not chat_id:
        name = f"{message_request.content[:30]}{'...' if len(message_request.content) > 30 else ''}"
        chat: ChatModel = await chat_repository.create(user.id, name)
    else:
        chat: ChatModel = await chat_repository.find_by_id_and_user(user.id, chat_id)

    if not chat:
        logging.warning(f"Can't find chat {chat_id=} for user {user.id} | {user.email}")
        return MessageSendResponse()

    await chat_repository.write_user_message(chat.id, message_request.content)

    return MessageSendResponse(success=True, redirect_to=f"/chat/{chat.id}" if not chat_id else None)
