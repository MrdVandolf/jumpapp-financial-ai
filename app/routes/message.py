import logging
import asyncio

from fastapi import APIRouter, Request, Response
from app.models.routes.message import MessageSendRequest, MessageSendResponse
from app.models.data.chats import ChatModel


__all__ = ("MessageRouter",)


MessageRouter = APIRouter(tags=["message"], prefix="/message")


@MessageRouter.post(
    '/send',
    status_code=200,
    response_model=MessageSendResponse,
)
async def main(message_request: MessageSendRequest, request: Request):
    app_container = request.app.container
    chat_repository = app_container.repository_container.chats()
    ai_service = app_container.service_container.ai_service()
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

    message_text = await ai_service.make_request(message_request.content)

    await chat_repository.write_ai_message(chat.id, message_text)

    return MessageSendResponse(
        success=True,
        message=message_text,
        redirect_to=f"/chat/{chat.id}" if not chat_id else None
    )
