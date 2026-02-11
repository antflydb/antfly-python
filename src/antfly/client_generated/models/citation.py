from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Citation")


@_attrs_define
class Citation:
    """A citation extracted from the generated response

    Attributes:
        document_id (str): ID of the cited document
        text (Union[Unset, str]): Relevant text from the document
        score (Union[Unset, float]): Relevance score of the citation
    """

    document_id: str
    text: Union[Unset, str] = UNSET
    score: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        text = self.text

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_id": document_id,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("document_id")

        text = d.pop("text", UNSET)

        score = d.pop("score", UNSET)

        citation = cls(
            document_id=document_id,
            text=text,
            score=score,
        )

        citation.additional_properties = d
        return citation

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
