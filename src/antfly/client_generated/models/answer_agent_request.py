from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generator_config import GeneratorConfig


T = TypeVar("T", bound="AnswerAgentRequest")


@_attrs_define
class AnswerAgentRequest:
    """
    Attributes:
        query (str): User's natural language query Example: What are the best gaming laptops under $2000?.
        summarizer (GeneratorConfig): A unified configuration for a generative AI provider. Example: {'provider':
            'openai', 'model': 'gpt-4o', 'temperature': 0.7, 'max_tokens': 2048}.
        tables (Union[Unset, list[str]]): Optional list of tables to search. If empty, searches all tables. Example:
            ['products', 'reviews'].
        indexes (Union[Unset, list[str]]): Optional list of indexes to use for each table. If empty, uses all available
            indexes. Example: ['embedding_idx', 'search_idx'].
        system_prompt (Union[Unset, str]): Optional system prompt to guide classification and answer generation Example:
            You are a helpful shopping assistant..
        with_streaming (Union[Unset, bool]): Enable SSE streaming of results (classification, keywords, queries,
            results, answer) instead of JSON response Default: True.
    """

    query: str
    summarizer: "GeneratorConfig"
    tables: Union[Unset, list[str]] = UNSET
    indexes: Union[Unset, list[str]] = UNSET
    system_prompt: Union[Unset, str] = UNSET
    with_streaming: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        summarizer = self.summarizer.to_dict()

        tables: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tables, Unset):
            tables = self.tables

        indexes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.indexes, Unset):
            indexes = self.indexes

        system_prompt = self.system_prompt

        with_streaming = self.with_streaming

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "summarizer": summarizer,
            }
        )
        if tables is not UNSET:
            field_dict["tables"] = tables
        if indexes is not UNSET:
            field_dict["indexes"] = indexes
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if with_streaming is not UNSET:
            field_dict["with_streaming"] = with_streaming

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generator_config import GeneratorConfig

        d = dict(src_dict)
        query = d.pop("query")

        summarizer = GeneratorConfig.from_dict(d.pop("summarizer"))

        tables = cast(list[str], d.pop("tables", UNSET))

        indexes = cast(list[str], d.pop("indexes", UNSET))

        system_prompt = d.pop("system_prompt", UNSET)

        with_streaming = d.pop("with_streaming", UNSET)

        answer_agent_request = cls(
            query=query,
            summarizer=summarizer,
            tables=tables,
            indexes=indexes,
            system_prompt=system_prompt,
            with_streaming=with_streaming,
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
