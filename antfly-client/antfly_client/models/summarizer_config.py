from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummarizerConfig")


@_attrs_define
class SummarizerConfig:
    """
    Attributes:
        provider (str):
        model (str):
        model_provider (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    provider: str
    model: str
    model_provider: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        model = self.model

        model_provider = self.model_provider

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "model": model,
            }
        )
        if model_provider is not UNSET:
            field_dict["model_provider"] = model_provider
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider")

        model = d.pop("model")

        model_provider = d.pop("model_provider", UNSET)

        url = d.pop("url", UNSET)

        summarizer_config = cls(
            provider=provider,
            model=model,
            model_provider=model_provider,
            url=url,
        )

        summarizer_config.additional_properties = d
        return summarizer_config

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
