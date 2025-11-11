from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_table_request_indexes import CreateTableRequestIndexes
    from ..models.table_schema import TableSchema


T = TypeVar("T", bound="CreateTableRequest")


@_attrs_define
class CreateTableRequest:
    """
    Attributes:
        num_shards (Union[Unset, int]): Number of shards to create for the table. Data is partitioned across shards
            based on key ranges.

            Guidelines:
            - Small datasets (<100K docs): 1-3 shards
            - Medium datasets (100K-1M docs): 3-10 shards
            - Large datasets (>1M docs): 10+ shards

            More shards enable better parallelism but increase overhead. Choose based on expected data size and query
            patterns.
             Example: 3.
        description (Union[Unset, str]): Optional human-readable description of the table and its purpose.
            Useful for documentation and team collaboration.
             Example: User profiles with embeddings for semantic search.
        indexes (Union[Unset, CreateTableRequestIndexes]): Map of index name to index configuration. Indexes enable
            different query capabilities:
            - Full-text indexes for BM25 search
            - Vector indexes for semantic similarity
            - Multimodal indexes for images/audio/video

            You can add multiple indexes to support different query patterns.
             Example: {'search_index': {'type': 'full_text_v0'}, 'embedding_index': {'type': 'aknn_v0', 'dimension': 384,
            'embedder': {'provider': 'ollama', 'model': 'all-minilm'}}}.
        schema (Union[Unset, TableSchema]): Schema definition for a table with multiple document types
    """

    num_shards: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    indexes: Union[Unset, "CreateTableRequestIndexes"] = UNSET
    schema: Union[Unset, "TableSchema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_shards = self.num_shards

        description = self.description

        indexes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.indexes, Unset):
            indexes = self.indexes.to_dict()

        schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_shards is not UNSET:
            field_dict["num_shards"] = num_shards
        if description is not UNSET:
            field_dict["description"] = description
        if indexes is not UNSET:
            field_dict["indexes"] = indexes
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_table_request_indexes import CreateTableRequestIndexes
        from ..models.table_schema import TableSchema

        d = dict(src_dict)
        num_shards = d.pop("num_shards", UNSET)

        description = d.pop("description", UNSET)

        _indexes = d.pop("indexes", UNSET)
        indexes: Union[Unset, CreateTableRequestIndexes]
        if isinstance(_indexes, Unset):
            indexes = UNSET
        else:
            indexes = CreateTableRequestIndexes.from_dict(_indexes)

        _schema = d.pop("schema", UNSET)
        schema: Union[Unset, TableSchema]
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = TableSchema.from_dict(_schema)

        create_table_request = cls(
            num_shards=num_shards,
            description=description,
            indexes=indexes,
            schema=schema,
        )

        create_table_request.additional_properties = d
        return create_table_request

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
