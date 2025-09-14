from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_status import StorageStatus
    from ..models.table_indexes import TableIndexes
    from ..models.table_schema import TableSchema
    from ..models.table_shards import TableShards


T = TypeVar("T", bound="TableStatus")


@_attrs_define
class TableStatus:
    """
    Attributes:
        name (str):
        indexes (TableIndexes):
        shards (TableShards):
        storage_status (StorageStatus):
        schema (Union[Unset, TableSchema]):
    """

    name: str
    indexes: "TableIndexes"
    shards: "TableShards"
    storage_status: "StorageStatus"
    schema: Union[Unset, "TableSchema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        indexes = self.indexes.to_dict()

        shards = self.shards.to_dict()

        storage_status = self.storage_status.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "indexes": indexes,
                "shards": shards,
                "storage_status": storage_status,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_status import StorageStatus
        from ..models.table_indexes import TableIndexes
        from ..models.table_schema import TableSchema
        from ..models.table_shards import TableShards

        d = dict(src_dict)
        name = d.pop("name")

        indexes = TableIndexes.from_dict(d.pop("indexes"))

        shards = TableShards.from_dict(d.pop("shards"))

        storage_status = StorageStatus.from_dict(d.pop("storage_status"))

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, TableSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = TableSchema.from_dict(_schema)

        table_status = cls(
            name=name,
            indexes=indexes,
            shards=shards,
            storage_status=storage_status,
            schema=schema,
        )

        table_status.additional_properties = d
        return table_status

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
