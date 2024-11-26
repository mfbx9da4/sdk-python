"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .apistatus import APIStatus
from apideck.types import BaseModel
from apideck.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ApisFilterTypedDict(TypedDict):
    status: NotRequired[APIStatus]
    r"""Status of the API. APIs with status live or beta are callable."""


class ApisFilter(BaseModel):
    status: Annotated[Optional[APIStatus], FieldMetadata(query=True)] = None
    r"""Status of the API. APIs with status live or beta are callable."""
