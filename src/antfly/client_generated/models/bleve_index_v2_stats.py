from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BleveIndexV2Stats")


@_attrs_define
class BleveIndexV2Stats:
    """
    Attributes:
        error (Union[Unset, str]): Error message if stats could not be retrieved
        total_indexed (Union[Unset, int]): Number of documents in the index
        disk_usage (Union[Unset, int]): Size of the index in bytes
        rebuilding (Union[Unset, bool]): Whether the index is currently rebuilding
    """

    error: Union[Unset, str] = UNSET
    total_indexed: Union[Unset, int] = UNSET
    disk_usage: Union[Unset, int] = UNSET
    rebuilding: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        total_indexed = self.total_indexed

        disk_usage = self.disk_usage

        rebuilding = self.rebuilding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if total_indexed is not UNSET:
            field_dict["total_indexed"] = total_indexed
        if disk_usage is not UNSET:
            field_dict["disk_usage"] = disk_usage
        if rebuilding is not UNSET:
            field_dict["rebuilding"] = rebuilding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        total_indexed = d.pop("total_indexed", UNSET)

        disk_usage = d.pop("disk_usage", UNSET)

        rebuilding = d.pop("rebuilding", UNSET)

        bleve_index_v2_stats = cls(
            error=error,
            total_indexed=total_indexed,
            disk_usage=disk_usage,
            rebuilding=rebuilding,
        )

        bleve_index_v2_stats.additional_properties = d
        return bleve_index_v2_stats

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
