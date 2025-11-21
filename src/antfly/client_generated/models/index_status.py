from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bleve_index_v2_config import BleveIndexV2Config
    from ..models.bleve_index_v2_stats import BleveIndexV2Stats
    from ..models.embedding_index_config import EmbeddingIndexConfig
    from ..models.embedding_index_stats import EmbeddingIndexStats
    from ..models.graph_index_v0_config import GraphIndexV0Config
    from ..models.graph_index_v0_stats import GraphIndexV0Stats
    from ..models.index_status_shard_status import IndexStatusShardStatus


T = TypeVar("T", bound="IndexStatus")


@_attrs_define
class IndexStatus:
    """
    Attributes:
        shard_status (IndexStatusShardStatus):
        config (Union['BleveIndexV2Config', 'EmbeddingIndexConfig', 'GraphIndexV0Config']): Configuration for an index
        status (Union['BleveIndexV2Stats', 'EmbeddingIndexStats', 'GraphIndexV0Stats']): Statistics for an index
    """

    shard_status: "IndexStatusShardStatus"
    config: Union["BleveIndexV2Config", "EmbeddingIndexConfig", "GraphIndexV0Config"]
    status: Union["BleveIndexV2Stats", "EmbeddingIndexStats", "GraphIndexV0Stats"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bleve_index_v2_config import BleveIndexV2Config
        from ..models.bleve_index_v2_stats import BleveIndexV2Stats
        from ..models.embedding_index_config import EmbeddingIndexConfig
        from ..models.embedding_index_stats import EmbeddingIndexStats

        shard_status = self.shard_status.to_dict()

        config: dict[str, Any]
        if isinstance(self.config, BleveIndexV2Config):
            config = self.config.to_dict()
        elif isinstance(self.config, EmbeddingIndexConfig):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        status: dict[str, Any]
        if isinstance(self.status, BleveIndexV2Stats):
            status = self.status.to_dict()
        elif isinstance(self.status, EmbeddingIndexStats):
            status = self.status.to_dict()
        else:
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shard_status": shard_status,
                "config": config,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bleve_index_v2_config import BleveIndexV2Config
        from ..models.bleve_index_v2_stats import BleveIndexV2Stats
        from ..models.embedding_index_config import EmbeddingIndexConfig
        from ..models.embedding_index_stats import EmbeddingIndexStats
        from ..models.graph_index_v0_config import GraphIndexV0Config
        from ..models.graph_index_v0_stats import GraphIndexV0Stats
        from ..models.index_status_shard_status import IndexStatusShardStatus

        d = dict(src_dict)
        shard_status = IndexStatusShardStatus.from_dict(d.pop("shard_status"))

        def _parse_config(data: object) -> Union["BleveIndexV2Config", "EmbeddingIndexConfig", "GraphIndexV0Config"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_index_config_type_0 = BleveIndexV2Config.from_dict(data)

                return componentsschemas_index_config_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_index_config_type_1 = EmbeddingIndexConfig.from_dict(data)

                return componentsschemas_index_config_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_index_config_type_2 = GraphIndexV0Config.from_dict(data)

            return componentsschemas_index_config_type_2

        config = _parse_config(d.pop("config"))

        def _parse_status(data: object) -> Union["BleveIndexV2Stats", "EmbeddingIndexStats", "GraphIndexV0Stats"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_index_stats_type_0 = BleveIndexV2Stats.from_dict(data)

                return componentsschemas_index_stats_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_index_stats_type_1 = EmbeddingIndexStats.from_dict(data)

                return componentsschemas_index_stats_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_index_stats_type_2 = GraphIndexV0Stats.from_dict(data)

            return componentsschemas_index_stats_type_2

        status = _parse_status(d.pop("status"))

        index_status = cls(
            shard_status=shard_status,
            config=config,
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
