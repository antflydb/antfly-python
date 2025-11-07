from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_result import QueryResult
    from ..models.summarize_result import SummarizeResult


T = TypeVar("T", bound="RAGResult")


@_attrs_define
class RAGResult:
    """RAG result with individual query results and summary

    Attributes:
        query_results (Union[Unset, list['QueryResult']]): Results from each query. Check each result's status and error
            fields for failures.
        summary_result (Union[Unset, SummarizeResult]): Result of a summarization operation. The summary is formatted as
            markdown with inline document references using [doc_id <id>] or [doc_id <id1>, <id2>] format.
    """

    query_results: Union[Unset, list["QueryResult"]] = UNSET
    summary_result: Union[Unset, "SummarizeResult"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.query_results, Unset):
            query_results = []
            for query_results_item_data in self.query_results:
                query_results_item = query_results_item_data.to_dict()
                query_results.append(query_results_item)

        summary_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summary_result, Unset):
            summary_result = self.summary_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_results is not UNSET:
            field_dict["query_results"] = query_results
        if summary_result is not UNSET:
            field_dict["summary_result"] = summary_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_result import QueryResult
        from ..models.summarize_result import SummarizeResult

        d = dict(src_dict)
        query_results = []
        _query_results = d.pop("query_results", UNSET)
        for query_results_item_data in _query_results or []:
            query_results_item = QueryResult.from_dict(query_results_item_data)

            query_results.append(query_results_item)

        _summary_result = d.pop("summary_result", UNSET)
        summary_result: Union[Unset, SummarizeResult]
        if isinstance(_summary_result, Unset):
            summary_result = UNSET
        else:
            summary_result = SummarizeResult.from_dict(_summary_result)

        rag_result = cls(
            query_results=query_results,
            summary_result=summary_result,
        )

        rag_result.additional_properties = d
        return rag_result

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
