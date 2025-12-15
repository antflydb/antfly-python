from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eval_result import EvalResult
    from ..models.generate_result import GenerateResult
    from ..models.query_result import QueryResult


T = TypeVar("T", bound="RAGResult")


@_attrs_define
class RAGResult:
    """RAG result with individual query results and generation/evaluation outcome

    Attributes:
        query_results (Union[Unset, list['QueryResult']]): Results from each query. Check each result's status and error
            fields for failures.
        generate_result (Union[Unset, GenerateResult]): Result of a generate operation. Formatted as markdown by default
            with inline resource references using [resource_id <id>] or [resource_id <id1>, <id2>] format.
        eval_result (Union[Unset, EvalResult]): Complete evaluation result
    """

    query_results: Union[Unset, list["QueryResult"]] = UNSET
    generate_result: Union[Unset, "GenerateResult"] = UNSET
    eval_result: Union[Unset, "EvalResult"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.query_results, Unset):
            query_results = []
            for query_results_item_data in self.query_results:
                query_results_item = query_results_item_data.to_dict()
                query_results.append(query_results_item)

        generate_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.generate_result, Unset):
            generate_result = self.generate_result.to_dict()

        eval_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.eval_result, Unset):
            eval_result = self.eval_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_results is not UNSET:
            field_dict["query_results"] = query_results
        if generate_result is not UNSET:
            field_dict["generate_result"] = generate_result
        if eval_result is not UNSET:
            field_dict["eval_result"] = eval_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eval_result import EvalResult
        from ..models.generate_result import GenerateResult
        from ..models.query_result import QueryResult

        d = dict(src_dict)
        query_results = []
        _query_results = d.pop("query_results", UNSET)
        for query_results_item_data in _query_results or []:
            query_results_item = QueryResult.from_dict(query_results_item_data)

            query_results.append(query_results_item)

        _generate_result = d.pop("generate_result", UNSET)
        generate_result: Union[Unset, GenerateResult]
        if isinstance(_generate_result, Unset):
            generate_result = UNSET
        else:
            generate_result = GenerateResult.from_dict(_generate_result)

        _eval_result = d.pop("eval_result", UNSET)
        eval_result: Union[Unset, EvalResult]
        if isinstance(_eval_result, Unset):
            eval_result = UNSET
        else:
            eval_result = EvalResult.from_dict(_eval_result)

        rag_result = cls(
            query_results=query_results,
            generate_result=generate_result,
            eval_result=eval_result,
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
