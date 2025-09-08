from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.index_config_config import IndexConfigConfig
    from ..models.index_status_shard_status import IndexStatusShardStatus
    from ..models.index_status_status import IndexStatusStatus


T = TypeVar("T", bound="IndexStatus")


@_attrs_define
class IndexStatus:
    """
    Attributes:
        name (str):
        type_ (str):
        config (IndexConfigConfig):
        shard_status (IndexStatusShardStatus):
        status (IndexStatusStatus):
    """

    name: str
    type_: str
    config: "IndexConfigConfig"
    shard_status: "IndexStatusShardStatus"
    status: "IndexStatusStatus"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        config = self.config.to_dict()

        shard_status = self.shard_status.to_dict()

        status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "config": config,
                "shard_status": shard_status,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.index_config_config import IndexConfigConfig
        from ..models.index_status_shard_status import IndexStatusShardStatus
        from ..models.index_status_status import IndexStatusStatus

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        config = IndexConfigConfig.from_dict(d.pop("config"))

        shard_status = IndexStatusShardStatus.from_dict(d.pop("shard_status"))

        status = IndexStatusStatus.from_dict(d.pop("status"))

        index_status = cls(
            name=name,
            type_=type_,
            config=config,
            shard_status=shard_status,
            status=status,
        )

        index_status.additional_properties = d
        return index_status

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
