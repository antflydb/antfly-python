from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bleve_index_v2_stats import BleveIndexV2Stats
    from ..models.embedding_index_stats import EmbeddingIndexStats
    from ..models.graph_index_v0_stats import GraphIndexV0Stats


T = TypeVar("T", bound="IndexStatusShardStatus")


@_attrs_define
class IndexStatusShardStatus:
    """ """

    additional_properties: dict[str, Union["BleveIndexV2Stats", "EmbeddingIndexStats", "GraphIndexV0Stats"]] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.bleve_index_v2_stats import BleveIndexV2Stats
        from ..models.embedding_index_stats import EmbeddingIndexStats

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, BleveIndexV2Stats):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, EmbeddingIndexStats):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bleve_index_v2_stats import BleveIndexV2Stats
        from ..models.embedding_index_stats import EmbeddingIndexStats
        from ..models.graph_index_v0_stats import GraphIndexV0Stats

        d = dict(src_dict)
        index_status_shard_status = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union["BleveIndexV2Stats", "EmbeddingIndexStats", "GraphIndexV0Stats"]:
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

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        index_status_shard_status.additional_properties = additional_properties
        return index_status_shard_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union["BleveIndexV2Stats", "EmbeddingIndexStats", "GraphIndexV0Stats"]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: Union["BleveIndexV2Stats", "EmbeddingIndexStats", "GraphIndexV0Stats"]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
