"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createtrackingcategoryresponse import (
    CreateTrackingCategoryResponse,
    CreateTrackingCategoryResponseTypedDict,
)
from .trackingcategory import TrackingCategoryInput, TrackingCategoryInputTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel
from apideck.utils import (
    FieldMetadata,
    HeaderMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class AccountingTrackingCategoriesAddGlobalsTypedDict(TypedDict):
    customer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class AccountingTrackingCategoriesAddGlobals(BaseModel):
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


class AccountingTrackingCategoriesAddRequestTypedDict(TypedDict):
    tracking_category: TrackingCategoryInputTypedDict
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""


class AccountingTrackingCategoriesAddRequest(BaseModel):
    tracking_category: Annotated[
        TrackingCategoryInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    raw: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include raw response. Mostly used for debugging purposes"""

    service_id: Annotated[
        Optional[str],
        pydantic.Field(alias="x-apideck-service-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""


AccountingTrackingCategoriesAddResponseTypedDict = TypeAliasType(
    "AccountingTrackingCategoriesAddResponseTypedDict",
    Union[CreateTrackingCategoryResponseTypedDict, UnexpectedErrorResponseTypedDict],
)


AccountingTrackingCategoriesAddResponse = TypeAliasType(
    "AccountingTrackingCategoriesAddResponse",
    Union[CreateTrackingCategoryResponse, UnexpectedErrorResponse],
)
