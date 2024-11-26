"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CursorsTypedDict(TypedDict):
    r"""Cursors to navigate to previous or next pages through the API"""

    previous: NotRequired[Nullable[str]]
    r"""Cursor to navigate to the previous page of results through the API"""
    current: NotRequired[Nullable[str]]
    r"""Cursor to navigate to the current page of results through the API"""
    next: NotRequired[Nullable[str]]
    r"""Cursor to navigate to the next page of results through the API"""


class Cursors(BaseModel):
    r"""Cursors to navigate to previous or next pages through the API"""

    previous: OptionalNullable[str] = UNSET
    r"""Cursor to navigate to the previous page of results through the API"""

    current: OptionalNullable[str] = UNSET
    r"""Cursor to navigate to the current page of results through the API"""

    next: OptionalNullable[str] = UNSET
    r"""Cursor to navigate to the next page of results through the API"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["previous", "current", "next"]
        nullable_fields = ["previous", "current", "next"]
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


class MetaTypedDict(TypedDict):
    r"""Response metadata"""

    items_on_page: NotRequired[int]
    r"""Number of items returned in the data property of the response"""
    cursors: NotRequired[CursorsTypedDict]
    r"""Cursors to navigate to previous or next pages through the API"""


class Meta(BaseModel):
    r"""Response metadata"""

    items_on_page: Optional[int] = None
    r"""Number of items returned in the data property of the response"""

    cursors: Optional[Cursors] = None
    r"""Cursors to navigate to previous or next pages through the API"""
