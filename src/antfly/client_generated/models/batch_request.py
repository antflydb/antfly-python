from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_request_inserts import BatchRequestInserts


T = TypeVar("T", bound="BatchRequest")


@_attrs_define
class BatchRequest:
    """
    Example:
        {'inserts': {'user:123': {'name': 'John Doe', 'email': 'john@example.com', 'age': 30, 'tags': ['customer',
            'premium']}, 'user:456': {'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25, 'tags': ['customer']}},
            'deletes': ['user:789', 'user:old_account']}

    Attributes:
        inserts (Union[Unset, BatchRequestInserts]):
        deletes (Union[Unset, list[str]]): List of keys to delete.
    """

    inserts: Union[Unset, "BatchRequestInserts"] = UNSET
    deletes: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inserts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inserts, Unset):
            inserts = self.inserts.to_dict()

        deletes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.deletes, Unset):
            deletes = self.deletes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inserts is not UNSET:
            field_dict["inserts"] = inserts
        if deletes is not UNSET:
            field_dict["deletes"] = deletes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_request_inserts import BatchRequestInserts

        d = dict(src_dict)
        _inserts = d.pop("inserts", UNSET)
        inserts: Union[Unset, BatchRequestInserts]
        if isinstance(_inserts, Unset):
            inserts = UNSET
        else:
            inserts = BatchRequestInserts.from_dict(_inserts)

        deletes = cast(list[str], d.pop("deletes", UNSET))

        batch_request = cls(
            inserts=inserts,
            deletes=deletes,
        )

        batch_request.additional_properties = d
        return batch_request

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
