from schemas.index import UnFollowWebHook

async def unfollow_use_case(body: UnFollowWebHook) -> str:
    print(body)
    return body.events[0].source.userId