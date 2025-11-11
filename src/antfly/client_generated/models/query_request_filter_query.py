from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueryRequestFilterQuery")


@_attrs_define
class QueryRequestFilterQuery:
    """Bleve query applied as an AND condition. Documents must match both the main query
    and this filter. Applied before scoring for better performance.

    Use for:
    - Status filtering: `"status:published"`
    - Date ranges: `"created_at:>2023-01-01"`
    - Category filtering: `"category:technology AND language:en"`

        Example:
            {'query': 'category:technology AND year:>2020'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_request_filter_query = cls()

        query_request_filter_query.additional_properties = d
        return query_request_filter_query

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
