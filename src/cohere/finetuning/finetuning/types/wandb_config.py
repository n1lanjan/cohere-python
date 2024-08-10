# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel


class WandbConfig(UncheckedBaseModel):
    """
    The Weights & Biases configuration.
    """

    project: str = pydantic.Field()
    """
    The WandB project name to be used during training.
    """

    api_key: str = pydantic.Field()
    """
    The WandB API key to be used during training.
    """

    entity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The WandB entity name to be used during training.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow