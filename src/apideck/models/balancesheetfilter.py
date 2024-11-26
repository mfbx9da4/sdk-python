"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel
from apideck.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BalanceSheetFilterTypedDict(TypedDict):
    start_date: NotRequired[str]
    r"""Filter by start date. If start date is given, end date is required."""
    end_date: NotRequired[str]
    r"""Filter by end date. If end date is given, start date is required."""


class BalanceSheetFilter(BaseModel):
    start_date: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Filter by start date. If start date is given, end date is required."""

    end_date: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Filter by end date. If end date is given, start date is required."""
