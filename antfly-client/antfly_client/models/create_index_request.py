from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedder_config import EmbedderConfig
    from ..models.summarizer_config import SummarizerConfig


T = TypeVar("T", bound="CreateIndexRequest")


@_attrs_define
class CreateIndexRequest:
    """
    Attributes:
        dimension (int):
        embedder_config (EmbedderConfig):
        field (Union[Unset, str]):
        template (Union[Unset, str]):
        mem_only (Union[Unset, bool]):
        summarizer_config (Union[Unset, SummarizerConfig]):
    """

    dimension: int
    embedder_config: "EmbedderConfig"
    field: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    mem_only: Union[Unset, bool] = UNSET
    summarizer_config: Union[Unset, "SummarizerConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        embedder_config = self.embedder_config.to_dict()

        field = self.field

        template = self.template

        mem_only = self.mem_only

        summarizer_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summarizer_config, Unset):
            summarizer_config = self.summarizer_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dimension": dimension,
                "embedder_config": embedder_config,
            }
        )
        if field is not UNSET:
            field_dict["field"] = field
        if template is not UNSET:
            field_dict["template"] = template
        if mem_only is not UNSET:
            field_dict["mem_only"] = mem_only
        if summarizer_config is not UNSET:
            field_dict["summarizer_config"] = summarizer_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedder_config import EmbedderConfig
        from ..models.summarizer_config import SummarizerConfig

        d = dict(src_dict)
        dimension = d.pop("dimension")

        embedder_config = EmbedderConfig.from_dict(d.pop("embedder_config"))

        field = d.pop("field", UNSET)

        template = d.pop("template", UNSET)

        mem_only = d.pop("mem_only", UNSET)

        _summarizer_config = d.pop("summarizer_config", UNSET)
        summarizer_config: Union[Unset, SummarizerConfig]
        if isinstance(_summarizer_config, Unset):
            summarizer_config = UNSET
        else:
            summarizer_config = SummarizerConfig.from_dict(_summarizer_config)

        create_index_request = cls(
            dimension=dimension,
            embedder_config=embedder_config,
            field=field,
            template=template,
            mem_only=mem_only,
            summarizer_config=summarizer_config,
        )

        create_index_request.additional_properties = d
        return create_index_request

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
