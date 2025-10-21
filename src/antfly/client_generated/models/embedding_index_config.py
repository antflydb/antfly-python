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
        embedder (Union[Unset, ModelConfig]): A unified configuration for an embedding provider. Example: {'provider':
            'openai', 'model': 'text-embedding-004'}.
        summarizer (Union[Unset, ModelConfig]): A unified configuration for an embedding provider. Example: {'provider':
            'openai', 'model': 'text-embedding-004'}.
    """

    dimension: int
    field: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    mem_only: Union[Unset, bool] = UNSET
    embedder: Union[Unset, "ModelConfig"] = UNSET
    summarizer: Union[Unset, "ModelConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        field = self.field

        template = self.template

        mem_only = self.mem_only

        embedder: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.embedder, Unset):
            embedder = self.embedder.to_dict()

        summarizer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summarizer, Unset):
            summarizer = self.summarizer.to_dict()

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
        if embedder is not UNSET:
            field_dict["embedder"] = embedder
        if summarizer is not UNSET:
            field_dict["summarizer"] = summarizer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_config import ModelConfig

        d = dict(src_dict)
        dimension = d.pop("dimension")

        field = d.pop("field", UNSET)

        template = d.pop("template", UNSET)

        mem_only = d.pop("mem_only", UNSET)

        _embedder = d.pop("embedder", UNSET)
        embedder: Union[Unset, ModelConfig]
        if isinstance(_embedder, Unset):
            embedder = UNSET
        else:
            embedder = ModelConfig.from_dict(_embedder)

        _summarizer = d.pop("summarizer", UNSET)
        summarizer: Union[Unset, ModelConfig]
        if isinstance(_summarizer, Unset):
            summarizer = UNSET
        else:
            summarizer = ModelConfig.from_dict(_summarizer)

        embedding_index_config = cls(
            dimension=dimension,
            field=field,
            template=template,
            mem_only=mem_only,
            embedder=embedder,
            summarizer=summarizer,
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
