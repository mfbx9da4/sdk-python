"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getinvoicesresponse import GetInvoicesResponse, GetInvoicesResponseTypedDict
from .invoicesfilter import InvoicesFilter, InvoicesFilterTypedDict
from .invoicessort import InvoicesSort, InvoicesSortTypedDict
from .unexpectederrorresponse import (
    UnexpectedErrorResponse,
    UnexpectedErrorResponseTypedDict,
)
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from apideck.utils import FieldMetadata, HeaderMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import Any, Dict, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class AccountingInvoicesAllGlobalsTypedDict(TypedDict):
    consumer_id: NotRequired[str]
    r"""ID of the consumer which you want to get or push data from"""
    app_id: NotRequired[str]
    r"""The ID of your Unify application"""


class AccountingInvoicesAllGlobals(BaseModel):
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


class AccountingInvoicesAllRequestTypedDict(TypedDict):
    raw: NotRequired[bool]
    r"""Include raw response. Mostly used for debugging purposes"""
    service_id: NotRequired[str]
    r"""Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API."""
    cursor: NotRequired[Nullable[str]]
    r"""Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response."""
    limit: NotRequired[int]
    r"""Number of results to return. Minimum 1, Maximum 200, Default 20"""
    filter_: NotRequired[InvoicesFilterTypedDict]
    r"""Apply filters"""
    sort: NotRequired[InvoicesSortTypedDict]
    r"""Apply sorting"""
    pass_through: NotRequired[Dict[str, Any]]
    r"""Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads"""
    fields: NotRequired[Nullable[str]]
    r"""The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded."""


class AccountingInvoicesAllRequest(BaseModel):
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

    cursor: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Number of results to return. Minimum 1, Maximum 200, Default 20"""

    filter_: Annotated[
        Optional[InvoicesFilter],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Apply filters"""

    sort: Annotated[
        Optional[InvoicesSort],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Apply sorting"""

    pass_through: Annotated[
        Optional[Dict[str, Any]],
        FieldMetadata(query=QueryParamMetadata(style="deepObject", explode=True)),
    ] = None
    r"""Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads"""

    fields: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET
    r"""The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "raw",
            "serviceId",
            "cursor",
            "limit",
            "filter",
            "sort",
            "pass_through",
            "fields",
        ]
        nullable_fields = ["cursor", "fields"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


AccountingInvoicesAllResponseTypedDict = TypeAliasType(
    "AccountingInvoicesAllResponseTypedDict",
    Union[UnexpectedErrorResponseTypedDict, GetInvoicesResponseTypedDict],
)


AccountingInvoicesAllResponse = TypeAliasType(
    "AccountingInvoicesAllResponse", Union[UnexpectedErrorResponse, GetInvoicesResponse]
)
