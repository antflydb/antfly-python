from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleConfig")


@_attrs_define
class GoogleConfig:
    """Configuration for the Google embedding provider.

    Attributes:
        model (str): The name of the embedding model to use (e.g., 'text-embedding-004'). Default: 'text-embedding-004'.
        project_id (Union[Unset, str]): The Google Cloud project ID.
        location (Union[Unset, str]): The Google Cloud location (e.g., 'us-central1').
        dimension (Union[Unset, int]): The dimension of the embedding. Default: 1024.
        api_key (Union[Unset, str]): The Google API key.
        url (Union[Unset, str]): The URL of the Google API endpoint.
    """

    model: str = "text-embedding-004"
    project_id: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    dimension: Union[Unset, int] = 1024
    api_key: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        project_id = self.project_id

        location = self.location

        dimension = self.dimension

        api_key = self.api_key

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if location is not UNSET:
            field_dict["location"] = location
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        project_id = d.pop("project_id", UNSET)

        location = d.pop("location", UNSET)

        dimension = d.pop("dimension", UNSET)

        api_key = d.pop("api_key", UNSET)

        url = d.pop("url", UNSET)

        google_config = cls(
            model=model,
            project_id=project_id,
            location=location,
            dimension=dimension,
            api_key=api_key,
            url=url,
        )

        google_config.additional_properties = d
        return google_config

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
