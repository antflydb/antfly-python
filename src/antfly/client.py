"""Main client interface for Antfly SDK."""

from typing import Any, Optional, Union, cast

from httpx import Timeout

from antfly.client_generated import Client
from antfly.client_generated.api.data_operations import batch_write, lookup_key
from antfly.client_generated.api.table_management import (
    create_table,
    drop_table,
    get_table,
    list_tables,
)
from antfly.client_generated.client import AuthenticatedClient
from antfly.client_generated.models import (
    BatchRequest,
    BatchRequestInserts,
    BatchRequestInsertsAdditionalProperty,
    CreateTableRequest,
    CreateTableRequestIndexes,
    Error,
    Table,
    TableSchema,
    TableStatus,
)
from antfly.client_generated.types import UNSET, Unset

from .exceptions import AntflyException

# Type alias: generated API functions type-hint AuthenticatedClient but work with
# Client too since both have identical interfaces (get_httpx_client, etc.)
# We use Client with basic auth via httpx_args instead of token-based auth.
ApiClient = Union[Client, AuthenticatedClient]


class AntflyClient:
    """High-level client for interacting with Antfly database."""

    _client: ApiClient

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

        httpx_args: dict[str, Any] = {}
        if username and password:
            httpx_args["auth"] = (username, password)

        self._client: ApiClient = Client(
            base_url=self.base_url,
            timeout=Timeout(timeout),
            httpx_args=httpx_args,
        )

    # Table operations

    def create_table(
        self,
        name: str,
        num_shards: Optional[int] = None,
        indexes: Optional[dict[str, Any]] = None,
        schema: Optional[dict[str, Any]] = None,
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
            client=self._client,  # type: ignore[arg-type]
            body=request,
        )

        if isinstance(response, Error):
            raise AntflyException(f"Failed to create table '{name}': {response.error}")
        if response is None:
            raise AntflyException(f"Failed to create table '{name}'")

        return response

    def list_tables(self) -> list[TableStatus]:
        """
        List all tables.

        Returns:
            List of table objects

        Raises:
            AntflyException: If listing tables fails
        """
        response = list_tables.sync(client=self._client)  # type: ignore[arg-type]

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
            client=self._client,  # type: ignore[arg-type]
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
            client=self._client,  # type: ignore[arg-type]
        )

        if isinstance(response, Error):
            raise AntflyException(f"Failed to drop table '{name}': {response.error}")
        if response is None:
            raise AntflyException(f"Failed to drop table '{name}'")

    # Data operations

    def get(self, table: str, key: str) -> dict[str, Any]:
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
            client=self._client,  # type: ignore[arg-type]
        )

        if isinstance(response, Error):
            raise AntflyException(f"Failed to get key '{key}' from table '{table}': {response.error}")
        if response is None:
            raise AntflyException(f"Failed to get key '{key}' from table '{table}'")

        return response.to_dict()

    def batch(
        self,
        table: str,
        inserts: Optional[dict[str, dict[str, Any]]] = None,
        deletes: Optional[list[str]] = None,
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
        # Convert plain dict to proper BatchRequestInserts model
        inserts_model: BatchRequestInserts | Unset = UNSET
        if inserts is not None:
            inserts_model = BatchRequestInserts()
            for key, value in inserts.items():
                prop = BatchRequestInsertsAdditionalProperty()
                prop.additional_properties = value
                inserts_model[key] = prop

        request = BatchRequest(
            inserts=inserts_model,
            deletes=deletes if deletes is not None else UNSET,
        )

        response = batch_write.sync(
            table_name=table,
            client=self._client,  # type: ignore[arg-type]
            body=request,
        )

        if isinstance(response, Error):
            raise AntflyException(f"Batch operation failed for table '{table}': {response.error}")
        if response is None:
            raise AntflyException(f"Batch operation failed for table '{table}'")
