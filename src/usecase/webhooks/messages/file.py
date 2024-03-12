from schemas.index import MessageFileWebHook

async def file_message(body: MessageFileWebHook) -> str:
    print(body)
    return body.events[0].source.userId