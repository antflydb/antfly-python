from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateRangeResult")


@_attrs_define
class DateRangeResult:
    """
    Attributes:
        name (str):
        count (int):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
    """

    name: str
    count: int
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        count = self.count

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "count": count,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        count = d.pop("count")

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        date_range_result = cls(
            name=name,
            count=count,
            from_=from_,
            to=to,
        )

        date_range_result.additional_properties = d
        return date_range_result

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
