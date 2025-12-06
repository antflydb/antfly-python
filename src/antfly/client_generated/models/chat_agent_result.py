from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_message import ChatMessage
    from ..models.clarification_request import ClarificationRequest
    from ..models.classification_transformation_result import ClassificationTransformationResult
    from ..models.filter_spec import FilterSpec
    from ..models.schemas_chat_agent_result_query_results_item import SchemasChatAgentResultQueryResultsItem


T = TypeVar("T", bound="ChatAgentResult")


@_attrs_define
class ChatAgentResult:
    """
    Attributes:
        messages (list['ChatMessage']): Updated conversation history including the assistant's response
        pending_clarification (Union[Unset, ClarificationRequest]): A request for clarification from the user
        applied_filters (Union[Unset, list['FilterSpec']]): Filters that have been applied in this conversation
        query_results (Union[Unset, list['SchemasChatAgentResultQueryResultsItem']]): Search results from executed
            queries
        answer (Union[Unset, str]): Final answer text (if available)
        answer_confidence (Union[Unset, float]): Confidence in the answer
        tool_calls_made (Union[Unset, int]): Number of tool calls made in this turn
        classification_transformation (Union[Unset, ClassificationTransformationResult]): Query classification and
            transformation result combining all query enhancements including strategy selection and semantic optimization
    """

    messages: list["ChatMessage"]
    pending_clarification: Union[Unset, "ClarificationRequest"] = UNSET
    applied_filters: Union[Unset, list["FilterSpec"]] = UNSET
    query_results: Union[Unset, list["SchemasChatAgentResultQueryResultsItem"]] = UNSET
    answer: Union[Unset, str] = UNSET
    answer_confidence: Union[Unset, float] = UNSET
    tool_calls_made: Union[Unset, int] = UNSET
    classification_transformation: Union[Unset, "ClassificationTransformationResult"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        pending_clarification: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pending_clarification, Unset):
            pending_clarification = self.pending_clarification.to_dict()

        applied_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.applied_filters, Unset):
            applied_filters = []
            for applied_filters_item_data in self.applied_filters:
                applied_filters_item = applied_filters_item_data.to_dict()
                applied_filters.append(applied_filters_item)

        query_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.query_results, Unset):
            query_results = []
            for query_results_item_data in self.query_results:
                query_results_item = query_results_item_data.to_dict()
                query_results.append(query_results_item)

        answer = self.answer

        answer_confidence = self.answer_confidence

        tool_calls_made = self.tool_calls_made

        classification_transformation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.classification_transformation, Unset):
            classification_transformation = self.classification_transformation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )
        if pending_clarification is not UNSET:
            field_dict["pending_clarification"] = pending_clarification
        if applied_filters is not UNSET:
            field_dict["applied_filters"] = applied_filters
        if query_results is not UNSET:
            field_dict["query_results"] = query_results
        if answer is not UNSET:
            field_dict["answer"] = answer
        if answer_confidence is not UNSET:
            field_dict["answer_confidence"] = answer_confidence
        if tool_calls_made is not UNSET:
            field_dict["tool_calls_made"] = tool_calls_made
        if classification_transformation is not UNSET:
            field_dict["classification_transformation"] = classification_transformation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message import ChatMessage
        from ..models.clarification_request import ClarificationRequest
        from ..models.classification_transformation_result import ClassificationTransformationResult
        from ..models.filter_spec import FilterSpec
        from ..models.schemas_chat_agent_result_query_results_item import SchemasChatAgentResultQueryResultsItem

        d = dict(src_dict)
        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = ChatMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        _pending_clarification = d.pop("pending_clarification", UNSET)
        pending_clarification: Union[Unset, ClarificationRequest]
        if isinstance(_pending_clarification, Unset):
            pending_clarification = UNSET
        else:
            pending_clarification = ClarificationRequest.from_dict(_pending_clarification)

        applied_filters = []
        _applied_filters = d.pop("applied_filters", UNSET)
        for applied_filters_item_data in _applied_filters or []:
            applied_filters_item = FilterSpec.from_dict(applied_filters_item_data)

            applied_filters.append(applied_filters_item)

        query_results = []
        _query_results = d.pop("query_results", UNSET)
        for query_results_item_data in _query_results or []:
            query_results_item = SchemasChatAgentResultQueryResultsItem.from_dict(query_results_item_data)

            query_results.append(query_results_item)

        answer = d.pop("answer", UNSET)

        answer_confidence = d.pop("answer_confidence", UNSET)

        tool_calls_made = d.pop("tool_calls_made", UNSET)

        _classification_transformation = d.pop("classification_transformation", UNSET)
        classification_transformation: Union[Unset, ClassificationTransformationResult]
        if isinstance(_classification_transformation, Unset):
            classification_transformation = UNSET
        else:
            classification_transformation = ClassificationTransformationResult.from_dict(_classification_transformation)

        chat_agent_result = cls(
            messages=messages,
            pending_clarification=pending_clarification,
            applied_filters=applied_filters,
            query_results=query_results,
            answer=answer,
            answer_confidence=answer_confidence,
            tool_calls_made=tool_calls_made,
            classification_transformation=classification_transformation,
        )

        chat_agent_result.additional_properties = d
        return chat_agent_result

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
