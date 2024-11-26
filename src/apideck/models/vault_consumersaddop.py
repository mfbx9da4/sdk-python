"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createconsumerresponse import (
    CreateConsumerResponse,
    CreateConsumerResponseTypedDict,
)
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import FieldMetadata, HeaderMetadata
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class VaultConsumersAddGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConsumersAddGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


VaultConsumersAddResponseTypedDict = TypeAliasType(
    "VaultConsumersAddResponseTypedDict",
    Union[CreateConsumerResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


VaultConsumersAddResponse = TypeAliasType(
    "VaultConsumersAddResponse", Union[CreateConsumerResponse, UnexpectedErrorResponse]
)
