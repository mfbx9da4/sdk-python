"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class Audience(str, Enum):
    r"""Audience for the doc."""

    APPLICATION_OWNER = "application_owner"
    CONSUMER = "consumer"


class Format(str, Enum):
    r"""Format of the doc."""

    MARKDOWN = "markdown"


class ConnectorDocTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    name: NotRequired[str]
    r"""Name of the doc."""
    audience: NotRequired[Audience]
    r"""Audience for the doc."""
    format: NotRequired[Format]
    r"""Format of the doc."""
    url: NotRequired[str]
    r"""Link to fetch the content of the doc."""


class ConnectorDoc(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    name: Optional[str] = None
    r"""Name of the doc."""

    audience: Optional[Audience] = None
    r"""Audience for the doc."""

    format: Optional[Format] = None
    r"""Format of the doc."""

    url: Optional[str] = None
    r"""Link to fetch the content of the doc."""
