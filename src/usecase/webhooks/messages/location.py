from services.notification.interface import ApplyRegisterModule, ApplyRegister
from injector import Injector
from schemas.index import MessageLocationWebHook

async def location_message(body: MessageLocationWebHook) -> str:
    print(body)
    message: str = body.events[0].message.address
    injector = Injector([ApplyRegisterModule()])
    _injection = injector.get(ApplyRegister)
    _injection.register(message)
    return body.events[0].source.userId