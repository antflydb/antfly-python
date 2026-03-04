from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.replication_source_type import ReplicationSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.replication_transform_op import ReplicationTransformOp


T = TypeVar("T", bound="ReplicationSource")


@_attrs_define
class ReplicationSource:
    """
    Attributes:
        type_ (ReplicationSourceType): Type of the replication source. Currently only "postgres" is supported.
             Example: postgres.
        dsn (str): Data source name (connection string) for the PostgreSQL database.
            Supports `${secret:key_name}` references that resolve from the Antfly keystore
            or environment variables. Requires `wal_level=logical` on the source.
             Example: ${secret:pg_dsn}.
        postgres_table (str): Name of the table in the PostgreSQL database to replicate from.
             Example: users.
        key_template (Union[Unset, str]): Template for constructing the Antfly document key from PG columns.
            A plain string (e.g., "id") uses that column's value directly.
            Use `{{column}}` syntax for composite keys: `{{tenant_id}}:{{user_id}}`.
             Default: 'id'. Example: id.
        slot_name (Union[Unset, str]): PostgreSQL replication slot name. If omitted, auto-derived from
            the Antfly table and PG table names. Specify this when using
            pre-created slots (e.g., on Supabase or Neon).
        publication_name (Union[Unset, str]): PostgreSQL publication name. If omitted, auto-derived and created
            automatically. Specify this when using pre-created publications.
        on_update (Union[Unset, list['ReplicationTransformOp']]): Transform operations applied on INSERT/UPDATE events.
            Values can
            reference PG columns via `{{column}}` syntax. If omitted, auto-generates
            `$set` for every column (passthrough mode).
             Example: [{'op': '$set', 'path': 'email', 'value': '{{user_email}}'}, {'op': '$set', 'path': 'score', 'value':
            '{{score}}'}, {'op': '$merge', 'value': '{{metadata}}'}, {'op': '$set', 'path': 'active', 'value': True}].
        on_delete (Union[Unset, list['ReplicationTransformOp']]): Transform operations applied on DELETE events. If
            omitted, auto-derives
            `$unset` ops from `on_update`'s `$set` paths (safe for multi-source).
            Use `$delete_document` op to delete the entire Antfly document.
             Example: [{'op': '$set', 'path': 'active', 'value': False}].
    """

    type_: ReplicationSourceType
    dsn: str
    postgres_table: str
    key_template: Union[Unset, str] = "id"
    slot_name: Union[Unset, str] = UNSET
    publication_name: Union[Unset, str] = UNSET
    on_update: Union[Unset, list["ReplicationTransformOp"]] = UNSET
    on_delete: Union[Unset, list["ReplicationTransformOp"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        dsn = self.dsn

        postgres_table = self.postgres_table

        key_template = self.key_template

        slot_name = self.slot_name

        publication_name = self.publication_name

        on_update: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.on_update, Unset):
            on_update = []
            for on_update_item_data in self.on_update:
                on_update_item = on_update_item_data.to_dict()
                on_update.append(on_update_item)

        on_delete: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.on_delete, Unset):
            on_delete = []
            for on_delete_item_data in self.on_delete:
                on_delete_item = on_delete_item_data.to_dict()
                on_delete.append(on_delete_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "dsn": dsn,
                "postgres_table": postgres_table,
            }
        )
        if key_template is not UNSET:
            field_dict["key_template"] = key_template
        if slot_name is not UNSET:
            field_dict["slot_name"] = slot_name
        if publication_name is not UNSET:
            field_dict["publication_name"] = publication_name
        if on_update is not UNSET:
            field_dict["on_update"] = on_update
        if on_delete is not UNSET:
            field_dict["on_delete"] = on_delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replication_transform_op import ReplicationTransformOp

        d = dict(src_dict)
        type_ = ReplicationSourceType(d.pop("type"))

        dsn = d.pop("dsn")

        postgres_table = d.pop("postgres_table")

        key_template = d.pop("key_template", UNSET)

        slot_name = d.pop("slot_name", UNSET)

        publication_name = d.pop("publication_name", UNSET)

        on_update = []
        _on_update = d.pop("on_update", UNSET)
        for on_update_item_data in _on_update or []:
            on_update_item = ReplicationTransformOp.from_dict(on_update_item_data)

            on_update.append(on_update_item)

        on_delete = []
        _on_delete = d.pop("on_delete", UNSET)
        for on_delete_item_data in _on_delete or []:
            on_delete_item = ReplicationTransformOp.from_dict(on_delete_item_data)

            on_delete.append(on_delete_item)

        replication_source = cls(
            type_=type_,
            dsn=dsn,
            postgres_table=postgres_table,
            key_template=key_template,
            slot_name=slot_name,
            publication_name=publication_name,
            on_update=on_update,
            on_delete=on_delete,
        )

        replication_source.additional_properties = d
        return replication_source

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
