"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class PayrollTotalsTypedDict(TypedDict):
    r"""The overview of the payroll totals."""

    company_debit: NotRequired[Nullable[float]]
    r"""The total company debit for the payroll."""
    tax_debit: NotRequired[Nullable[float]]
    r"""The total tax debit for the payroll."""
    check_amount: NotRequired[Nullable[float]]
    r"""The total check amount for the payroll."""
    net_pay: NotRequired[Nullable[float]]
    r"""The net pay amount for the payroll."""
    gross_pay: NotRequired[Nullable[float]]
    r"""The gross pay amount for the payroll."""
    employer_taxes: NotRequired[Nullable[float]]
    r"""The total amount of employer paid taxes for the payroll."""
    employee_taxes: NotRequired[Nullable[float]]
    r"""The total amount of employee paid taxes for the payroll."""
    employer_benefit_contributions: NotRequired[Nullable[float]]
    r"""The total amount of company contributed benefits for the payroll."""
    employee_benefit_deductions: NotRequired[Nullable[float]]
    r"""The total amount of employee deducted benefits for the payroll."""


class PayrollTotals(BaseModel):
    r"""The overview of the payroll totals."""

    company_debit: OptionalNullable[float] = UNSET
    r"""The total company debit for the payroll."""

    tax_debit: OptionalNullable[float] = UNSET
    r"""The total tax debit for the payroll."""

    check_amount: OptionalNullable[float] = UNSET
    r"""The total check amount for the payroll."""

    net_pay: OptionalNullable[float] = UNSET
    r"""The net pay amount for the payroll."""

    gross_pay: OptionalNullable[float] = UNSET
    r"""The gross pay amount for the payroll."""

    employer_taxes: OptionalNullable[float] = UNSET
    r"""The total amount of employer paid taxes for the payroll."""

    employee_taxes: OptionalNullable[float] = UNSET
    r"""The total amount of employee paid taxes for the payroll."""

    employer_benefit_contributions: OptionalNullable[float] = UNSET
    r"""The total amount of company contributed benefits for the payroll."""

    employee_benefit_deductions: OptionalNullable[float] = UNSET
    r"""The total amount of employee deducted benefits for the payroll."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "company_debit",
            "tax_debit",
            "check_amount",
            "net_pay",
            "gross_pay",
            "employer_taxes",
            "employee_taxes",
            "employer_benefit_contributions",
            "employee_benefit_deductions",
        ]
        nullable_fields = [
            "company_debit",
            "tax_debit",
            "check_amount",
            "net_pay",
            "gross_pay",
            "employer_taxes",
            "employee_taxes",
            "employer_benefit_contributions",
            "employee_benefit_deductions",
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
