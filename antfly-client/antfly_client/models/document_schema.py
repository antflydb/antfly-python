from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_schema_fields import DocumentSchemaFields


T = TypeVar("T", bound="DocumentSchema")


@_attrs_define
class DocumentSchema:
    """
    Attributes:
        fields (Union[Unset, DocumentSchemaFields]): A map of field names to their value schema (type, defaults,
            configuration etc.).
            This allows for flexible content types per field.
            The key is the field name, and the value is the value type schema.
    """

    fields: Union[Unset, "DocumentSchemaFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_schema_fields import DocumentSchemaFields

        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: Union[Unset, DocumentSchemaFields]
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = DocumentSchemaFields.from_dict(_fields)

        document_schema = cls(
            fields=fields,
        )

        document_schema.additional_properties = d
        return document_schema

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
