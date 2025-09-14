from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_config import ModelConfig


T = TypeVar("T", bound="EmbeddingIndexConfig")


@_attrs_define
class EmbeddingIndexConfig:
    """
    Attributes:
        dimension (int): Vector dimension
        field (Union[Unset, str]): Field to extract embeddings from
        template (Union[Unset, str]): Go string template for generating prompts. See https://pkg.go.dev/text/template
            for more information. Example: Hello, {{if eq .Name "John"}}Johnathan{{else}}{{.Name}}{{end}}! You are {{.Age}}
            years old..
        mem_only (Union[Unset, bool]): Whether to use in-memory only storage
        embedder_config (Union[Unset, ModelConfig]): A unified configuration for an embedding provider. Example:
            {'provider': 'openai', 'model': 'text-embedding-004'}.
        summarizer_config (Union[Unset, ModelConfig]): A unified configuration for an embedding provider. Example:
            {'provider': 'openai', 'model': 'text-embedding-004'}.
    """

    dimension: int
    field: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    mem_only: Union[Unset, bool] = UNSET
    embedder_config: Union[Unset, "ModelConfig"] = UNSET
    summarizer_config: Union[Unset, "ModelConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        field = self.field

        template = self.template

        mem_only = self.mem_only

        embedder_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.embedder_config, Unset):
            embedder_config = self.embedder_config.to_dict()

        summarizer_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summarizer_config, Unset):
            summarizer_config = self.summarizer_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dimension": dimension,
            }
        )
        if field is not UNSET:
            field_dict["field"] = field
        if template is not UNSET:
            field_dict["template"] = template
        if mem_only is not UNSET:
            field_dict["mem_only"] = mem_only
        if embedder_config is not UNSET:
            field_dict["embedder_config"] = embedder_config
        if summarizer_config is not UNSET:
            field_dict["summarizer_config"] = summarizer_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_config import ModelConfig

        d = dict(src_dict)
        dimension = d.pop("dimension")

        field = d.pop("field", UNSET)

        template = d.pop("template", UNSET)

        mem_only = d.pop("mem_only", UNSET)

        _embedder_config = d.pop("embedder_config", UNSET)
        embedder_config: Union[Unset, ModelConfig]
        if isinstance(_embedder_config, Unset):
            embedder_config = UNSET
        else:
            embedder_config = ModelConfig.from_dict(_embedder_config)

        _summarizer_config = d.pop("summarizer_config", UNSET)
        summarizer_config: Union[Unset, ModelConfig]
        if isinstance(_summarizer_config, Unset):
            summarizer_config = UNSET
        else:
            summarizer_config = ModelConfig.from_dict(_summarizer_config)

        embedding_index_config = cls(
            dimension=dimension,
            field=field,
            template=template,
            mem_only=mem_only,
            embedder_config=embedder_config,
            summarizer_config=summarizer_config,
        )

        embedding_index_config.additional_properties = d
        return embedding_index_config

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
