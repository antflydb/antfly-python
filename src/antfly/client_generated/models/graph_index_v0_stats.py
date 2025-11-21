from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_index_v0_stats_edge_types import GraphIndexV0StatsEdgeTypes


T = TypeVar("T", bound="GraphIndexV0Stats")


@_attrs_define
class GraphIndexV0Stats:
    """Statistics for graph_v0 index

    Attributes:
        error (Union[Unset, str]): Error message if stats could not be retrieved
        total_edges (Union[Unset, int]): Total number of edges in the graph
        edge_types (Union[Unset, GraphIndexV0StatsEdgeTypes]): Count of edges per edge type
    """

    error: Union[Unset, str] = UNSET
    total_edges: Union[Unset, int] = UNSET
    edge_types: Union[Unset, "GraphIndexV0StatsEdgeTypes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        total_edges = self.total_edges

        edge_types: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edge_types, Unset):
            edge_types = self.edge_types.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if total_edges is not UNSET:
            field_dict["total_edges"] = total_edges
        if edge_types is not UNSET:
            field_dict["edge_types"] = edge_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_index_v0_stats_edge_types import GraphIndexV0StatsEdgeTypes

        d = dict(src_dict)
        error = d.pop("error", UNSET)

        total_edges = d.pop("total_edges", UNSET)

        _edge_types = d.pop("edge_types", UNSET)
        edge_types: Union[Unset, GraphIndexV0StatsEdgeTypes]
        if isinstance(_edge_types, Unset):
            edge_types = UNSET
        else:
            edge_types = GraphIndexV0StatsEdgeTypes.from_dict(_edge_types)

        graph_index_v0_stats = cls(
            error=error,
            total_edges=total_edges,
            edge_types=edge_types,
        )

        graph_index_v0_stats.additional_properties = d
        return graph_index_v0_stats

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
