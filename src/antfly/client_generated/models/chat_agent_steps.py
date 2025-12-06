from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.answer_step_config import AnswerStepConfig
    from ..models.chat_tools_config import ChatToolsConfig
    from ..models.classification_step_config import ClassificationStepConfig


T = TypeVar("T", bound="ChatAgentSteps")


@_attrs_define
class ChatAgentSteps:
    """Per-step configuration for the chat agent pipeline. Similar to AnswerAgentSteps
    but includes tool-specific configuration.

        Attributes:
            classification (Union[Unset, ClassificationStepConfig]): Configuration for the classification step. This step
                analyzes the query,
                selects the optimal retrieval strategy, and generates semantic transformations.
            answer (Union[Unset, AnswerStepConfig]): Configuration for the answer generation step. This step generates the
                final
                answer from retrieved documents using the reasoning as context.
            tools (Union[Unset, ChatToolsConfig]): Configuration for chat agent tools.

                If `enabled_tools` is empty/omitted, defaults to: add_filter, ask_clarification, search.

                For models that don't support native tool calling (e.g., Ollama),
                a prompt-based fallback is used with structured output parsing.
    """

    classification: Union[Unset, "ClassificationStepConfig"] = UNSET
    answer: Union[Unset, "AnswerStepConfig"] = UNSET
    tools: Union[Unset, "ChatToolsConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classification: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.to_dict()

        answer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.answer, Unset):
            answer = self.answer.to_dict()

        tools: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tools, Unset):
            tools = self.tools.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classification is not UNSET:
            field_dict["classification"] = classification
        if answer is not UNSET:
            field_dict["answer"] = answer
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.answer_step_config import AnswerStepConfig
        from ..models.chat_tools_config import ChatToolsConfig
        from ..models.classification_step_config import ClassificationStepConfig

        d = dict(src_dict)
        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, ClassificationStepConfig]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = ClassificationStepConfig.from_dict(_classification)

        _answer = d.pop("answer", UNSET)
        answer: Union[Unset, AnswerStepConfig]
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = AnswerStepConfig.from_dict(_answer)

        _tools = d.pop("tools", UNSET)
        tools: Union[Unset, ChatToolsConfig]
        if isinstance(_tools, Unset):
            tools = UNSET
        else:
            tools = ChatToolsConfig.from_dict(_tools)

        chat_agent_steps = cls(
            classification=classification,
            answer=answer,
            tools=tools,
        )

        chat_agent_steps.additional_properties = d
        return chat_agent_steps

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
