from schemas.index import MessageTextWebHook

async def text_message(body: MessageTextWebHook) -> str:
    print(body)
    return body.events[0].source.userId