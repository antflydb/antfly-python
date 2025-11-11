from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generator_config import GeneratorConfig
    from ..models.query_request import QueryRequest


T = TypeVar("T", bound="AnswerAgentRequest")


@_attrs_define
class AnswerAgentRequest:
    """
    Attributes:
        query (str): User's natural language query to be classified and improved Example: What are the best gaming
            laptops under $2000?.
        summarizer (GeneratorConfig): A unified configuration for a generative AI provider. Example: {'provider':
            'openai', 'model': 'gpt-4o', 'temperature': 0.7, 'max_tokens': 2048}.
        queries (list['QueryRequest']): Array of query requests to execute. The query text will be transformed for
            semantic search
            and populated into the semantic_search field of each query. Example: [{'table': 'products', 'indexes':
            ['embedding_idx'], 'limit': 10}, {'table': 'reviews', 'indexes': ['embedding_idx'], 'limit': 5}].
        system_prompt (Union[Unset, str]): Optional system prompt to guide classification and answer generation Example:
            You are a helpful shopping assistant..
        with_streaming (Union[Unset, bool]): Enable SSE streaming of results (classification, queries, results, answer)
            instead of JSON response Default: True.
        with_reasoning (Union[Unset, bool]): Include the LLM's reasoning process as separate events before the answer
            Default: False.
        with_followup (Union[Unset, bool]): Include suggested follow-up questions as separate events after the answer
            Default: False.
    """

    query: str
    summarizer: "GeneratorConfig"
    queries: list["QueryRequest"]
    system_prompt: Union[Unset, str] = UNSET
    with_streaming: Union[Unset, bool] = True
    with_reasoning: Union[Unset, bool] = False
    with_followup: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        summarizer = self.summarizer.to_dict()

        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)

        system_prompt = self.system_prompt

        with_streaming = self.with_streaming

        with_reasoning = self.with_reasoning

        with_followup = self.with_followup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "summarizer": summarizer,
                "queries": queries,
            }
        )
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if with_streaming is not UNSET:
            field_dict["with_streaming"] = with_streaming
        if with_reasoning is not UNSET:
            field_dict["with_reasoning"] = with_reasoning
        if with_followup is not UNSET:
            field_dict["with_followup"] = with_followup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generator_config import GeneratorConfig
        from ..models.query_request import QueryRequest

        d = dict(src_dict)
        query = d.pop("query")

        summarizer = GeneratorConfig.from_dict(d.pop("summarizer"))

        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:
            queries_item = QueryRequest.from_dict(queries_item_data)

            queries.append(queries_item)

        system_prompt = d.pop("system_prompt", UNSET)

        with_streaming = d.pop("with_streaming", UNSET)

        with_reasoning = d.pop("with_reasoning", UNSET)

        with_followup = d.pop("with_followup", UNSET)

        answer_agent_request = cls(
            query=query,
            summarizer=summarizer,
            queries=queries,
            system_prompt=system_prompt,
            with_streaming=with_streaming,
            with_reasoning=with_reasoning,
            with_followup=with_followup,
        )

        answer_agent_request.additional_properties = d
        return answer_agent_request

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
