from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_config import ModelConfig
    from ..models.query_request import QueryRequest


T = TypeVar("T", bound="RAGRequest")


@_attrs_define
class RAGRequest:
    """
    Attributes:
        query (QueryRequest):
        summarizer (ModelConfig): A unified configuration for an embedding provider. Example: {'provider': 'openai',
            'model': 'text-embedding-004'}.
        system_prompt (Union[Unset, str]): Optional system prompt to guide the summarization Example: You are a helpful
            AI assistant. Summarize the following search results concisely..
        with_citations (Union[Unset, bool]): Enable citations in the summary output
        document_renderer (Union[Unset, str]): Optional Go template string for rendering document content to the prompt
            Example: {{.title}}: {{.body}}.
    """

    query: "QueryRequest"
    summarizer: "ModelConfig"
    system_prompt: Union[Unset, str] = UNSET
    with_citations: Union[Unset, bool] = UNSET
    document_renderer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query.to_dict()

        summarizer = self.summarizer.to_dict()

        system_prompt = self.system_prompt

        with_citations = self.with_citations

        document_renderer = self.document_renderer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "summarizer": summarizer,
            }
        )
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if with_citations is not UNSET:
            field_dict["with_citations"] = with_citations
        if document_renderer is not UNSET:
            field_dict["document_renderer"] = document_renderer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_config import ModelConfig
        from ..models.query_request import QueryRequest

        d = dict(src_dict)
        query = QueryRequest.from_dict(d.pop("query"))

        summarizer = ModelConfig.from_dict(d.pop("summarizer"))

        system_prompt = d.pop("system_prompt", UNSET)

        with_citations = d.pop("with_citations", UNSET)

        document_renderer = d.pop("document_renderer", UNSET)

        rag_request = cls(
            query=query,
            summarizer=summarizer,
            system_prompt=system_prompt,
            with_citations=with_citations,
            document_renderer=document_renderer,
        )

        rag_request.additional_properties = d
        return rag_request

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
