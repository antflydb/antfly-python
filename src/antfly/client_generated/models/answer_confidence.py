from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnswerConfidence")


@_attrs_define
class AnswerConfidence:
    """Confidence assessment for the generated answer

    Attributes:
        answer_confidence (float): Overall confidence in the answer (0.0 to 1.0). Considers both ability to answer from
            provided resources and general knowledge.
        context_relevance (float): Relevance of the provided resources to the question (0.0 to 1.0)
    """

    answer_confidence: float
    context_relevance: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer_confidence = self.answer_confidence

        context_relevance = self.context_relevance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answer_confidence": answer_confidence,
                "context_relevance": context_relevance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        answer_confidence = d.pop("answer_confidence")

        context_relevance = d.pop("context_relevance")

        answer_confidence = cls(
            answer_confidence=answer_confidence,
            context_relevance=context_relevance,
        )

        answer_confidence.additional_properties = d
        return answer_confidence

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
