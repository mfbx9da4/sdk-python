"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .links import Links, LinksTypedDict
from .meta import Meta, MetaTypedDict
from .opportunity import Opportunity, OpportunityTypedDict
from apideck.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class GetOpportunitiesResponseTypedDict(TypedDict):
    r"""Opportunities"""

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
    data: List[OpportunityTypedDict]
    meta: NotRequired[MetaTypedDict]
    r"""Response metadata"""
    links: NotRequired[LinksTypedDict]
    r"""Links to navigate to previous or next pages through the API"""


class GetOpportunitiesResponse(BaseModel):
    r"""Opportunities"""

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

    data: List[Opportunity]

    meta: Optional[Meta] = None
    r"""Response metadata"""

    links: Optional[Links] = None
    r"""Links to navigate to previous or next pages through the API"""
