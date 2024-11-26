"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getconnectorresponse import GetConnectorResponse, GetConnectorResponseTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import FieldMetadata, HeaderMetadata, PathParamMetadata
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class ConnectorConnectorsOneGlobalsTypedDict(TypedDict):
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class ConnectorConnectorsOneGlobals(BaseModel):
    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class ConnectorConnectorsOneRequestTypedDict(TypedDict):
    id: str
    r"""ID of the record you are acting upon."""


class ConnectorConnectorsOneRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the record you are acting upon."""


ConnectorConnectorsOneResponseTypedDict = TypeAliasType(
    "ConnectorConnectorsOneResponseTypedDict",
    Union[GetConnectorResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


ConnectorConnectorsOneResponse = TypeAliasType(
    "ConnectorConnectorsOneResponse",
    Union[GetConnectorResponse, UnexpectedErrorResponse],
)
