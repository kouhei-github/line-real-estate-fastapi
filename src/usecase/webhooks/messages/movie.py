from schemas.index import MessageMovieWebHook

async def movie_message(body: MessageMovieWebHook) -> str:
    print(body)
    return body.events[0].source.userId