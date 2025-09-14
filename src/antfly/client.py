"""Main client interface for Antfly SDK."""

from typing import Dict, List, Optional, Any, cast
from httpx import Timeout
from .exceptions import AntflyException
from antfly_client import Client
from antfly_client.api.api_table import (
    create_table,
    list_tables,
    get_table,
    drop_table,
    query_table,
    batch_table_operations,
    lookup_key,
)
from antfly_client.models import (
    CreateTableRequest,
    QueryRequest,
    BatchRequest,
    Table,
    TableStatus,
    Error,
    CreateTableRequestIndexes,
    TableSchema,
    QueryRequestFullTextSearch,
    BatchRequestInserts,
    QueryResponses,
)
from antfly_client.client import AuthenticatedClient
from antfly_client.types import UNSET


class AntflyClient:
    """High-level client for interacting with Antfly database."""

    def __init__(
        self,
        base_url: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        timeout: float = 30.0,
    ):
        """
        Initialize Antfly client.

        Args:
            base_url: Base URL of the Antfly server
            username: Username for authentication (optional)
            password: Password for authentication (optional)
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip("/")

        httpx_args: Dict[str, Any] = {}
        if username and password:
            httpx_args["auth"] = (username, password)

        self._client = Client(
            base_url=self.base_url,
            timeout=Timeout(timeout),
            httpx_args=httpx_args,
        )

    # Table operations

    def create_table(
        self,
        name: str,
        num_shards: Optional[int] = None,
        indexes: Optional[Dict[str, Any]] = None,
        schema: Optional[Dict[str, Any]] = None,
    ) -> Table:
        """
        Create a new table.

        Args:
            name: Name of the table
            num_shards: Number of shards for the table
            indexes: Index configurations
            schema: Table schema definition

        Returns:
            Created table object

        Raises:
            AntflyException: If table creation fails
        """
        request = CreateTableRequest(
            num_shards=num_shards if num_shards is not None else UNSET,
            indexes=cast(CreateTableRequestIndexes, indexes) if indexes is not None else UNSET,
            schema=cast(TableSchema, schema) if schema is not None else UNSET,
        )

        response = create_table.sync(
            table_name=name,
            client=cast(AuthenticatedClient, self._client),
            body=request,
        )

        if isinstance(response, Error):
            raise AntflyException(f"Failed to create table '{name}': {response.error}")
        if response is None:
            raise AntflyException(f"Failed to create table '{name}'")

        return response

    def list_tables(self) -> List[TableStatus]:
        """
        List all tables.

        Returns:
            List of table objects

        Raises:
            AntflyException: If listing tables fails
        """
        response = list_tables.sync(client=cast(AuthenticatedClient, self._client))

        if isinstance(response, Error):
            raise AntflyException(f"Failed to list tables: {response.error}")
        if response is None:
            raise AntflyException("Failed to list tables")

        return response

    def get_table(self, name: str) -> TableStatus:
        """
        Get table details.

        Args:
            name: Name of the table

        Returns:
            Table status object

        Raises:
            AntflyException: If getting table fails
        """
        response = get_table.sync(
            table_name=name,
            client=cast(AuthenticatedClient, self._client),
        )

        if isinstance(response, Error):
            raise AntflyException(f"Failed to get table '{name}': {response.error}")
        if response is None:
            raise AntflyException(f"Failed to get table '{name}'")

        return response

    def drop_table(self, name: str) -> None:
        """
        Drop a table.

        Args:
            name: Name of the table to drop

        Raises:
            AntflyException: If dropping table fails
        """
        response = drop_table.sync(
            table_name=name,
            client=cast(AuthenticatedClient, self._client),
        )

        if isinstance(response, Error):
            raise AntflyException(f"Failed to drop table '{name}': {response.error}")
        if response is None:
            raise AntflyException(f"Failed to drop table '{name}'")

    # Query operations

    def query(
        self,
        table: Optional[str] = None,
        full_text_search: Optional[Dict[str, Any]] = None,
        semantic_search: Optional[str] = None,
        filter_prefix: Optional[str] = None,
        limit: int = 10,
        offset: int = 0,
        **kwargs,
    ) -> QueryResponses:
        """
        Query a table or perform global query.

        Args:
            table: Table name (optional for global query)
            full_text_search: Full-text search query
            semantic_search: Semantic search query
            filter_prefix: Key prefix filter
            limit: Maximum number of results
            offset: Number of results to skip
            **kwargs: Additional query parameters

        Returns:
            Query result object

        Raises:
            AntflyException: If query fails
        """
        request = QueryRequest(
            table=table if table is not None else UNSET,
            full_text_search=cast(QueryRequestFullTextSearch, full_text_search)
            if full_text_search is not None
            else UNSET,
            semantic_search=semantic_search if semantic_search is not None else UNSET,
            filter_prefix=filter_prefix if filter_prefix is not None else UNSET,
            limit=limit,
            offset=offset,
            **kwargs,
        )

        if table:
            response = query_table.sync(
                table_name=table,
                client=cast(AuthenticatedClient, self._client),
                body=request,
            )
        else:
            # Use global query endpoint
            from antfly_client.api.api_table import global_query

            response = global_query.sync(
                client=cast(AuthenticatedClient, self._client),
                body=request,
            )

        if isinstance(response, Error):
            raise AntflyException(f"Query failed: {response.error}")
        if response is None:
            raise AntflyException("Query failed")

        return response

    def get(self, table: str, key: str) -> Dict[str, Any]:
        """
        Get a single record by key.

        Args:
            table: Table name
            key: Record key

        Returns:
            Record data

        Raises:
            AntflyException: If lookup fails
        """
        response = lookup_key.sync(
            table_name=table,
            key=key,
            client=cast(AuthenticatedClient, self._client),
        )

        if isinstance(response, Error):
            raise AntflyException(
                f"Failed to get key '{key}' from table '{table}': {response.error}"
            )
        if response is None:
            raise AntflyException(f"Failed to get key '{key}' from table '{table}'")

        return response.to_dict()

    def batch(
        self,
        table: str,
        inserts: Optional[Dict[str, Dict[str, Any]]] = None,
        deletes: Optional[List[str]] = None,
    ) -> None:
        """
        Perform batch operations on a table.

        Args:
            table: Table name
            inserts: Dictionary of key-value pairs to insert
            deletes: List of keys to delete

        Raises:
            AntflyException: If batch operation fails
        """
        request = BatchRequest(
            inserts=cast(BatchRequestInserts, inserts) if inserts is not None else UNSET,
            deletes=deletes or [],
        )

        response = batch_table_operations.sync(
            table_name=table,
            client=cast(AuthenticatedClient, self._client),
            body=request,
        )

        if isinstance(response, Error):
            raise AntflyException(
                f"Batch operation failed for table '{table}': {response.error}"
            )
        if response is None:
            raise AntflyException(f"Batch operation failed for table '{table}'")
