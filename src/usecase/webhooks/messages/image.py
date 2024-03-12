from schemas.index import MessageImageWebHook

async def image_message(body: MessageImageWebHook) -> str:
    print(body)
    return body.events[0].source.userId