from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_schema_document_schemas import TableSchemaDocumentSchemas
    from ..models.table_schema_document_types import TableSchemaDocumentTypes


T = TypeVar("T", bound="TableSchema")


@_attrs_define
class TableSchema:
    """
    Attributes:
        key (Union[Unset, str]):
        default_type (Union[Unset, str]): Default type to use from the document_types.
        document_types (Union[Unset, TableSchemaDocumentTypes]): A map of type names to their content schemas.
            The key is the type name, and the value is the schema for that document type.
            This allows for flexible content types per field.
        document_schemas (Union[Unset, TableSchemaDocumentSchemas]): A map of type names to their document json schemas.
    """

    key: Union[Unset, str] = UNSET
    default_type: Union[Unset, str] = UNSET
    document_types: Union[Unset, "TableSchemaDocumentTypes"] = UNSET
    document_schemas: Union[Unset, "TableSchemaDocumentSchemas"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        default_type = self.default_type

        document_types: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_types, Unset):
            document_types = self.document_types.to_dict()

        document_schemas: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_schemas, Unset):
            document_schemas = self.document_schemas.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if default_type is not UNSET:
            field_dict["default_type"] = default_type
        if document_types is not UNSET:
            field_dict["document_types"] = document_types
        if document_schemas is not UNSET:
            field_dict["document_schemas"] = document_schemas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_schema_document_schemas import TableSchemaDocumentSchemas
        from ..models.table_schema_document_types import TableSchemaDocumentTypes

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        default_type = d.pop("default_type", UNSET)

        _document_types = d.pop("document_types", UNSET)
        document_types: Union[Unset, TableSchemaDocumentTypes]
        if isinstance(_document_types, Unset):
            document_types = UNSET
        else:
            document_types = TableSchemaDocumentTypes.from_dict(_document_types)

        _document_schemas = d.pop("document_schemas", UNSET)
        document_schemas: Union[Unset, TableSchemaDocumentSchemas]
        if isinstance(_document_schemas, Unset):
            document_schemas = UNSET
        else:
            document_schemas = TableSchemaDocumentSchemas.from_dict(_document_schemas)

        table_schema = cls(
            key=key,
            default_type=default_type,
            document_types=document_types,
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
