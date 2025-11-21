from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserContext")


@_attrs_define
class UserContext:
    """Optional user context to customize the content guidance for each section of the answer agent response.

    **What you can customize**: Style, tone, length, detail level, and focus of content for each section independently.

    **What is fixed**: The response format is always markdown with consistent structure (## Reasoning, ## Answer, ##
    Follow-up Questions).
    Markdown formatting (headings, bullets, code blocks, etc.) is always applied and cannot be disabled.

    **Architecture**: These contexts are passed as template variables to the prompt template. Defaults are set
    at the application layer, and users can override them via this API to customize content guidance.

        Attributes:
            reasoning_context (Union[Unset, str]): Custom content guidance for the reasoning section. Controls what
                information to include,
                the level of detail, and the focus of the reasoning process. Does not control markdown formatting.
                 Example: Keep reasoning brief, 1-2 sentences maximum.
            answer_context (Union[Unset, str]): Custom content guidance for the answer section. Controls the tone, content
                depth, level of detail,
                and what information to emphasize. Does not control markdown formatting (which is always applied).
                 Example: Provide a comprehensive answer with technical details and examples.
            followup_context (Union[Unset, str]): Custom content guidance for follow-up questions. Controls the quantity,
                focus area, tone,
                and style of follow-up questions. Does not control markdown formatting.
                 Example: Generate 5 follow-up questions focused on technical specifications and pricing.
    """

    reasoning_context: Union[Unset, str] = UNSET
    answer_context: Union[Unset, str] = UNSET
    followup_context: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reasoning_context = self.reasoning_context

        answer_context = self.answer_context

        followup_context = self.followup_context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reasoning_context is not UNSET:
            field_dict["reasoning_context"] = reasoning_context
        if answer_context is not UNSET:
            field_dict["answer_context"] = answer_context
        if followup_context is not UNSET:
            field_dict["followup_context"] = followup_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reasoning_context = d.pop("reasoning_context", UNSET)

        answer_context = d.pop("answer_context", UNSET)

        followup_context = d.pop("followup_context", UNSET)

        user_context = cls(
            reasoning_context=reasoning_context,
            answer_context=answer_context,
            followup_context=followup_context,
        )

        user_context.additional_properties = d
        return user_context

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
