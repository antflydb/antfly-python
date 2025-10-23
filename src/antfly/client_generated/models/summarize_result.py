from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.citation import Citation


T = TypeVar("T", bound="SummarizeResult")


@_attrs_define
class SummarizeResult:
    """Result of a summarization operation with optional citations.

    Attributes:
        summary (str): The generated summary text
        citations (list['Citation']): List of citations referencing source documents
    """

    summary: str
    citations: list["Citation"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        citations = []
        for citations_item_data in self.citations:
            citations_item = citations_item_data.to_dict()
            citations.append(citations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
                "citations": citations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.citation import Citation

        d = dict(src_dict)
        summary = d.pop("summary")

        citations = []
        _citations = d.pop("citations")
        for citations_item_data in _citations:
            citations_item = Citation.from_dict(citations_item_data)

            citations.append(citations_item)

        summarize_result = cls(
            summary=summary,
            citations=citations,
        )

        summarize_result.additional_properties = d
        return summarize_result

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
