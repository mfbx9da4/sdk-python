"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .deprecatedlinkedtrackingcategory import (
    DeprecatedLinkedTrackingCategory,
    DeprecatedLinkedTrackingCategoryTypedDict,
)
from .linkedledgeraccount import LinkedLedgerAccount, LinkedLedgerAccountTypedDict
from .linkedledgeraccount_input import (
    LinkedLedgerAccountInput,
    LinkedLedgerAccountInputTypedDict,
)
from .linkedtaxrate import LinkedTaxRate, LinkedTaxRateTypedDict
from .linkedtaxrate_input import LinkedTaxRateInput, LinkedTaxRateInputTypedDict
from .linkedtrackingcategory import (
    LinkedTrackingCategory,
    LinkedTrackingCategoryTypedDict,
)
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from datetime import date, datetime
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class InvoiceItemType(str, Enum):
    r"""Item type"""

    INVENTORY = "inventory"
    SERVICE = "service"
    OTHER = "other"


class SalesDetailsTypedDict(TypedDict):
    unit_price: NotRequired[Nullable[float]]
    unit_of_measure: NotRequired[Nullable[str]]
    r"""Description of the unit type the item is sold as, ie: kg, hour."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    tax_rate: NotRequired[LinkedTaxRateTypedDict]


class SalesDetails(BaseModel):
    unit_price: OptionalNullable[float] = UNSET

    unit_of_measure: OptionalNullable[str] = UNSET
    r"""Description of the unit type the item is sold as, ie: kg, hour."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    tax_rate: Optional[LinkedTaxRate] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["unit_price", "unit_of_measure", "tax_inclusive", "tax_rate"]
        nullable_fields = ["unit_price", "unit_of_measure", "tax_inclusive"]
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


class PurchaseDetailsTypedDict(TypedDict):
    unit_price: NotRequired[Nullable[float]]
    unit_of_measure: NotRequired[Nullable[str]]
    r"""Description of the unit type the item is sold as, ie: kg, hour."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    tax_rate: NotRequired[LinkedTaxRateTypedDict]


class PurchaseDetails(BaseModel):
    unit_price: OptionalNullable[float] = UNSET

    unit_of_measure: OptionalNullable[str] = UNSET
    r"""Description of the unit type the item is sold as, ie: kg, hour."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    tax_rate: Optional[LinkedTaxRate] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["unit_price", "unit_of_measure", "tax_inclusive", "tax_rate"]
        nullable_fields = ["unit_price", "unit_of_measure", "tax_inclusive"]
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


class InvoiceItemTypedDict(TypedDict):
    id: NotRequired[str]
    r"""The ID of the item."""
    name: NotRequired[Nullable[str]]
    r"""Item name"""
    description: NotRequired[Nullable[str]]
    r"""A short description of the item"""
    code: NotRequired[Nullable[str]]
    r"""User defined item code"""
    sold: NotRequired[Nullable[bool]]
    r"""Item will be available on sales transactions"""
    purchased: NotRequired[Nullable[bool]]
    r"""Item is available for purchase transactions"""
    tracked: NotRequired[Nullable[bool]]
    r"""Item is inventoried"""
    taxable: NotRequired[Nullable[bool]]
    r"""If true, transactions for this item are taxable"""
    inventory_date: NotRequired[Nullable[date]]
    r"""The date of opening balance if inventory item is tracked - YYYY-MM-DD."""
    type: NotRequired[Nullable[InvoiceItemType]]
    r"""Item type"""
    sales_details: NotRequired[SalesDetailsTypedDict]
    purchase_details: NotRequired[PurchaseDetailsTypedDict]
    quantity: NotRequired[Nullable[float]]
    unit_price: NotRequired[Nullable[float]]
    asset_account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    income_account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    expense_account: NotRequired[Nullable[LinkedLedgerAccountTypedDict]]
    tracking_category: NotRequired[Nullable[DeprecatedLinkedTrackingCategoryTypedDict]]
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
    active: NotRequired[Nullable[bool]]
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    updated_by: NotRequired[Nullable[str]]
    r"""The user who last updated the object."""
    created_by: NotRequired[Nullable[str]]
    r"""The user who created the object."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was last updated."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class InvoiceItem(BaseModel):
    id: Optional[str] = None
    r"""The ID of the item."""

    name: OptionalNullable[str] = UNSET
    r"""Item name"""

    description: OptionalNullable[str] = UNSET
    r"""A short description of the item"""

    code: OptionalNullable[str] = UNSET
    r"""User defined item code"""

    sold: OptionalNullable[bool] = UNSET
    r"""Item will be available on sales transactions"""

    purchased: OptionalNullable[bool] = UNSET
    r"""Item is available for purchase transactions"""

    tracked: OptionalNullable[bool] = UNSET
    r"""Item is inventoried"""

    taxable: OptionalNullable[bool] = UNSET
    r"""If true, transactions for this item are taxable"""

    inventory_date: OptionalNullable[date] = UNSET
    r"""The date of opening balance if inventory item is tracked - YYYY-MM-DD."""

    type: OptionalNullable[InvoiceItemType] = UNSET
    r"""Item type"""

    sales_details: Optional[SalesDetails] = None

    purchase_details: Optional[PurchaseDetails] = None

    quantity: OptionalNullable[float] = UNSET

    unit_price: OptionalNullable[float] = UNSET

    asset_account: OptionalNullable[LinkedLedgerAccount] = UNSET

    income_account: OptionalNullable[LinkedLedgerAccount] = UNSET

    expense_account: OptionalNullable[LinkedLedgerAccount] = UNSET

    tracking_category: Annotated[
        OptionalNullable[DeprecatedLinkedTrackingCategory],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = UNSET

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

    active: OptionalNullable[bool] = UNSET

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    updated_by: OptionalNullable[str] = UNSET
    r"""The user who last updated the object."""

    created_by: OptionalNullable[str] = UNSET
    r"""The user who created the object."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was last updated."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "name",
            "description",
            "code",
            "sold",
            "purchased",
            "tracked",
            "taxable",
            "inventory_date",
            "type",
            "sales_details",
            "purchase_details",
            "quantity",
            "unit_price",
            "asset_account",
            "income_account",
            "expense_account",
            "tracking_category",
            "tracking_categories",
            "active",
            "custom_mappings",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "name",
            "description",
            "code",
            "sold",
            "purchased",
            "tracked",
            "taxable",
            "inventory_date",
            "type",
            "quantity",
            "unit_price",
            "asset_account",
            "income_account",
            "expense_account",
            "tracking_category",
            "tracking_categories",
            "active",
            "custom_mappings",
            "row_version",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
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


class InvoiceItemSalesDetailsTypedDict(TypedDict):
    unit_price: NotRequired[Nullable[float]]
    unit_of_measure: NotRequired[Nullable[str]]
    r"""Description of the unit type the item is sold as, ie: kg, hour."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    tax_rate: NotRequired[LinkedTaxRateInputTypedDict]


class InvoiceItemSalesDetails(BaseModel):
    unit_price: OptionalNullable[float] = UNSET

    unit_of_measure: OptionalNullable[str] = UNSET
    r"""Description of the unit type the item is sold as, ie: kg, hour."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    tax_rate: Optional[LinkedTaxRateInput] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["unit_price", "unit_of_measure", "tax_inclusive", "tax_rate"]
        nullable_fields = ["unit_price", "unit_of_measure", "tax_inclusive"]
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


class InvoiceItemPurchaseDetailsTypedDict(TypedDict):
    unit_price: NotRequired[Nullable[float]]
    unit_of_measure: NotRequired[Nullable[str]]
    r"""Description of the unit type the item is sold as, ie: kg, hour."""
    tax_inclusive: NotRequired[Nullable[bool]]
    r"""Amounts are including tax"""
    tax_rate: NotRequired[LinkedTaxRateInputTypedDict]


class InvoiceItemPurchaseDetails(BaseModel):
    unit_price: OptionalNullable[float] = UNSET

    unit_of_measure: OptionalNullable[str] = UNSET
    r"""Description of the unit type the item is sold as, ie: kg, hour."""

    tax_inclusive: OptionalNullable[bool] = UNSET
    r"""Amounts are including tax"""

    tax_rate: Optional[LinkedTaxRateInput] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["unit_price", "unit_of_measure", "tax_inclusive", "tax_rate"]
        nullable_fields = ["unit_price", "unit_of_measure", "tax_inclusive"]
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


class InvoiceItemInputTypedDict(TypedDict):
    name: NotRequired[Nullable[str]]
    r"""Item name"""
    description: NotRequired[Nullable[str]]
    r"""A short description of the item"""
    code: NotRequired[Nullable[str]]
    r"""User defined item code"""
    sold: NotRequired[Nullable[bool]]
    r"""Item will be available on sales transactions"""
    purchased: NotRequired[Nullable[bool]]
    r"""Item is available for purchase transactions"""
    tracked: NotRequired[Nullable[bool]]
    r"""Item is inventoried"""
    taxable: NotRequired[Nullable[bool]]
    r"""If true, transactions for this item are taxable"""
    inventory_date: NotRequired[Nullable[date]]
    r"""The date of opening balance if inventory item is tracked - YYYY-MM-DD."""
    type: NotRequired[Nullable[InvoiceItemType]]
    r"""Item type"""
    sales_details: NotRequired[InvoiceItemSalesDetailsTypedDict]
    purchase_details: NotRequired[InvoiceItemPurchaseDetailsTypedDict]
    quantity: NotRequired[Nullable[float]]
    unit_price: NotRequired[Nullable[float]]
    asset_account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    income_account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    expense_account: NotRequired[Nullable[LinkedLedgerAccountInputTypedDict]]
    tracking_category: NotRequired[Nullable[DeprecatedLinkedTrackingCategoryTypedDict]]
    tracking_categories: NotRequired[Nullable[List[LinkedTrackingCategoryTypedDict]]]
    r"""A list of linked tracking categories."""
    active: NotRequired[Nullable[bool]]
    row_version: NotRequired[Nullable[str]]
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class InvoiceItemInput(BaseModel):
    name: OptionalNullable[str] = UNSET
    r"""Item name"""

    description: OptionalNullable[str] = UNSET
    r"""A short description of the item"""

    code: OptionalNullable[str] = UNSET
    r"""User defined item code"""

    sold: OptionalNullable[bool] = UNSET
    r"""Item will be available on sales transactions"""

    purchased: OptionalNullable[bool] = UNSET
    r"""Item is available for purchase transactions"""

    tracked: OptionalNullable[bool] = UNSET
    r"""Item is inventoried"""

    taxable: OptionalNullable[bool] = UNSET
    r"""If true, transactions for this item are taxable"""

    inventory_date: OptionalNullable[date] = UNSET
    r"""The date of opening balance if inventory item is tracked - YYYY-MM-DD."""

    type: OptionalNullable[InvoiceItemType] = UNSET
    r"""Item type"""

    sales_details: Optional[InvoiceItemSalesDetails] = None

    purchase_details: Optional[InvoiceItemPurchaseDetails] = None

    quantity: OptionalNullable[float] = UNSET

    unit_price: OptionalNullable[float] = UNSET

    asset_account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    income_account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    expense_account: OptionalNullable[LinkedLedgerAccountInput] = UNSET

    tracking_category: Annotated[
        OptionalNullable[DeprecatedLinkedTrackingCategory],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = UNSET

    tracking_categories: OptionalNullable[List[LinkedTrackingCategory]] = UNSET
    r"""A list of linked tracking categories."""

    active: OptionalNullable[bool] = UNSET

    row_version: OptionalNullable[str] = UNSET
    r"""A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "description",
            "code",
            "sold",
            "purchased",
            "tracked",
            "taxable",
            "inventory_date",
            "type",
            "sales_details",
            "purchase_details",
            "quantity",
            "unit_price",
            "asset_account",
            "income_account",
            "expense_account",
            "tracking_category",
            "tracking_categories",
            "active",
            "row_version",
            "pass_through",
        ]
        nullable_fields = [
            "name",
            "description",
            "code",
            "sold",
            "purchased",
            "tracked",
            "taxable",
            "inventory_date",
            "type",
            "quantity",
            "unit_price",
            "asset_account",
            "income_account",
            "expense_account",
            "tracking_category",
            "tracking_categories",
            "active",
            "row_version",
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
