from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TermiteChunkerConfigFullText")


@_attrs_define
class TermiteChunkerConfigFullText:
    """Configuration for full-text indexing of chunks in Bleve.
    When present (even if empty), chunks will be stored with :cft: suffix and indexed in Bleve's _chunks field.
    When absent, chunks use :c: suffix and are only used for vector embeddings.
    This object is reserved for future options like boosting, field mapping, etc.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        termite_chunker_config_full_text = cls()

        termite_chunker_config_full_text.additional_properties = d
        return termite_chunker_config_full_text

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
