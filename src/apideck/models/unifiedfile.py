"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .custommappings import CustomMappings, CustomMappingsTypedDict
from .filetype import FileType
from .linkedfolder import LinkedFolder, LinkedFolderTypedDict
from .owner import Owner, OwnerTypedDict
from apideck.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from datetime import datetime
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PermissionsTypedDict(TypedDict):
    r"""Permissions the current user has on this file."""

    download: NotRequired[bool]
    r"""Whether the current user can download this file."""


class Permissions(BaseModel):
    r"""Permissions the current user has on this file."""

    download: Optional[bool] = None
    r"""Whether the current user can download this file."""


class UnifiedFileTypedDict(TypedDict):
    id: str
    r"""A unique identifier for an object."""
    name: Nullable[str]
    r"""The name of the file"""
    type: Nullable[FileType]
    r"""The type of resource. Could be file, folder or url"""
    downstream_id: NotRequired[Nullable[str]]
    r"""The third-party API ID of original entity"""
    description: NotRequired[Nullable[str]]
    r"""Optional description of the file"""
    path: NotRequired[Nullable[str]]
    r"""The full path of the file or folder (includes the file name)"""
    mime_type: NotRequired[Nullable[str]]
    r"""The MIME type of the file."""
    downloadable: NotRequired[bool]
    r"""Whether the current user can download this file"""
    size: NotRequired[Nullable[int]]
    r"""The size of the file in bytes"""
    owner: NotRequired[OwnerTypedDict]
    parent_folders: NotRequired[List[LinkedFolderTypedDict]]
    r"""The parent folders of the file, starting from the root"""
    parent_folders_complete: NotRequired[bool]
    r"""Whether the list of parent folders is complete. Some connectors only return the direct parent of a file"""
    permissions: NotRequired[PermissionsTypedDict]
    r"""Permissions the current user has on this file."""
    exportable: NotRequired[bool]
    r"""Whether the current file is exportable to other file formats. This property is relevant for proprietary file formats such as Google Docs or Dropbox Paper."""
    export_formats: NotRequired[Nullable[List[str]]]
    r"""The available file formats when exporting this file."""
    custom_mappings: NotRequired[Nullable[CustomMappingsTypedDict]]
    r"""When custom mappings are configured on the resource, the result is included here."""
    updated_by: NotRequired[Nullable[str]]
    r"""The user who last updated the object."""
    created_by: NotRequired[Nullable[str]]
    r"""The user who created the object."""
    updated_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was last updated."""
    created_at: NotRequired[Nullable[datetime]]
    r"""The date and time when the object was created."""


class UnifiedFile(BaseModel):
    id: str
    r"""A unique identifier for an object."""

    name: Nullable[str]
    r"""The name of the file"""

    type: Nullable[FileType]
    r"""The type of resource. Could be file, folder or url"""

    downstream_id: OptionalNullable[str] = UNSET
    r"""The third-party API ID of original entity"""

    description: OptionalNullable[str] = UNSET
    r"""Optional description of the file"""

    path: OptionalNullable[str] = UNSET
    r"""The full path of the file or folder (includes the file name)"""

    mime_type: OptionalNullable[str] = UNSET
    r"""The MIME type of the file."""

    downloadable: Optional[bool] = None
    r"""Whether the current user can download this file"""

    size: OptionalNullable[int] = UNSET
    r"""The size of the file in bytes"""

    owner: Optional[Owner] = None

    parent_folders: Optional[List[LinkedFolder]] = None
    r"""The parent folders of the file, starting from the root"""

    parent_folders_complete: Optional[bool] = None
    r"""Whether the list of parent folders is complete. Some connectors only return the direct parent of a file"""

    permissions: Optional[Permissions] = None
    r"""Permissions the current user has on this file."""

    exportable: Optional[bool] = None
    r"""Whether the current file is exportable to other file formats. This property is relevant for proprietary file formats such as Google Docs or Dropbox Paper."""

    export_formats: OptionalNullable[List[str]] = UNSET
    r"""The available file formats when exporting this file."""

    custom_mappings: OptionalNullable[CustomMappings] = UNSET
    r"""When custom mappings are configured on the resource, the result is included here."""

    updated_by: OptionalNullable[str] = UNSET
    r"""The user who last updated the object."""

    created_by: OptionalNullable[str] = UNSET
    r"""The user who created the object."""

    updated_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was last updated."""

    created_at: OptionalNullable[datetime] = UNSET
    r"""The date and time when the object was created."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "downstream_id",
            "description",
            "path",
            "mime_type",
            "downloadable",
            "size",
            "owner",
            "parent_folders",
            "parent_folders_complete",
            "permissions",
            "exportable",
            "export_formats",
            "custom_mappings",
            "updated_by",
            "created_by",
            "updated_at",
            "created_at",
        ]
        nullable_fields = [
            "name",
            "type",
            "downstream_id",
            "description",
            "path",
            "mime_type",
            "size",
            "export_formats",
            "custom_mappings",
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
