from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retrieval_reasoning_step_details import RetrievalReasoningStepDetails


T = TypeVar("T", bound="RetrievalReasoningStep")


@_attrs_define
class RetrievalReasoningStep:
    """A step in the retrieval reasoning chain

    Attributes:
        step (str): Name of the tool call or action taken Example: semantic_search.
        action (str): What action was taken Example: Searched for OAuth configuration in doc_embeddings index.
        details (Union[Unset, RetrievalReasoningStepDetails]): Additional details about the step (e.g., tool arguments,
            result count)
    """

    step: str
    action: str
    details: Union[Unset, "RetrievalReasoningStepDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        action = self.action

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step": step,
                "action": action,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retrieval_reasoning_step_details import RetrievalReasoningStepDetails

        d = dict(src_dict)
        step = d.pop("step")

        action = d.pop("action")

        _details = d.pop("details", UNSET)
        details: Union[Unset, RetrievalReasoningStepDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RetrievalReasoningStepDetails.from_dict(_details)

        retrieval_reasoning_step = cls(
            step=step,
            action=action,
            details=details,
        )

        retrieval_reasoning_step.additional_properties = d
        return retrieval_reasoning_step

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
