from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_schema_document_schemas import TableSchemaDocumentSchemas


T = TypeVar("T", bound="TableSchema")


@_attrs_define
class TableSchema:
    """
    Attributes:
        version (Union[Unset, int]): Version of the schema. Used for migrations.
        key (Union[Unset, str]): The default field to use as the document ID (optional).
            Useful if no type-specific key is defined or if all types share the same key field.
             Example: _id.
        enforce_types (Union[Unset, bool]): Whether to enforce that documents must match one of the provided document
            types.
            If false, documents not matching any type will be accepted but not indexed.
        default_type (Union[Unset, str]): Default type to use from the document_types.
        ttl_field (Union[Unset, str]): The field containing the timestamp for TTL expiration (optional).
            Defaults to "_timestamp" if ttl_duration is specified but ttl_field is not.
             Example: created_at.
        ttl_duration (Union[Unset, str]): The duration after which documents should expire, based on the ttl_field
            timestamp (optional).
            Uses Go duration format (e.g., '24h', '7d', '168h').
             Example: 24h.
        document_schemas (Union[Unset, TableSchemaDocumentSchemas]): A map of type names to their document json schemas.
    """

    version: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    enforce_types: Union[Unset, bool] = UNSET
    default_type: Union[Unset, str] = UNSET
    ttl_field: Union[Unset, str] = UNSET
    ttl_duration: Union[Unset, str] = UNSET
    document_schemas: Union[Unset, "TableSchemaDocumentSchemas"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        key = self.key

        enforce_types = self.enforce_types

        default_type = self.default_type

        ttl_field = self.ttl_field

        ttl_duration = self.ttl_duration

        document_schemas: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_schemas, Unset):
            document_schemas = self.document_schemas.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if key is not UNSET:
            field_dict["key"] = key
        if enforce_types is not UNSET:
            field_dict["enforce_types"] = enforce_types
        if default_type is not UNSET:
            field_dict["default_type"] = default_type
        if ttl_field is not UNSET:
            field_dict["ttl_field"] = ttl_field
        if ttl_duration is not UNSET:
            field_dict["ttl_duration"] = ttl_duration
        if document_schemas is not UNSET:
            field_dict["document_schemas"] = document_schemas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_schema_document_schemas import TableSchemaDocumentSchemas

        d = dict(src_dict)
        version = d.pop("version", UNSET)

        key = d.pop("key", UNSET)

        enforce_types = d.pop("enforce_types", UNSET)

        default_type = d.pop("default_type", UNSET)

        ttl_field = d.pop("ttl_field", UNSET)

        ttl_duration = d.pop("ttl_duration", UNSET)

        _document_schemas = d.pop("document_schemas", UNSET)
        document_schemas: Union[Unset, TableSchemaDocumentSchemas]
        if isinstance(_document_schemas, Unset):
            document_schemas = UNSET
        else:
            document_schemas = TableSchemaDocumentSchemas.from_dict(_document_schemas)

        table_schema = cls(
            version=version,
            key=key,
            enforce_types=enforce_types,
            default_type=default_type,
            ttl_field=ttl_field,
            ttl_duration=ttl_duration,
            document_schemas=document_schemas,
        )

        table_schema.additional_properties = d
        return table_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
