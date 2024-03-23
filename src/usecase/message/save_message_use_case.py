from schemas.index import MessageTextSchema
from repositories.message.interface import MessageRepositoryModule, MessageRepository
from injector import Injector

async def save_message_use_case(body: MessageTextSchema) -> dict:
    # user
    injector = Injector([MessageRepositoryModule()])
    message_repository = injector.get(MessageRepository)
    response = message_repository.save(body.text)
    return response