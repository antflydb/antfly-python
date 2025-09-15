from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bleve_index_v2_config import BleveIndexV2Config
    from ..models.embedding_index_config import EmbeddingIndexConfig


T = TypeVar("T", bound="TableIndexes")


@_attrs_define
class TableIndexes:
    """ """

    additional_properties: dict[str, Union["BleveIndexV2Config", "EmbeddingIndexConfig"]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.bleve_index_v2_config import BleveIndexV2Config

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, BleveIndexV2Config):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bleve_index_v2_config import BleveIndexV2Config
        from ..models.embedding_index_config import EmbeddingIndexConfig

        d = dict(src_dict)
        table_indexes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union["BleveIndexV2Config", "EmbeddingIndexConfig"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_index_config_type_0 = BleveIndexV2Config.from_dict(data)

                    return componentsschemas_index_config_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_index_config_type_1 = EmbeddingIndexConfig.from_dict(data)

                return componentsschemas_index_config_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        table_indexes.additional_properties = additional_properties
        return table_indexes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union["BleveIndexV2Config", "EmbeddingIndexConfig"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union["BleveIndexV2Config", "EmbeddingIndexConfig"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
