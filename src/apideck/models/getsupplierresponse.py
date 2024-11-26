"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .supplier import Supplier, SupplierTypedDict
from apideck.types import BaseModel
from typing_extensions import TypedDict


class GetSupplierResponseTypedDict(TypedDict):
    r"""Supplier"""

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
    data: SupplierTypedDict


class GetSupplierResponse(BaseModel):
    r"""Supplier"""

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

    data: Supplier
