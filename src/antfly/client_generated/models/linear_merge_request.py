from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linear_merge_request_records import LinearMergeRequestRecords


T = TypeVar("T", bound="LinearMergeRequest")


@_attrs_define
class LinearMergeRequest:
    """
    Attributes:
        records (LinearMergeRequestRecords): Map of document ID to document object: {"doc_id_1": {...}, "doc_id_2":
            {...}}
            Server will sort keys lexicographically before processing.
            This format avoids duplicate IDs (matches Antfly's batch write interface).
        last_merged_id (Union[Unset, str]): ID of last record from previous merge request.
            Empty string "" for first request.
            Defines lower bound of key range to process.
        dry_run (Union[Unset, bool]): If true, return what would be deleted without making changes.
            Useful for validating sync behavior before committing.
             Default: False.
    """

    records: "LinearMergeRequestRecords"
    last_merged_id: Union[Unset, str] = UNSET
    dry_run: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records = self.records.to_dict()

        last_merged_id = self.last_merged_id

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "records": records,
            }
        )
        if last_merged_id is not UNSET:
            field_dict["last_merged_id"] = last_merged_id
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linear_merge_request_records import LinearMergeRequestRecords

        d = dict(src_dict)
        records = LinearMergeRequestRecords.from_dict(d.pop("records"))

        last_merged_id = d.pop("last_merged_id", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        linear_merge_request = cls(
            records=records,
            last_merged_id=last_merged_id,
            dry_run=dry_run,
        )

        linear_merge_request.additional_properties = d
        return linear_merge_request

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
