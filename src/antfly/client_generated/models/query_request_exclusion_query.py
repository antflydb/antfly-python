from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueryRequestExclusionQuery")


@_attrs_define
class QueryRequestExclusionQuery:
    """Bleve query applied as a NOT condition. Documents matching this query are excluded
    from results. Applied before scoring.

    Use for:
    - Excluding drafts: `"status:draft"`
    - Removing deprecated content: `"deprecated:true"`
    - Filtering out archived items: `"status:archived"`

        Example:
            {'query': 'category:deprecated OR status:archived'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_request_exclusion_query = cls()

        query_request_exclusion_query.additional_properties = d
        return query_request_exclusion_query

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
