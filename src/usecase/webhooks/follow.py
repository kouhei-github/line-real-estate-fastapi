from schemas.index import FollowWebHook

async def follow_use_case(body: FollowWebHook) -> str:
    print(body)
    return body.events[0].source.userId