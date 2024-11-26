"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .unifiedid import UnifiedID, UnifiedIDTypedDict
from apideck.types import BaseModel
from typing_extensions import TypedDict


class DeleteCommentResponseTypedDict(TypedDict):
    r"""Delete a Comment"""

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
    data: UnifiedIDTypedDict


class DeleteCommentResponse(BaseModel):
    r"""Delete a Comment"""

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

    data: UnifiedID
