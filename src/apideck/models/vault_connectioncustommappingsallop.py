"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getcustommappingsresponse import (
    GetCustomMappingsResponse,
    GetCustomMappingsResponseTypedDict,
)
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class VaultConnectionCustomMappingsAllGlobalsTypedDict(TypedDict):
    customer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class VaultConnectionCustomMappingsAllGlobals(BaseModel):
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


class VaultConnectionCustomMappingsAllRequestTypedDict(TypedDict):
    unified_api: str
    r"""Unified API"""
    service_id: str
    r"""Service ID of the resource to return"""
    resource: str
    r"""Name of the resource (plural)"""
    resource_id: NotRequired[str]
    r"""This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id."""


class VaultConnectionCustomMappingsAllRequest(BaseModel):
    unified_api: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unified API"""

    service_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Service ID of the resource to return"""

    resource: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Name of the resource (plural)"""

    resource_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""This is the id of the resource you want to fetch when listing custom fields. For example, if you want to fetch custom fields for a specific contact, you would use the contact id."""


VaultConnectionCustomMappingsAllResponseTypedDict = TypeAliasType(
    "VaultConnectionCustomMappingsAllResponseTypedDict",
    Union[GetCustomMappingsResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


VaultConnectionCustomMappingsAllResponse = TypeAliasType(
    "VaultConnectionCustomMappingsAllResponse",
    Union[GetCustomMappingsResponse, UnexpectedErrorResponse],
)
