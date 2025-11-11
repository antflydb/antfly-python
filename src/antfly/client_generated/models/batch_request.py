from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.batch_request_sync_level import BatchRequestSyncLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_request_inserts import BatchRequestInserts


T = TypeVar("T", bound="BatchRequest")


@_attrs_define
class BatchRequest:
    """Batch insert and delete operations in a single request. All operations are processed atomically within each shard.

    Benefits:
    - Reduces network overhead compared to individual requests
    - More efficient indexing (updates are batched)
    - Atomic within shard boundaries

    The inserts are upserts - existing keys are overwritten, new keys are created.

        Example:
            {'inserts': {'user:123': {'name': 'John Doe', 'email': 'john@example.com', 'age': 30, 'tags': ['customer',
                'premium']}, 'user:456': {'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25, 'tags': ['customer']}},
                'deletes': ['user:789', 'user:old_account']}

        Attributes:
            inserts (Union[Unset, BatchRequestInserts]): Map of document IDs to document objects. Each key is the unique
                identifier for the document.

                Best practices:
                - Use consistent key naming schemes (e.g., "user:123", "article:456")
                - Key length affects storage and performance - keep them reasonably short
                - Keys are sorted lexicographically, so choose prefixes that support range scans
                 Example: {'user:123': {'name': 'John Doe', 'email': 'john@example.com', 'age': 30, 'tags': ['customer',
                'premium']}, 'user:456': {'name': 'Jane Smith', 'email': 'jane@example.com', 'age': 25, 'tags': ['customer']}}.
            deletes (Union[Unset, list[str]]): Array of document IDs to delete. Documents are removed from all indexes.

                Notes:
                - Non-existent keys are silently ignored
                - Deletions are processed before inserts in the same batch
                - Keys are permanently removed from storage and indexes
                 Example: ['user:789', 'user:old_account'].
            sync_level (Union[Unset, BatchRequestSyncLevel]): Synchronization level for the batch operation:
                - "propose": Wait for Raft proposal acceptance (fastest, default)
                - "write": Wait for Pebble KV write
                - "full_text": Wait for full-text index WAL write (slowest, most durable)
                 Default: BatchRequestSyncLevel.PROPOSE.
    """

    inserts: Union[Unset, "BatchRequestInserts"] = UNSET
    deletes: Union[Unset, list[str]] = UNSET
    sync_level: Union[Unset, BatchRequestSyncLevel] = BatchRequestSyncLevel.PROPOSE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inserts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inserts, Unset):
            inserts = self.inserts.to_dict()

        deletes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.deletes, Unset):
            deletes = self.deletes

        sync_level: Union[Unset, str] = UNSET
        if not isinstance(self.sync_level, Unset):
            sync_level = self.sync_level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inserts is not UNSET:
            field_dict["inserts"] = inserts
        if deletes is not UNSET:
            field_dict["deletes"] = deletes
        if sync_level is not UNSET:
            field_dict["sync_level"] = sync_level

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

        _sync_level = d.pop("sync_level", UNSET)
        sync_level: Union[Unset, BatchRequestSyncLevel]
        if isinstance(_sync_level, Unset):
            sync_level = UNSET
        else:
            sync_level = BatchRequestSyncLevel(_sync_level)

        batch_request = cls(
            inserts=inserts,
            deletes=deletes,
            sync_level=sync_level,
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
