"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address import Address, AddressTypedDict
from .customfield import CustomField, CustomFieldTypedDict
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .email import Email, EmailTypedDict
from .passthroughbody import PassThroughBody, PassThroughBodyTypedDict
from .phonenumber import PhoneNumber, PhoneNumberTypedDict
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from datetime import date, datetime
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ApplicantType(str, Enum):
    r"""The type of website"""

    PRIMARY = "primary"
    SECONDARY = "secondary"
    WORK = "work"
    PERSONAL = "personal"
    OTHER = "other"


class WebsitesTypedDict(TypedDict):
    url: str
    r"""The website URL"""
    id: NotRequired[Nullable[str]]
    r"""Unique identifier for the website"""
    type: NotRequired[Nullable[ApplicantType]]
    r"""The type of website"""


class Websites(BaseModel):
    url: str
    r"""The website URL"""

    id: OptionalNullable[str] = UNSET
    r"""Unique identifier for the website"""

    type: OptionalNullable[ApplicantType] = UNSET
    r"""The type of website"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "type"]
        nullable_fields = ["id", "type"]
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


class SocialLinksTypedDict(TypedDict):
    url: str
    r"""URL of the social link, e.g. https://www.twitter.com/apideck"""
    id: NotRequired[Nullable[str]]
    r"""Unique identifier of the social link"""
    type: NotRequired[Nullable[str]]
    r"""Type of the social link, e.g. twitter"""


class SocialLinks(BaseModel):
    url: str
    r"""URL of the social link, e.g. https://www.twitter.com/apideck"""

    id: OptionalNullable[str] = UNSET
    r"""Unique identifier of the social link"""

    type: OptionalNullable[str] = UNSET
    r"""Type of the social link, e.g. twitter"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id", "type"]
        nullable_fields = ["id", "type"]
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


class ApplicantTypedDict(TypedDict):
    id: NotRequired[str]
    r"""A unique identifier for an object."""
    name: NotRequired[str]
    r"""The name of an applicant."""
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the person."""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the person."""
    middle_name: NotRequired[Nullable[str]]
    r"""Middle name of the person."""
    initials: NotRequired[Nullable[str]]
    r"""The initials of the person, usually derived from their first, middle, and last names."""
    birthday: NotRequired[Nullable[date]]
    r"""The date of birth of the person."""
    cover_letter: NotRequired[str]
    job_url: NotRequired[Nullable[str]]
    photo_url: NotRequired[Nullable[str]]
    r"""The URL of the photo of a person."""
    headline: NotRequired[str]
    r"""Typically a list of previous companies where the contact has worked or schools that the contact has attended"""
    title: NotRequired[Nullable[str]]
    r"""The job title of the person."""
    emails: NotRequired[List[EmailTypedDict]]
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    phone_numbers: NotRequired[List[PhoneNumberTypedDict]]
    addresses: NotRequired[List[AddressTypedDict]]
    websites: NotRequired[List[WebsitesTypedDict]]
    social_links: NotRequired[List[SocialLinksTypedDict]]
    stage_id: NotRequired[str]
    recruiter_id: NotRequired[str]
    coordinator_id: NotRequired[str]
    application_ids: NotRequired[Nullable[List[str]]]
    applications: NotRequired[Nullable[List[str]]]
    followers: NotRequired[Nullable[List[str]]]
    sources: NotRequired[Nullable[List[str]]]
    source_id: NotRequired[str]
    confidential: NotRequired[bool]
    anonymized: NotRequired[bool]
    tags: NotRequired[Nullable[List[str]]]
    archived: NotRequired[Nullable[bool]]
    last_interaction_at: NotRequired[Nullable[datetime]]
    owner_id: NotRequired[Nullable[str]]
    sourced_by: NotRequired[Nullable[str]]
    cv_url: NotRequired[str]
    record_url: NotRequired[Nullable[str]]
    rejected_at: NotRequired[Nullable[datetime]]
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    deleted: NotRequired[Nullable[bool]]
    r"""Flag to indicate if the object is deleted."""
    deleted_by: NotRequired[Nullable[str]]
    r"""The user who deleted the object."""
    deleted_at: NotRequired[Nullable[datetime]]
    r"""The time at which the object was deleted."""
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


class Applicant(BaseModel):
    id: Optional[str] = None
    r"""A unique identifier for an object."""

    name: Optional[str] = None
    r"""The name of an applicant."""

    first_name: OptionalNullable[str] = UNSET
    r"""The first name of the person."""

    last_name: OptionalNullable[str] = UNSET
    r"""The last name of the person."""

    middle_name: OptionalNullable[str] = UNSET
    r"""Middle name of the person."""

    initials: OptionalNullable[str] = UNSET
    r"""The initials of the person, usually derived from their first, middle, and last names."""

    birthday: OptionalNullable[date] = UNSET
    r"""The date of birth of the person."""

    cover_letter: Optional[str] = None

    job_url: OptionalNullable[str] = UNSET

    photo_url: OptionalNullable[str] = UNSET
    r"""The URL of the photo of a person."""

    headline: Optional[str] = None
    r"""Typically a list of previous companies where the contact has worked or schools that the contact has attended"""

    title: OptionalNullable[str] = UNSET
    r"""The job title of the person."""

    emails: Optional[List[Email]] = None

    custom_fields: Optional[List[CustomField]] = None

    phone_numbers: Optional[List[PhoneNumber]] = None

    addresses: Optional[List[Address]] = None

    websites: Optional[List[Websites]] = None

    social_links: Optional[List[SocialLinks]] = None

    stage_id: Optional[str] = None

    recruiter_id: Optional[str] = None

    coordinator_id: Optional[str] = None

    application_ids: OptionalNullable[List[str]] = UNSET

    applications: OptionalNullable[List[str]] = UNSET

    followers: OptionalNullable[List[str]] = UNSET

    sources: OptionalNullable[List[str]] = UNSET

    source_id: Optional[str] = None

    confidential: Optional[bool] = None

    anonymized: Optional[bool] = None

    tags: OptionalNullable[List[str]] = UNSET

    archived: OptionalNullable[bool] = UNSET

    last_interaction_at: OptionalNullable[datetime] = UNSET

    owner_id: OptionalNullable[str] = UNSET

    sourced_by: OptionalNullable[str] = UNSET

    cv_url: Optional[str] = None

    record_url: OptionalNullable[str] = UNSET

    rejected_at: OptionalNullable[datetime] = UNSET

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    deleted: OptionalNullable[bool] = UNSET
    r"""Flag to indicate if the object is deleted."""

    deleted_by: OptionalNullable[str] = UNSET
    r"""The user who deleted the object."""

    deleted_at: OptionalNullable[datetime] = UNSET
    r"""The time at which the object was deleted."""

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
            "first_name",
            "last_name",
            "middle_name",
            "initials",
            "birthday",
            "cover_letter",
            "job_url",
            "photo_url",
            "headline",
            "title",
            "emails",
            "custom_fields",
            "phone_numbers",
            "addresses",
            "websites",
            "social_links",
            "stage_id",
            "recruiter_id",
            "coordinator_id",
            "application_ids",
            "applications",
            "followers",
            "sources",
            "source_id",
            "confidential",
            "anonymized",
            "tags",
            "archived",
            "last_interaction_at",
            "owner_id",
            "sourced_by",
            "cv_url",
            "record_url",
            "rejected_at",
            "custom_mappings",
            "deleted",
            "deleted_by",
            "deleted_at",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
            "pass_through",
        ]
        nullable_fields = [
            "first_name",
            "last_name",
            "middle_name",
            "initials",
            "birthday",
            "job_url",
            "photo_url",
            "title",
            "application_ids",
            "applications",
            "followers",
            "sources",
            "tags",
            "archived",
            "last_interaction_at",
            "owner_id",
            "sourced_by",
            "record_url",
            "rejected_at",
            "custom_mappings",
            "deleted",
            "deleted_by",
            "deleted_at",
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


class ApplicantInputTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The name of an applicant."""
    first_name: NotRequired[Nullable[str]]
    r"""The first name of the person."""
    last_name: NotRequired[Nullable[str]]
    r"""The last name of the person."""
    middle_name: NotRequired[Nullable[str]]
    r"""Middle name of the person."""
    initials: NotRequired[Nullable[str]]
    r"""The initials of the person, usually derived from their first, middle, and last names."""
    birthday: NotRequired[Nullable[date]]
    r"""The date of birth of the person."""
    cover_letter: NotRequired[str]
    photo_url: NotRequired[Nullable[str]]
    r"""The URL of the photo of a person."""
    headline: NotRequired[str]
    r"""Typically a list of previous companies where the contact has worked or schools that the contact has attended"""
    title: NotRequired[Nullable[str]]
    r"""The job title of the person."""
    emails: NotRequired[List[EmailTypedDict]]
    custom_fields: NotRequired[List[CustomFieldTypedDict]]
    phone_numbers: NotRequired[List[PhoneNumberTypedDict]]
    addresses: NotRequired[List[AddressTypedDict]]
    websites: NotRequired[List[WebsitesTypedDict]]
    social_links: NotRequired[List[SocialLinksTypedDict]]
    stage_id: NotRequired[str]
    recruiter_id: NotRequired[str]
    coordinator_id: NotRequired[str]
    application_ids: NotRequired[Nullable[List[str]]]
    applications: NotRequired[Nullable[List[str]]]
    followers: NotRequired[Nullable[List[str]]]
    sources: NotRequired[Nullable[List[str]]]
    confidential: NotRequired[bool]
    anonymized: NotRequired[bool]
    tags: NotRequired[Nullable[List[str]]]
    archived: NotRequired[Nullable[bool]]
    owner_id: NotRequired[Nullable[str]]
    record_url: NotRequired[Nullable[str]]
    deleted: NotRequired[Nullable[bool]]
    r"""Flag to indicate if the object is deleted."""
    pass_through: NotRequired[List[PassThroughBodyTypedDict]]
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""


class ApplicantInput(BaseModel):
    name: Optional[str] = None
    r"""The name of an applicant."""

    first_name: OptionalNullable[str] = UNSET
    r"""The first name of the person."""

    last_name: OptionalNullable[str] = UNSET
    r"""The last name of the person."""

    middle_name: OptionalNullable[str] = UNSET
    r"""Middle name of the person."""

    initials: OptionalNullable[str] = UNSET
    r"""The initials of the person, usually derived from their first, middle, and last names."""

    birthday: OptionalNullable[date] = UNSET
    r"""The date of birth of the person."""

    cover_letter: Optional[str] = None

    photo_url: OptionalNullable[str] = UNSET
    r"""The URL of the photo of a person."""

    headline: Optional[str] = None
    r"""Typically a list of previous companies where the contact has worked or schools that the contact has attended"""

    title: OptionalNullable[str] = UNSET
    r"""The job title of the person."""

    emails: Optional[List[Email]] = None

    custom_fields: Optional[List[CustomField]] = None

    phone_numbers: Optional[List[PhoneNumber]] = None

    addresses: Optional[List[Address]] = None

    websites: Optional[List[Websites]] = None

    social_links: Optional[List[SocialLinks]] = None

    stage_id: Optional[str] = None

    recruiter_id: Optional[str] = None

    coordinator_id: Optional[str] = None

    application_ids: OptionalNullable[List[str]] = UNSET

    applications: OptionalNullable[List[str]] = UNSET

    followers: OptionalNullable[List[str]] = UNSET

    sources: OptionalNullable[List[str]] = UNSET

    confidential: Optional[bool] = None

    anonymized: Optional[bool] = None

    tags: OptionalNullable[List[str]] = UNSET

    archived: OptionalNullable[bool] = UNSET

    owner_id: OptionalNullable[str] = UNSET

    record_url: OptionalNullable[str] = UNSET

    deleted: OptionalNullable[bool] = UNSET
    r"""Flag to indicate if the object is deleted."""

    pass_through: Optional[List[PassThroughBody]] = None
    r"""The pass_through property allows passing service-specific, custom data or structured modifications in request body when creating or updating resources."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "first_name",
            "last_name",
            "middle_name",
            "initials",
            "birthday",
            "cover_letter",
            "photo_url",
            "headline",
            "title",
            "emails",
            "custom_fields",
            "phone_numbers",
            "addresses",
            "websites",
            "social_links",
            "stage_id",
            "recruiter_id",
            "coordinator_id",
            "application_ids",
            "applications",
            "followers",
            "sources",
            "confidential",
            "anonymized",
            "tags",
            "archived",
            "owner_id",
            "record_url",
            "deleted",
            "pass_through",
        ]
        nullable_fields = [
            "first_name",
            "last_name",
            "middle_name",
            "initials",
            "birthday",
            "photo_url",
            "title",
            "application_ids",
            "applications",
            "followers",
            "sources",
            "tags",
            "archived",
            "owner_id",
            "record_url",
            "deleted",
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
