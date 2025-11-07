from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.answer_agent_result_classification import AnswerAgentResultClassification
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_request import QueryRequest
    from ..models.query_result import QueryResult


T = TypeVar("T", bound="AnswerAgentResult")


@_attrs_define
class AnswerAgentResult:
    """Answer agent result with classification, keywords, and generated answer or document IDs

    Attributes:
        classification (Union[Unset, AnswerAgentResultClassification]): Classification of the query type
        keywords (Union[Unset, list[str]]): Keywords extracted from the query
        queries_executed (Union[Unset, list['QueryRequest']]): The queries that were generated and executed
        query_results (Union[Unset, list['QueryResult']]): Results from each generated query
        answer (Union[Unset, str]): Generated answer for "question" classification (markdown format with inline document
            references)
        document_ids (Union[Unset, list[str]]): Document IDs for "search" classification
    """

    classification: Union[Unset, AnswerAgentResultClassification] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    queries_executed: Union[Unset, list["QueryRequest"]] = UNSET
    query_results: Union[Unset, list["QueryResult"]] = UNSET
    answer: Union[Unset, str] = UNSET
    document_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classification: Union[Unset, str] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.value

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        queries_executed: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.queries_executed, Unset):
            queries_executed = []
            for queries_executed_item_data in self.queries_executed:
                queries_executed_item = queries_executed_item_data.to_dict()
                queries_executed.append(queries_executed_item)

        query_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.query_results, Unset):
            query_results = []
            for query_results_item_data in self.query_results:
                query_results_item = query_results_item_data.to_dict()
                query_results.append(query_results_item)

        answer = self.answer

        document_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.document_ids, Unset):
            document_ids = self.document_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classification is not UNSET:
            field_dict["classification"] = classification
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if queries_executed is not UNSET:
            field_dict["queries_executed"] = queries_executed
        if query_results is not UNSET:
            field_dict["query_results"] = query_results
        if answer is not UNSET:
            field_dict["answer"] = answer
        if document_ids is not UNSET:
            field_dict["document_ids"] = document_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_request import QueryRequest
        from ..models.query_result import QueryResult

        d = dict(src_dict)
        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, AnswerAgentResultClassification]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = AnswerAgentResultClassification(_classification)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        queries_executed = []
        _queries_executed = d.pop("queries_executed", UNSET)
        for queries_executed_item_data in _queries_executed or []:
            queries_executed_item = QueryRequest.from_dict(queries_executed_item_data)

            queries_executed.append(queries_executed_item)

        query_results = []
        _query_results = d.pop("query_results", UNSET)
        for query_results_item_data in _query_results or []:
            query_results_item = QueryResult.from_dict(query_results_item_data)

            query_results.append(query_results_item)

        answer = d.pop("answer", UNSET)

        document_ids = cast(list[str], d.pop("document_ids", UNSET))

        answer_agent_result = cls(
            classification=classification,
            keywords=keywords,
            queries_executed=queries_executed,
            query_results=query_results,
            answer=answer,
            document_ids=document_ids,
        )

        answer_agent_result.additional_properties = d
        return answer_agent_result

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
