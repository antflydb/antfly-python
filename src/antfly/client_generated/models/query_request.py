from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.merge_strategy import MergeStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analyses import Analyses
    from ..models.query_request_embeddings import QueryRequestEmbeddings
    from ..models.query_request_exclusion_query import QueryRequestExclusionQuery
    from ..models.query_request_facets import QueryRequestFacets
    from ..models.query_request_filter_query import QueryRequestFilterQuery
    from ..models.query_request_full_text_search import QueryRequestFullTextSearch
    from ..models.query_request_order_by import QueryRequestOrderBy
    from ..models.reranker_config import RerankerConfig


T = TypeVar("T", bound="QueryRequest")


@_attrs_define
class QueryRequest:
    r"""
    Attributes:
        table (Union[Unset, str]): Name of the table to query. Optional for global queries. Example: wikipedia.
        full_text_search (Union[Unset, QueryRequestFullTextSearch]): Bleve query for full-text search. Supports field-
            specific queries, boolean operators, and complex expressions.

            Examples:
            - Simple: `{"query": "computer"}`
            - Field-specific: `{"query": "body:computer"}`
            - Boolean: `{"query": "artificial AND intelligence"}`
            - Range: `{"query": "year:>2020"}`
            - Phrase: `{"query": "\"exact phrase\""}`
             Example: {'query': 'body:computer AND category:technology'}.
        semantic_search (Union[Unset, str]): Natural language query for vector similarity search. Results are ranked by
            semantic similarity
            to the query and can be combined with full_text_search using Reciprocal Rank Fusion (RRF).

            The semantic_search string is automatically embedded using the configured embedding model
            for the specified indexes.
             Example: artificial intelligence and machine learning applications.
        indexes (Union[Unset, list[str]]): List of vector index names to use for semantic search. Required when using
            semantic_search.
            Multiple indexes can be specified, and their results will be merged using RRF.
             Example: ['title_body_nomic', 'description_embedding'].
        filter_prefix (Union[Unset, str]): Filter results by key prefix. Only returns documents whose keys start with
            this string.
            Applied before scoring to improve performance.

            Common use cases:
            - Multi-tenant filtering: `"tenant:acme:"`
            - User-specific data: `"user:123:"`
            - Document type filtering: `"article:"`
        filter_query (Union[Unset, QueryRequestFilterQuery]): Bleve query applied as an AND condition. Documents must
            match both the main query
            and this filter. Applied before scoring for better performance.

            Use for:
            - Status filtering: `"status:published"`
            - Date ranges: `"created_at:>2023-01-01"`
            - Category filtering: `"category:technology AND language:en"`
             Example: {'query': 'category:technology AND year:>2020'}.
        exclusion_query (Union[Unset, QueryRequestExclusionQuery]): Bleve query applied as a NOT condition. Documents
            matching this query are excluded
            from results. Applied before scoring.

            Use for:
            - Excluding drafts: `"status:draft"`
            - Removing deprecated content: `"deprecated:true"`
            - Filtering out archived items: `"status:archived"`
             Example: {'query': 'category:deprecated OR status:archived'}.
        facets (Union[Unset, QueryRequestFacets]): Faceting configuration for aggregating results by field values.
            Useful for building faceted navigation and filters.
        embeddings (Union[Unset, QueryRequestEmbeddings]): Pre-computed embeddings to use for semantic searches instead
            of embedding the semantic_search string.
            The keys are the index names, and values are the embedding vectors.

            Use when you've already generated embeddings on the client side to avoid redundant embedding calls.
        fields (Union[Unset, list[str]]): List of fields to include in the results. If not specified, all fields are
            returned.
            Use to reduce response size and improve performance.
             Example: ['title', 'url', 'summary', 'created_at'].
        limit (Union[Unset, int]): Maximum number of results to return. For semantic_search, this is the topk parameter.
            Default varies by query type (typically 10).
             Example: 20.
        offset (Union[Unset, int]): Number of results to skip for pagination. Only available for full_text_search
            queries.
            Not supported for semantic_search due to vector index limitations.
        order_by (Union[Unset, QueryRequestOrderBy]): Sort order for results. Map of field names to boolean (true =
            descending, false = ascending).
            Only applicable for full_text_search queries. Semantic searches are always sorted by similarity score.
             Example: {'created_at': True, 'score': True}.
        distance_under (Union[Unset, float]): Maximum distance threshold for semantic similarity search. Results with
            distance
            greater than this value are excluded. Lower distances indicate higher similarity.

            Useful for filtering out low-confidence matches.
             Example: 0.5.
        distance_over (Union[Unset, float]): Minimum distance threshold for semantic similarity search. Results with
            distance
            less than this value are excluded.

            Useful for excluding near-exact duplicates or finding dissimilar documents.
             Example: 0.1.
        merge_strategy (Union[Unset, MergeStrategy]): Merge strategy for combining results from the semantic_search and
            full_text_search.
            rrf: Reciprocal Rank Fusion
            failover: Use full_text_search if embedding generation fails
        count (Union[Unset, bool]): If true, returns only the total count of matching documents without retrieving the
            actual documents.
            Useful for pagination and displaying result counts.
        reranker (Union[Unset, RerankerConfig]): A unified configuration for an embedding provider. Example:
            {'provider': 'openai', 'model': 'text-embedding-004', 'field': 'content'}.
        analyses (Union[Unset, Analyses]):
        document_renderer (Union[Unset, str]): Optional Handlebars template string for rendering document content in RAG
            queries.
            Template has access to document fields via `{{this.fields.fieldName}}`.

            Useful for customizing how documents are presented to LLMs in RAG pipelines.
             Example: Title: {{this.fields.title}}
            Body: {{this.fields.body}}
            URL: {{this.fields.url}}.
    """

    table: Union[Unset, str] = UNSET
    full_text_search: Union[Unset, "QueryRequestFullTextSearch"] = UNSET
    semantic_search: Union[Unset, str] = UNSET
    indexes: Union[Unset, list[str]] = UNSET
    filter_prefix: Union[Unset, str] = UNSET
    filter_query: Union[Unset, "QueryRequestFilterQuery"] = UNSET
    exclusion_query: Union[Unset, "QueryRequestExclusionQuery"] = UNSET
    facets: Union[Unset, "QueryRequestFacets"] = UNSET
    embeddings: Union[Unset, "QueryRequestEmbeddings"] = UNSET
    fields: Union[Unset, list[str]] = UNSET
    limit: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    order_by: Union[Unset, "QueryRequestOrderBy"] = UNSET
    distance_under: Union[Unset, float] = UNSET
    distance_over: Union[Unset, float] = UNSET
    merge_strategy: Union[Unset, MergeStrategy] = UNSET
    count: Union[Unset, bool] = UNSET
    reranker: Union[Unset, "RerankerConfig"] = UNSET
    analyses: Union[Unset, "Analyses"] = UNSET
    document_renderer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table

        full_text_search: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.full_text_search, Unset):
            full_text_search = self.full_text_search.to_dict()

        semantic_search = self.semantic_search

        indexes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.indexes, Unset):
            indexes = self.indexes

        filter_prefix = self.filter_prefix

        filter_query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_query, Unset):
            filter_query = self.filter_query.to_dict()

        exclusion_query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exclusion_query, Unset):
            exclusion_query = self.exclusion_query.to_dict()

        facets: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.facets, Unset):
            facets = self.facets.to_dict()

        embeddings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.embeddings, Unset):
            embeddings = self.embeddings.to_dict()

        fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        limit = self.limit

        offset = self.offset

        order_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_by, Unset):
            order_by = self.order_by.to_dict()

        distance_under = self.distance_under

        distance_over = self.distance_over

        merge_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.merge_strategy, Unset):
            merge_strategy = self.merge_strategy.value

        count = self.count

        reranker: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reranker, Unset):
            reranker = self.reranker.to_dict()

        analyses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.analyses, Unset):
            analyses = self.analyses.to_dict()

        document_renderer = self.document_renderer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table is not UNSET:
            field_dict["table"] = table
        if full_text_search is not UNSET:
            field_dict["full_text_search"] = full_text_search
        if semantic_search is not UNSET:
            field_dict["semantic_search"] = semantic_search
        if indexes is not UNSET:
            field_dict["indexes"] = indexes
        if filter_prefix is not UNSET:
            field_dict["filter_prefix"] = filter_prefix
        if filter_query is not UNSET:
            field_dict["filter_query"] = filter_query
        if exclusion_query is not UNSET:
            field_dict["exclusion_query"] = exclusion_query
        if facets is not UNSET:
            field_dict["facets"] = facets
        if embeddings is not UNSET:
            field_dict["embeddings"] = embeddings
        if fields is not UNSET:
            field_dict["fields"] = fields
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if order_by is not UNSET:
            field_dict["order_by"] = order_by
        if distance_under is not UNSET:
            field_dict["distance_under"] = distance_under
        if distance_over is not UNSET:
            field_dict["distance_over"] = distance_over
        if merge_strategy is not UNSET:
            field_dict["merge_strategy"] = merge_strategy
        if count is not UNSET:
            field_dict["count"] = count
        if reranker is not UNSET:
            field_dict["reranker"] = reranker
        if analyses is not UNSET:
            field_dict["analyses"] = analyses
        if document_renderer is not UNSET:
            field_dict["document_renderer"] = document_renderer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analyses import Analyses
        from ..models.query_request_embeddings import QueryRequestEmbeddings
        from ..models.query_request_exclusion_query import QueryRequestExclusionQuery
        from ..models.query_request_facets import QueryRequestFacets
        from ..models.query_request_filter_query import QueryRequestFilterQuery
        from ..models.query_request_full_text_search import QueryRequestFullTextSearch
        from ..models.query_request_order_by import QueryRequestOrderBy
        from ..models.reranker_config import RerankerConfig

        d = dict(src_dict)
        table = d.pop("table", UNSET)

        _full_text_search = d.pop("full_text_search", UNSET)
        full_text_search: Union[Unset, QueryRequestFullTextSearch]
        if isinstance(_full_text_search, Unset):
            full_text_search = UNSET
        else:
            full_text_search = QueryRequestFullTextSearch.from_dict(_full_text_search)

        semantic_search = d.pop("semantic_search", UNSET)

        indexes = cast(list[str], d.pop("indexes", UNSET))

        filter_prefix = d.pop("filter_prefix", UNSET)

        _filter_query = d.pop("filter_query", UNSET)
        filter_query: Union[Unset, QueryRequestFilterQuery]
        if isinstance(_filter_query, Unset):
            filter_query = UNSET
        else:
            filter_query = QueryRequestFilterQuery.from_dict(_filter_query)

        _exclusion_query = d.pop("exclusion_query", UNSET)
        exclusion_query: Union[Unset, QueryRequestExclusionQuery]
        if isinstance(_exclusion_query, Unset):
            exclusion_query = UNSET
        else:
            exclusion_query = QueryRequestExclusionQuery.from_dict(_exclusion_query)

        _facets = d.pop("facets", UNSET)
        facets: Union[Unset, QueryRequestFacets]
        if isinstance(_facets, Unset):
            facets = UNSET
        else:
            facets = QueryRequestFacets.from_dict(_facets)

        _embeddings = d.pop("embeddings", UNSET)
        embeddings: Union[Unset, QueryRequestEmbeddings]
        if isinstance(_embeddings, Unset):
            embeddings = UNSET
        else:
            embeddings = QueryRequestEmbeddings.from_dict(_embeddings)

        fields = cast(list[str], d.pop("fields", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        _order_by = d.pop("order_by", UNSET)
        order_by: Union[Unset, QueryRequestOrderBy]
        if isinstance(_order_by, Unset):
            order_by = UNSET
        else:
            order_by = QueryRequestOrderBy.from_dict(_order_by)

        distance_under = d.pop("distance_under", UNSET)

        distance_over = d.pop("distance_over", UNSET)

        _merge_strategy = d.pop("merge_strategy", UNSET)
        merge_strategy: Union[Unset, MergeStrategy]
        if isinstance(_merge_strategy, Unset):
            merge_strategy = UNSET
        else:
            merge_strategy = MergeStrategy(_merge_strategy)

        count = d.pop("count", UNSET)

        _reranker = d.pop("reranker", UNSET)
        reranker: Union[Unset, RerankerConfig]
        if isinstance(_reranker, Unset):
            reranker = UNSET
        else:
            reranker = RerankerConfig.from_dict(_reranker)

        _analyses = d.pop("analyses", UNSET)
        analyses: Union[Unset, Analyses]
        if isinstance(_analyses, Unset):
            analyses = UNSET
        else:
            analyses = Analyses.from_dict(_analyses)

        document_renderer = d.pop("document_renderer", UNSET)

        query_request = cls(
            table=table,
            full_text_search=full_text_search,
            semantic_search=semantic_search,
            indexes=indexes,
            filter_prefix=filter_prefix,
            filter_query=filter_query,
            exclusion_query=exclusion_query,
            facets=facets,
            embeddings=embeddings,
            fields=fields,
            limit=limit,
            offset=offset,
            order_by=order_by,
            distance_under=distance_under,
            distance_over=distance_over,
            merge_strategy=merge_strategy,
            count=count,
            reranker=reranker,
            analyses=analyses,
            document_renderer=document_renderer,
        )

        query_request.additional_properties = d
        return query_request

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
