from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Reranker")


@_attrs_define
class Reranker:
    """
    Attributes:
        model (str):
        provider (str):
        field (Union[Unset, str]):
        template (Union[Unset, str]):
        model_provider (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    model: str
    provider: str
    field: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    model_provider: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        provider = self.provider

        field = self.field

        template = self.template

        model_provider = self.model_provider

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "provider": provider,
            }
        )
        if field is not UNSET:
            field_dict["field"] = field
        if template is not UNSET:
            field_dict["template"] = template
        if model_provider is not UNSET:
            field_dict["model_provider"] = model_provider
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        provider = d.pop("provider")

        field = d.pop("field", UNSET)

        template = d.pop("template", UNSET)

        model_provider = d.pop("model_provider", UNSET)

        url = d.pop("url", UNSET)

        reranker = cls(
            model=model,
            provider=provider,
            field=field,
            template=template,
            model_provider=model_provider,
            url=url,
        )

        reranker.additional_properties = d
        return reranker

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
