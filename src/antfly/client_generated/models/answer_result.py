from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnswerResult")


@_attrs_define
class AnswerResult:
    """Result from answer generation with optional confidence and follow-up questions

    Attributes:
        answer (str): Generated answer in markdown format
        answer_confidence (Union[Unset, float]): Overall confidence in the answer (0.0 to 1.0)
        context_relevance (Union[Unset, float]): Relevance of the provided resources to the question (0.0 to 1.0)
        followup_questions (Union[Unset, list[str]]): Suggested follow-up questions
    """

    answer: str
    answer_confidence: Union[Unset, float] = UNSET
    context_relevance: Union[Unset, float] = UNSET
    followup_questions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer

        answer_confidence = self.answer_confidence

        context_relevance = self.context_relevance

        followup_questions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.followup_questions, Unset):
            followup_questions = self.followup_questions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answer": answer,
            }
        )
        if answer_confidence is not UNSET:
            field_dict["answer_confidence"] = answer_confidence
        if context_relevance is not UNSET:
            field_dict["context_relevance"] = context_relevance
        if followup_questions is not UNSET:
            field_dict["followup_questions"] = followup_questions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        answer = d.pop("answer")

        answer_confidence = d.pop("answer_confidence", UNSET)

        context_relevance = d.pop("context_relevance", UNSET)

        followup_questions = cast(list[str], d.pop("followup_questions", UNSET))

        answer_result = cls(
            answer=answer,
            answer_confidence=answer_confidence,
            context_relevance=context_relevance,
            followup_questions=followup_questions,
        )

        answer_result.additional_properties = d
        return answer_result

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
