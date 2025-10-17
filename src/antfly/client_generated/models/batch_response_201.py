from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_response_201_failed_item import BatchResponse201FailedItem


T = TypeVar("T", bound="BatchResponse201")


@_attrs_define
class BatchResponse201:
    """
    Attributes:
        inserted (Union[Unset, int]): Number of documents successfully inserted
        deleted (Union[Unset, int]): Number of documents successfully deleted
        failed (Union[Unset, list['BatchResponse201FailedItem']]): List of failed operations with error details
    """

    inserted: Union[Unset, int] = UNSET
    deleted: Union[Unset, int] = UNSET
    failed: Union[Unset, list["BatchResponse201FailedItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inserted = self.inserted

        deleted = self.deleted

        failed: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.failed, Unset):
            failed = []
            for failed_item_data in self.failed:
                failed_item = failed_item_data.to_dict()
                failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inserted is not UNSET:
            field_dict["inserted"] = inserted
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_response_201_failed_item import BatchResponse201FailedItem

        d = dict(src_dict)
        inserted = d.pop("inserted", UNSET)

        deleted = d.pop("deleted", UNSET)

        failed = []
        _failed = d.pop("failed", UNSET)
        for failed_item_data in _failed or []:
            failed_item = BatchResponse201FailedItem.from_dict(failed_item_data)

            failed.append(failed_item)

        batch_response_201 = cls(
            inserted=inserted,
            deleted=deleted,
            failed=failed,
        )

        batch_response_201.additional_properties = d
        return batch_response_201

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
