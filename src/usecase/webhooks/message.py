from typing import Dict
from schemas.index import (
    MessageTextWebHook, MessageImageWebHook, MessageMovieWebHook,
    MessageAudioWebHook, MessageFileWebHook, MessageLocationWebHook
)
from .messages.text import text_message
from .messages.image import image_message
from .messages.movie import movie_message
from .messages.audio import audio_message
from .messages.file import file_message
from .messages.location import location_message

async def message_use_case(body: Dict) -> str:
    message_type = body["events"][0]["message"]["type"]
    match message_type:
        case "text":
            body = MessageTextWebHook.parse_obj(body)
            await text_message(body)
        case "image":
            body = MessageImageWebHook.parse_obj(body)
            await image_message(body)
        case "video":
            body = MessageMovieWebHook.parse_obj(body)
            await movie_message(body)
        case "audio":
            body = MessageAudioWebHook.parse_obj(body)
            await audio_message(body)
        case "file":
            body = MessageFileWebHook.parse_obj(body)
            await file_message(body)
        case "location":
            body = MessageLocationWebHook.parse_obj(body)
            await location_message(body)

    return body.events[0].source.userId