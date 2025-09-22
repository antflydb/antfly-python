from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingIndexStats")


@_attrs_define
class EmbeddingIndexStats:
    """
    Attributes:
        error (Union[Unset, str]): Error message if stats could not be retrieved
        total_indexed (Union[Unset, int]): Number of vectors in the index
        disk_usage (Union[Unset, int]): Size of the index in bytes
        total_nodes (Union[Unset, int]): Total number of nodes in the index
    """

    error: Union[Unset, str] = UNSET
    total_indexed: Union[Unset, int] = UNSET
    disk_usage: Union[Unset, int] = UNSET
    total_nodes: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        total_indexed = self.total_indexed

        disk_usage = self.disk_usage

        total_nodes = self.total_nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if total_indexed is not UNSET:
            field_dict["total_indexed"] = total_indexed
        if disk_usage is not UNSET:
            field_dict["disk_usage"] = disk_usage
        if total_nodes is not UNSET:
            field_dict["total_nodes"] = total_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        total_indexed = d.pop("total_indexed", UNSET)

        disk_usage = d.pop("disk_usage", UNSET)

        total_nodes = d.pop("total_nodes", UNSET)

        embedding_index_stats = cls(
            error=error,
            total_indexed=total_indexed,
            disk_usage=disk_usage,
            total_nodes=total_nodes,
        )

        embedding_index_stats.additional_properties = d
        return embedding_index_stats

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
