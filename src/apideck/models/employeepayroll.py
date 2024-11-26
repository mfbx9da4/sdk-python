"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .compensation import Compensation, CompensationTypedDict
from .payrolltotals import PayrollTotals, PayrollTotalsTypedDict
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class EmployeePayrollTypedDict(TypedDict):
    id: Nullable[str]
    r"""A unique identifier for an object."""
    processed: Nullable[bool]
    r"""Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated."""
    check_date: Nullable[str]
    r"""The date on which employees will be paid for the payroll."""
    start_date: Nullable[str]
    r"""The start date, inclusive, of the pay period."""
    end_date: Nullable[str]
    r"""The end date, inclusive, of the pay period."""
    employee_id: NotRequired[Nullable[str]]
    r"""ID of the employee"""
    company_id: NotRequired[Nullable[str]]
    r"""The unique identifier of the company."""
    processed_date: NotRequired[Nullable[str]]
    r"""The date the payroll was processed."""
    totals: NotRequired[PayrollTotalsTypedDict]
    r"""The overview of the payroll totals."""
    compensations: NotRequired[List[CompensationTypedDict]]
    r"""An array of compensations for the payroll."""


class EmployeePayroll(BaseModel):
    id: Nullable[str]
    r"""A unique identifier for an object."""

    processed: Nullable[bool]
    r"""Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated."""

    check_date: Nullable[str]
    r"""The date on which employees will be paid for the payroll."""

    start_date: Nullable[str]
    r"""The start date, inclusive, of the pay period."""

    end_date: Nullable[str]
    r"""The end date, inclusive, of the pay period."""

    employee_id: OptionalNullable[str] = UNSET
    r"""ID of the employee"""

    company_id: OptionalNullable[str] = UNSET
    r"""The unique identifier of the company."""

    processed_date: OptionalNullable[str] = UNSET
    r"""The date the payroll was processed."""

    totals: Optional[PayrollTotals] = None
    r"""The overview of the payroll totals."""

    compensations: Optional[List[Compensation]] = None
    r"""An array of compensations for the payroll."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "employee_id",
            "company_id",
            "processed_date",
            "totals",
            "compensations",
        ]
        nullable_fields = [
            "id",
            "processed",
            "check_date",
            "start_date",
            "end_date",
            "employee_id",
            "company_id",
            "processed_date",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
