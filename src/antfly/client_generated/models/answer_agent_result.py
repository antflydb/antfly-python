from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_transformation_result import ClassificationTransformationResult
    from ..models.query_result import QueryResult


T = TypeVar("T", bound="AnswerAgentResult")


@_attrs_define
class AnswerAgentResult:
    """Answer agent result with classification and generated answer with inline document references

    Attributes:
        classification_transformation (Union[Unset, ClassificationTransformationResult]): Query classification and
            transformation result combining all query enhancements
        query_results (Union[Unset, list['QueryResult']]): Results from each executed query
        reasoning (Union[Unset, str]): LLM's reasoning process (if with_reasoning was enabled)
        answer (Union[Unset, str]): Generated answer (markdown format with inline document references)
        followup_questions (Union[Unset, list[str]]): Suggested follow-up questions (if with_followup was enabled)
    """

    classification_transformation: Union[Unset, "ClassificationTransformationResult"] = UNSET
    query_results: Union[Unset, list["QueryResult"]] = UNSET
    reasoning: Union[Unset, str] = UNSET
    answer: Union[Unset, str] = UNSET
    followup_questions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classification_transformation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.classification_transformation, Unset):
            classification_transformation = self.classification_transformation.to_dict()

        query_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.query_results, Unset):
            query_results = []
            for query_results_item_data in self.query_results:
                query_results_item = query_results_item_data.to_dict()
                query_results.append(query_results_item)

        reasoning = self.reasoning

        answer = self.answer

        followup_questions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.followup_questions, Unset):
            followup_questions = self.followup_questions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classification_transformation is not UNSET:
            field_dict["classification_transformation"] = classification_transformation
        if query_results is not UNSET:
            field_dict["query_results"] = query_results
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if answer is not UNSET:
            field_dict["answer"] = answer
        if followup_questions is not UNSET:
            field_dict["followup_questions"] = followup_questions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.classification_transformation_result import ClassificationTransformationResult
        from ..models.query_result import QueryResult

        d = dict(src_dict)
        _classification_transformation = d.pop("classification_transformation", UNSET)
        classification_transformation: Union[Unset, ClassificationTransformationResult]
        if isinstance(_classification_transformation, Unset):
            classification_transformation = UNSET
        else:
            classification_transformation = ClassificationTransformationResult.from_dict(_classification_transformation)

        query_results = []
        _query_results = d.pop("query_results", UNSET)
        for query_results_item_data in _query_results or []:
            query_results_item = QueryResult.from_dict(query_results_item_data)

            query_results.append(query_results_item)

        reasoning = d.pop("reasoning", UNSET)

        answer = d.pop("answer", UNSET)

        followup_questions = cast(list[str], d.pop("followup_questions", UNSET))

        answer_agent_result = cls(
            classification_transformation=classification_transformation,
            query_results=query_results,
            reasoning=reasoning,
            answer=answer,
            followup_questions=followup_questions,
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
