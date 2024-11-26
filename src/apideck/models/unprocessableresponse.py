"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck import utils
from apideck.types import BaseModel
from typing import Optional, Union
from typing_extensions import TypeAliasType, TypedDict


class DetailUnprocessableResponse2TypedDict(TypedDict):
    pass


class DetailUnprocessableResponse2(BaseModel):
    pass


UnprocessableResponseDetailTypedDict = TypeAliasType(
    "UnprocessableResponseDetailTypedDict",
    Union[DetailUnprocessableResponse2TypedDict, str],
)
r"""Contains parameter or domain specific information related to the error and why it occurred."""


UnprocessableResponseDetail = TypeAliasType(
    "UnprocessableResponseDetail", Union[DetailUnprocessableResponse2, str]
)
r"""Contains parameter or domain specific information related to the error and why it occurred."""


class UnprocessableResponseData(BaseModel):
    status_code: Optional[float] = None
    r"""HTTP status code"""

    error: Optional[str] = None
    r"""Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 7231)"""

    type_name: Optional[str] = None
    r"""The type of error returned"""

    message: Optional[str] = None
    r"""A human-readable message providing more details about the error."""

    detail: Optional[UnprocessableResponseDetail] = None
    r"""Contains parameter or domain specific information related to the error and why it occurred."""

    ref: Optional[str] = None
    r"""Link to documentation of error type"""


class UnprocessableResponse(Exception):
    r"""Unprocessable"""

    data: UnprocessableResponseData

    def __init__(self, data: UnprocessableResponseData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, UnprocessableResponseData)
