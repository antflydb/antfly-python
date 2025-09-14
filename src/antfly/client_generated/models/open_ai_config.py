from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenAIConfig")


@_attrs_define
class OpenAIConfig:
    """Configuration for the OpenAI embedding provider.

    Attributes:
        model (str): The name of the OpenAI model to use.
        url (Union[Unset, str]): The URL of the OpenAI API endpoint.
        api_key (Union[Unset, str]): The OpenAI API key.
    """

    model: str
    url: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        url = self.url

        api_key = self.api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if api_key is not UNSET:
            field_dict["api_key"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        url = d.pop("url", UNSET)

        api_key = d.pop("api_key", UNSET)

        open_ai_config = cls(
            model=model,
            url=url,
            api_key=api_key,
        )

        open_ai_config.additional_properties = d
        return open_ai_config

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
