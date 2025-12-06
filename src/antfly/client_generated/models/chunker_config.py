from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chunker_provider import ChunkerProvider

T = TypeVar("T", bound="ChunkerConfig")


@_attrs_define
class ChunkerConfig:
    """A unified configuration for a chunking provider.

    Example:
        {'provider': 'termite', 'model': 'fixed', 'target_tokens': 500, 'overlap_tokens': 50}

    Attributes:
        provider (ChunkerProvider): The chunking provider to use.
    """

    provider: ChunkerProvider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = ChunkerProvider(d.pop("provider"))

        chunker_config = cls(
            provider=provider,
        )

        chunker_config.additional_properties = d
        return chunker_config

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
