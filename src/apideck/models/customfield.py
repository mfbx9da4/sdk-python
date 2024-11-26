"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


class SixTypedDict(TypedDict):
    pass


class Six(BaseModel):
    pass


class FourTypedDict(TypedDict):
    pass


class Four(BaseModel):
    pass


ValueTypedDict = TypeAliasType(
    "ValueTypedDict",
    Union[FourTypedDict, str, float, bool, List[str], List[SixTypedDict]],
)


Value = TypeAliasType("Value", Union[Four, str, float, bool, List[str], List[Six]])


class CustomFieldTypedDict(TypedDict):
    id: Nullable[str]
    r"""Unique identifier for the custom field."""
    name: NotRequired[Nullable[str]]
    r"""Name of the custom field."""
    description: NotRequired[Nullable[str]]
    r"""More information about the custom field"""
    value: NotRequired[Nullable[ValueTypedDict]]


class CustomField(BaseModel):
    id: Nullable[str]
    r"""Unique identifier for the custom field."""

    name: OptionalNullable[str] = UNSET
    r"""Name of the custom field."""

    description: OptionalNullable[str] = UNSET
    r"""More information about the custom field"""

    value: OptionalNullable[Value] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "description", "value"]
        nullable_fields = ["id", "name", "description", "value"]
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
