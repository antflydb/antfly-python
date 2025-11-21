from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.graph_query_type import GraphQueryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_node_selector import GraphNodeSelector
    from ..models.graph_query_params import GraphQueryParams


T = TypeVar("T", bound="GraphQuery")


@_attrs_define
class GraphQuery:
    """Declarative graph query to execute after full-text/vector searches

    Attributes:
        type_ (GraphQueryType): Type of graph query to execute
        index_name (str): Graph index name (must be graph_v0 type)
        start_nodes (GraphNodeSelector): Defines how to select start/target nodes for graph queries
        params (GraphQueryParams): Parameters for graph traversal and pathfinding
        target_nodes (Union[Unset, GraphNodeSelector]): Defines how to select start/target nodes for graph queries
        include_documents (Union[Unset, bool]): Fetch full documents for graph results
        include_edges (Union[Unset, bool]): Include edge details for each node
        fields (Union[Unset, list[str]]): Which fields to return from documents
    """

    type_: GraphQueryType
    index_name: str
    start_nodes: "GraphNodeSelector"
    params: "GraphQueryParams"
    target_nodes: Union[Unset, "GraphNodeSelector"] = UNSET
    include_documents: Union[Unset, bool] = UNSET
    include_edges: Union[Unset, bool] = UNSET
    fields: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        index_name = self.index_name

        start_nodes = self.start_nodes.to_dict()

        params = self.params.to_dict()

        target_nodes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target_nodes, Unset):
            target_nodes = self.target_nodes.to_dict()

        include_documents = self.include_documents

        include_edges = self.include_edges

        fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "index_name": index_name,
                "start_nodes": start_nodes,
                "params": params,
            }
        )
        if target_nodes is not UNSET:
            field_dict["target_nodes"] = target_nodes
        if include_documents is not UNSET:
            field_dict["include_documents"] = include_documents
        if include_edges is not UNSET:
            field_dict["include_edges"] = include_edges
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_node_selector import GraphNodeSelector
        from ..models.graph_query_params import GraphQueryParams

        d = dict(src_dict)
        type_ = GraphQueryType(d.pop("type"))

        index_name = d.pop("index_name")

        start_nodes = GraphNodeSelector.from_dict(d.pop("start_nodes"))

        params = GraphQueryParams.from_dict(d.pop("params"))

        _target_nodes = d.pop("target_nodes", UNSET)
        target_nodes: Union[Unset, GraphNodeSelector]
        if isinstance(_target_nodes, Unset):
            target_nodes = UNSET
        else:
            target_nodes = GraphNodeSelector.from_dict(_target_nodes)

        include_documents = d.pop("include_documents", UNSET)

        include_edges = d.pop("include_edges", UNSET)

        fields = cast(list[str], d.pop("fields", UNSET))

        graph_query = cls(
            type_=type_,
            index_name=index_name,
            start_nodes=start_nodes,
            params=params,
            target_nodes=target_nodes,
            include_documents=include_documents,
            include_edges=include_edges,
            fields=fields,
        )

        graph_query.additional_properties = d
        return graph_query

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
