from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.value_type import ValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_schema import DocumentSchema


T = TypeVar("T", bound="ValueSchema")


@_attrs_define
class ValueSchema:
    """
    Attributes:
        type_ (ValueType): Field type (e.g., string, int, float)
        schema (Union[Unset, DocumentSchema]):
    """

    type_: ValueType
    schema: Union[Unset, "DocumentSchema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_schema import DocumentSchema

        d = dict(src_dict)
        type_ = ValueType(d.pop("type"))

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, DocumentSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = DocumentSchema.from_dict(_schema)

        value_schema = cls(
            type_=type_,
            schema=schema,
        )

        value_schema.additional_properties = d
        return value_schema

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
