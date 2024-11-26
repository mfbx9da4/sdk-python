"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .webhook import Webhook, WebhookTypedDict
from apideck.types import BaseModel
from typing_extensions import TypedDict


class DeleteWebhookResponseTypedDict(TypedDict):
    r"""Webhooks"""

    status_code: int
    r"""HTTP Response Status Code"""
    status: str
    r"""HTTP Response Status"""
    data: WebhookTypedDict


class DeleteWebhookResponse(BaseModel):
    r"""Webhooks"""

    status_code: int
    r"""HTTP Response Status Code"""

    status: str
    r"""HTTP Response Status"""

    data: Webhook
