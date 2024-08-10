# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...core.pydantic_utilities import IS_PYDANTIC_V2
from .chat_message_end_event_delta import ChatMessageEndEventDelta
from .chat_stream_event_type import ChatStreamEventType


class ChatMessageEndEvent(ChatStreamEventType):
    """
    A streamed event which signifies that the chat message has ended.
    """

    id: typing.Optional[str] = None
    delta: typing.Optional[ChatMessageEndEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow