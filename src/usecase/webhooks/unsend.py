from schemas.index import UnSendWebHook

async def un_send_use_case(body: UnSendWebHook) -> str:
    print(body)
    return body.events[0].source.userId