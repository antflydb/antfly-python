from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider import Provider
from ..types import UNSET, Unset

T = TypeVar("T", bound="RerankerConfig")


@_attrs_define
class RerankerConfig:
    """A unified configuration for an embedding provider.

    Example:
        {'provider': 'openai', 'model': 'text-embedding-004', 'field': 'content'}

    Attributes:
        provider (Provider): The embedding provider to use.
        field (Union[Unset, str]):
        template (Union[Unset, str]):
    """

    provider: Provider
    field: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        field = self.field

        template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if field is not UNSET:
            field_dict["field"] = field
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = Provider(d.pop("provider"))

        field = d.pop("field", UNSET)

        template = d.pop("template", UNSET)

        reranker_config = cls(
            provider=provider,
            field=field,
            template=template,
        )

        reranker_config.additional_properties = d
        return reranker_config

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
