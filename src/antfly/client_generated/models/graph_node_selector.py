from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphNodeSelector")


@_attrs_define
class GraphNodeSelector:
    """Defines how to select start/target nodes for graph queries

    Attributes:
        keys (Union[Unset, list[str]]): Explicit list of node keys
        result_ref (Union[Unset, str]): Reference to search results to use as nodes:
            - "$full_text_results" - use full-text search results
            - "$aknn_results.index_name" - use vector search results from specific index
        limit (Union[Unset, int]): Maximum number of nodes to select from the referenced results
    """

    keys: Union[Unset, list[str]] = UNSET
    result_ref: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        result_ref = self.result_ref

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keys is not UNSET:
            field_dict["keys"] = keys
        if result_ref is not UNSET:
            field_dict["result_ref"] = result_ref
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keys = cast(list[str], d.pop("keys", UNSET))

        result_ref = d.pop("result_ref", UNSET)

        limit = d.pop("limit", UNSET)

        graph_node_selector = cls(
            keys=keys,
            result_ref=result_ref,
            limit=limit,
        )

        graph_node_selector.additional_properties = d
        return graph_node_selector

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
