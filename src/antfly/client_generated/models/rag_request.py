from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generator_config import GeneratorConfig
    from ..models.query_request import QueryRequest


T = TypeVar("T", bound="RAGRequest")


@_attrs_define
class RAGRequest:
    """
    Attributes:
        queries (list['QueryRequest']): Array of retrieval queries to execute. Each query must specify a table and can
            specify its own limit and document_renderer.
            Results from all queries are concatenated together (respecting each query's limit).
            For single table: [{"table": "papers", "semantic_search": "...", "limit": 10}]
            For broadcast: [{"table": "images", "limit": 5, ...}, {"table": "products", "limit": 5, ...}]
            For mixed: [{"table": "papers", "semantic_search": "...", "limit": 10}, {"table": "books", "full_text_search":
            {...}, "limit": 5}]
        summarizer (GeneratorConfig): A unified configuration for a generative AI provider. Example: {'provider':
            'openai', 'model': 'gpt-4o', 'temperature': 0.7, 'max_tokens': 2048}.
        system_prompt (Union[Unset, str]): Optional system prompt to guide the summarization Example: You are a helpful
            AI assistant. Summarize the following search results concisely..
        prompt (Union[Unset, str]): Optional custom user prompt template for the LLM. If not provided, a default prompt
            is used.
            The prompt can reference the following variables:
            - {{documents}}: Array of retrieved documents with id and fields
            - {{semantic_search}}: The user's semantic search query (if provided)
            You can use Handlebars template syntax to customize the prompt, including loops and conditionals.
            To generate a comma-separated list of document IDs, use: {{#each documents}}{{this.id}}{{#unless @last}},
            {{/unless}}{{/each}}
             Example: Based on these documents, provide a detailed analysis:

            {{#each documents}}
            Doc {{this.id}}: {{this.fields}}
            {{/each}}

            Valid IDs: {{#each documents}}{{this.id}}{{#unless @last}}, {{/unless}}{{/each}}.
        with_streaming (Union[Unset, bool]): Enable SSE streaming of results instead of JSON response
    """

    queries: list["QueryRequest"]
    summarizer: "GeneratorConfig"
    system_prompt: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    with_streaming: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        summarizer = self.summarizer.to_dict()

        system_prompt = self.system_prompt

        prompt = self.prompt

        with_streaming = self.with_streaming

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queries": queries,
                "summarizer": summarizer,
            }
        )
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if with_streaming is not UNSET:
            field_dict["with_streaming"] = with_streaming

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generator_config import GeneratorConfig
        from ..models.query_request import QueryRequest

        d = dict(src_dict)
        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = QueryRequest.from_dict(queries_item_data)

            queries.append(queries_item)

        summarizer = GeneratorConfig.from_dict(d.pop("summarizer"))

        system_prompt = d.pop("system_prompt", UNSET)

        prompt = d.pop("prompt", UNSET)

        with_streaming = d.pop("with_streaming", UNSET)

        rag_request = cls(
            queries=queries,
            summarizer=summarizer,
            system_prompt=system_prompt,
            prompt=prompt,
            with_streaming=with_streaming,
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
