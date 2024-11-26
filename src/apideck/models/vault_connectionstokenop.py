"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getconnectionresponse import GetConnectionResponse, GetConnectionResponseTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class VaultConnectionsTokenGlobalsTypedDict(TypedDict):
    customer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConnectionsTokenGlobals(BaseModel):
    customer_id: Annotated[
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


class VaultConnectionsTokenRequestBodyTypedDict(TypedDict):
    pass


class VaultConnectionsTokenRequestBody(BaseModel):
    pass


class VaultConnectionsTokenRequestTypedDict(TypedDict):
    service_id: str
    r"""Service ID of the resource to return"""
    unified_api: str
    r"""Unified API"""
    request_body: NotRequired[VaultConnectionsTokenRequestBodyTypedDict]


class VaultConnectionsTokenRequest(BaseModel):
    service_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Service ID of the resource to return"""

    unified_api: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unified API"""

    request_body: Annotated[
        Optional[VaultConnectionsTokenRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


VaultConnectionsTokenResponseTypedDict = TypeAliasType(
    "VaultConnectionsTokenResponseTypedDict",
    Union[GetConnectionResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


VaultConnectionsTokenResponse = TypeAliasType(
    "VaultConnectionsTokenResponse",
    Union[GetConnectionResponse, UnexpectedErrorResponse],
)
