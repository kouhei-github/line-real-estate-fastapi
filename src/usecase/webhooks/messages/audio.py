
from schemas.index import MessageAudioWebHook

async def audio_message(body: MessageAudioWebHook) -> str:
    print(body)
    return body.events[0].source.userId