from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.join_result import JoinResult
    from ..models.query_hits import QueryHits
    from ..models.query_result_aggregations import QueryResultAggregations
    from ..models.query_result_analyses import QueryResultAnalyses
    from ..models.query_result_graph_results import QueryResultGraphResults


T = TypeVar("T", bound="QueryResult")


@_attrs_define
class QueryResult:
    """Result of a query operation as an array of results and a count.

    Attributes:
        took (int): Duration of the query in milliseconds.
        status (int): HTTP status code of the query operation.
        hits (Union[Unset, QueryHits]): A list of query hits.
        aggregations (Union[Unset, QueryResultAggregations]): Aggregation results keyed by the user-defined aggregation
            names from the request.
            Contains computed metrics or buckets depending on the aggregation type.
        analyses (Union[Unset, QueryResultAnalyses]): Analysis results like PCA and t-SNE per index embeddings.
        graph_results (Union[Unset, QueryResultGraphResults]): Results from declarative graph queries.
        join_result (Union[Unset, JoinResult]): Statistics and metadata about join execution.
        error (Union[Unset, str]): Error message if the query failed.
        table (Union[Unset, str]): Which table this result came from
    """

    took: int
    status: int
    hits: Union[Unset, "QueryHits"] = UNSET
    aggregations: Union[Unset, "QueryResultAggregations"] = UNSET
    analyses: Union[Unset, "QueryResultAnalyses"] = UNSET
    graph_results: Union[Unset, "QueryResultGraphResults"] = UNSET
    join_result: Union[Unset, "JoinResult"] = UNSET
    error: Union[Unset, str] = UNSET
    table: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        took = self.took

        status = self.status

        hits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hits, Unset):
            hits = self.hits.to_dict()

        aggregations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aggregations, Unset):
            aggregations = self.aggregations.to_dict()

        analyses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.analyses, Unset):
            analyses = self.analyses.to_dict()

        graph_results: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.graph_results, Unset):
            graph_results = self.graph_results.to_dict()

        join_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.join_result, Unset):
            join_result = self.join_result.to_dict()

        error = self.error

        table = self.table

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "took": took,
                "status": status,
            }
        )
        if hits is not UNSET:
            field_dict["hits"] = hits
        if aggregations is not UNSET:
            field_dict["aggregations"] = aggregations
        if analyses is not UNSET:
            field_dict["analyses"] = analyses
        if graph_results is not UNSET:
            field_dict["graph_results"] = graph_results
        if join_result is not UNSET:
            field_dict["join_result"] = join_result
        if error is not UNSET:
            field_dict["error"] = error
        if table is not UNSET:
            field_dict["table"] = table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.join_result import JoinResult
        from ..models.query_hits import QueryHits
        from ..models.query_result_aggregations import QueryResultAggregations
        from ..models.query_result_analyses import QueryResultAnalyses
        from ..models.query_result_graph_results import QueryResultGraphResults

        d = dict(src_dict)
        took = d.pop("took")

        status = d.pop("status")

        _hits = d.pop("hits", UNSET)
        hits: Union[Unset, QueryHits]
        if isinstance(_hits, Unset):
            hits = UNSET
        else:
            hits = QueryHits.from_dict(_hits)

        _aggregations = d.pop("aggregations", UNSET)
        aggregations: Union[Unset, QueryResultAggregations]
        if isinstance(_aggregations, Unset):
            aggregations = UNSET
        else:
            aggregations = QueryResultAggregations.from_dict(_aggregations)

        _analyses = d.pop("analyses", UNSET)
        analyses: Union[Unset, QueryResultAnalyses]
        if isinstance(_analyses, Unset):
            analyses = UNSET
        else:
            analyses = QueryResultAnalyses.from_dict(_analyses)

        _graph_results = d.pop("graph_results", UNSET)
        graph_results: Union[Unset, QueryResultGraphResults]
        if isinstance(_graph_results, Unset):
            graph_results = UNSET
        else:
            graph_results = QueryResultGraphResults.from_dict(_graph_results)

        _join_result = d.pop("join_result", UNSET)
        join_result: Union[Unset, JoinResult]
        if isinstance(_join_result, Unset):
            join_result = UNSET
        else:
            join_result = JoinResult.from_dict(_join_result)

        error = d.pop("error", UNSET)

        table = d.pop("table", UNSET)

        query_result = cls(
            took=took,
            status=status,
            hits=hits,
            aggregations=aggregations,
            analyses=analyses,
            graph_results=graph_results,
            join_result=join_result,
            error=error,
            table=table,
        )

        query_result.additional_properties = d
        return query_result

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
