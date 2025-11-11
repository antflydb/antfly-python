from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.route_type import RouteType

T = TypeVar("T", bound="ClassificationTransformationResult")


@_attrs_define
class ClassificationTransformationResult:
    """Query classification and transformation result combining all query enhancements

    Attributes:
        route_type (RouteType): Classification of query type: question (specific factual query) or search (exploratory
            query)
        improved_query (str): Clarified query with added context for answer generation (human-readable)
        semantic_query (str): Optimized query for vector/semantic search (concept extraction with synonyms)
        confidence (float): Classification confidence (0.0 to 1.0)
    """

    route_type: RouteType
    improved_query: str
    semantic_query: str
    confidence: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        route_type = self.route_type.value

        improved_query = self.improved_query

        semantic_query = self.semantic_query

        confidence = self.confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "route_type": route_type,
                "improved_query": improved_query,
                "semantic_query": semantic_query,
                "confidence": confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        route_type = RouteType(d.pop("route_type"))

        improved_query = d.pop("improved_query")

        semantic_query = d.pop("semantic_query")

        confidence = d.pop("confidence")

        classification_transformation_result = cls(
            route_type=route_type,
            improved_query=improved_query,
            semantic_query=semantic_query,
            confidence=confidence,
        )

        classification_transformation_result.additional_properties = d
        return classification_transformation_result

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
