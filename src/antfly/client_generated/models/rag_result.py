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
    """RAG result combining query results with summary and citations

    Attributes:
        query_result (Union[Unset, QueryResult]): Result of a query operation as an array of results and a count.
        summary_result (Union[Unset, SummarizeResult]): Result of a summarization operation with optional citations.
    """

    query_result: Union[Unset, "QueryResult"] = UNSET
    summary_result: Union[Unset, "SummarizeResult"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_result, Unset):
            query_result = self.query_result.to_dict()

        summary_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summary_result, Unset):
            summary_result = self.summary_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_result is not UNSET:
            field_dict["query_result"] = query_result
        if summary_result is not UNSET:
            field_dict["summary_result"] = summary_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_result import QueryResult
        from ..models.summarize_result import SummarizeResult

        d = dict(src_dict)
        _query_result = d.pop("query_result", UNSET)
        query_result: Union[Unset, QueryResult]
        if isinstance(_query_result, Unset):
            query_result = UNSET
        else:
            query_result = QueryResult.from_dict(_query_result)

        _summary_result = d.pop("summary_result", UNSET)
        summary_result: Union[Unset, SummarizeResult]
        if isinstance(_summary_result, Unset):
            summary_result = UNSET
        else:
            summary_result = SummarizeResult.from_dict(_summary_result)

        rag_result = cls(
            query_result=query_result,
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
