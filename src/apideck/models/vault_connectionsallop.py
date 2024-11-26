"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getconnectionsresponse import (
    GetConnectionsResponse,
    GetConnectionsResponseTypedDict,
)
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class VaultConnectionsAllGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConnectionsAllGlobals(BaseModel):
    consumer_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-consumer-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""ID of the consumer which you want to get or push data from"""

    app_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-app-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""The ID of your Unify application"""


class VaultConnectionsAllRequestTypedDict(TypedDict):
    api: NotRequired[str]
    r"""Scope results to Unified API"""
    configured: NotRequired[bool]
    r"""Scopes results to connections that have been configured or not"""


class VaultConnectionsAllRequest(BaseModel):
    api: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Scope results to Unified API"""

    configured: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Scopes results to connections that have been configured or not"""


VaultConnectionsAllResponseTypedDict = TypeAliasType(
    "VaultConnectionsAllResponseTypedDict",
    Union[GetConnectionsResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


VaultConnectionsAllResponse = TypeAliasType(
    "VaultConnectionsAllResponse",
    Union[GetConnectionsResponse, UnexpectedErrorResponse],
)
