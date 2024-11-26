"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel
from apideck.utils import FieldMetadata
from datetime import datetime
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IssuesFilterTypedDict(TypedDict):
    status: NotRequired[List[str]]
    r"""Filter by ticket status, can be `open`, `closed` or `all`. Will passthrough if none of the above match"""
    since: NotRequired[datetime]
    r"""Only return tickets since a specific date"""
    assignee_id: NotRequired[str]
    r"""Only return tickets assigned to a specific user"""


class IssuesFilter(BaseModel):
    status: Annotated[Optional[List[str]], FieldMetadata(query=True)] = None
    r"""Filter by ticket status, can be `open`, `closed` or `all`. Will passthrough if none of the above match"""

    since: Annotated[Optional[datetime], FieldMetadata(query=True)] = None
    r"""Only return tickets since a specific date"""

    assignee_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""Only return tickets assigned to a specific user"""
