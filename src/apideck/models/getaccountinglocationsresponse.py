"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountinglocation import AccountingLocation, AccountingLocationTypedDict
from .links import Links, LinksTypedDict
from .meta import Meta, MetaTypedDict
from apideck.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GetAccountingLocationsResponseTypedDict(TypedDict):
    r"""Locations"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    service: str
    r"""Apideck ID of service provider"""
    resource: str
    r"""Unified API resource name"""
    operation: str
    r"""Operation performed"""
    data: List[AccountingLocationTypedDict]
    meta: NotRequired[MetaTypedDict]
    r"""Response metadata"""
    links: NotRequired[LinksTypedDict]
    r"""Links to navigate to previous or next pages through the API"""


class GetAccountingLocationsResponse(BaseModel):
    r"""Locations"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    service: str
    r"""Apideck ID of service provider"""

    resource: str
    r"""Unified API resource name"""

    operation: str
    r"""Operation performed"""

    data: List[AccountingLocation]

    meta: Optional[Meta] = None
    r"""Response metadata"""

    links: Optional[Links] = None
    r"""Links to navigate to previous or next pages through the API"""
