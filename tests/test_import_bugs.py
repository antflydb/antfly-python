"""Tests for import and type-related bugs in client.py.

These tests verify that the bugs have been FIXED.
"""

import pytest


class TestBug1FixedImportPaths:
    """Bug #1 Fix: Correct import paths for API modules.

    client.py now correctly imports from data_operations/ and table_management/
    instead of the non-existent api_table module.
    """

    def test_api_table_module_does_not_exist(self):
        """Verify that api_table module still doesn't exist (it never should)."""
        with pytest.raises((ModuleNotFoundError, ImportError)):
            from antfly.client_generated.api import api_table  # type: ignore[attr-defined] # noqa: F401

    def test_batch_write_is_in_data_operations(self):
        """Verify batch_write exists in data_operations."""
        from antfly.client_generated.api.data_operations import batch_write

        assert hasattr(batch_write, "sync")
        assert hasattr(batch_write, "asyncio")

    def test_lookup_key_is_in_data_operations(self):
        """Verify lookup_key exists in data_operations."""
        from antfly.client_generated.api.data_operations import lookup_key

        assert hasattr(lookup_key, "sync")
        assert hasattr(lookup_key, "asyncio")

    def test_table_operations_are_in_table_management(self):
        """Verify table operations exist in table_management."""
        from antfly.client_generated.api.table_management import (
            create_table,
            drop_table,
            get_table,
            list_tables,
        )

        assert hasattr(create_table, "sync")
        assert hasattr(drop_table, "sync")
        assert hasattr(get_table, "sync")
        assert hasattr(list_tables, "sync")

    def test_client_import_succeeds(self):
        """Verify that importing AntflyClient now succeeds."""
        # This should work now that imports are fixed
        from antfly import AntflyClient

        assert AntflyClient is not None

    def test_antfly_client_has_expected_methods(self):
        """Verify AntflyClient has the expected methods."""
        from antfly import AntflyClient

        # Table operations
        assert hasattr(AntflyClient, "create_table")
        assert hasattr(AntflyClient, "list_tables")
        assert hasattr(AntflyClient, "get_table")
        assert hasattr(AntflyClient, "drop_table")

        # Data operations
        assert hasattr(AntflyClient, "get")
        assert hasattr(AntflyClient, "batch")

        # Query method was removed since endpoints don't exist
        assert not hasattr(AntflyClient, "query")


class TestBug2FixedCastMisuse:
    """Bug #2 Fix: Proper BatchRequestInserts model conversion.

    Instead of using cast() which doesn't convert data, the client now
    properly creates BatchRequestInserts and BatchRequestInsertsAdditionalProperty
    model instances from plain dicts.
    """

    def test_cast_does_not_convert_dict_to_model(self):
        """Verify that cast() doesn't convert a plain dict to a model.

        This demonstrates why we can't use cast() and need proper conversion.
        """
        from typing import cast

        from antfly.client_generated.models import BatchRequestInserts

        plain_dict = {"user:1": {"name": "John"}}
        casted = cast(BatchRequestInserts, plain_dict)

        # cast() is just a type hint - the value is still a plain dict
        assert casted is plain_dict
        assert isinstance(casted, dict)
        assert not isinstance(casted, BatchRequestInserts)

    def test_batch_request_to_dict_fails_with_plain_dict_inserts(self):
        """Verify that BatchRequest.to_dict() fails when inserts is a plain dict.

        This demonstrates the bug that existed before the fix.
        """
        from typing import cast

        from antfly.client_generated.models import BatchRequest, BatchRequestInserts

        # This is what the broken client.py used to do
        plain_dict = {"user:1": {"name": "John"}}
        inserts = cast(BatchRequestInserts, plain_dict)

        request = BatchRequest(inserts=inserts, deletes=[])

        # This fails because plain_dict doesn't have to_dict()
        with pytest.raises(AttributeError, match="to_dict"):
            request.to_dict()

    def test_batch_request_works_with_proper_model(self):
        """Verify that BatchRequest.to_dict() works with proper model instances."""
        from antfly.client_generated.models import (
            BatchRequest,
            BatchRequestInserts,
            BatchRequestInsertsAdditionalProperty,
        )

        # Create proper model instances - this is how the fix works
        inserts = BatchRequestInserts()
        prop = BatchRequestInsertsAdditionalProperty()
        prop.additional_properties = {"name": "John"}
        inserts["user:1"] = prop

        request = BatchRequest(inserts=inserts, deletes=[])

        # This works with proper model
        result = request.to_dict()
        assert "inserts" in result
        assert "user:1" in result["inserts"]


class TestBug3FixedMissingQueryEndpoints:
    """Bug #3 Fix: Removed references to non-existent query endpoints.

    The query_table and global_query endpoints don't exist in the generated code.
    The query method has been removed from AntflyClient since it can't work.
    """

    def test_query_table_does_not_exist(self):
        """Verify query_table doesn't exist anywhere."""
        with pytest.raises((ModuleNotFoundError, ImportError)):
            from antfly.client_generated.api.api_table import query_table  # type: ignore[import-not-found] # noqa: F401

    def test_global_query_does_not_exist(self):
        """Verify global_query doesn't exist anywhere."""
        with pytest.raises((ModuleNotFoundError, ImportError)):
            from antfly.client_generated.api.api_table import (
                global_query,  # type: ignore[import-not-found] # noqa: F401
            )

    def test_query_request_model_does_not_exist(self):
        """Verify QueryRequest model doesn't exist."""
        with pytest.raises(ImportError):
            from antfly.client_generated.models import QueryRequest  # type: ignore[attr-defined] # noqa: F401

    def test_query_request_full_text_search_model_does_not_exist(self):
        """Verify QueryRequestFullTextSearch model doesn't exist."""
        with pytest.raises(ImportError):
            from antfly.client_generated.models import (
                QueryRequestFullTextSearch,  # type: ignore[attr-defined] # noqa: F401
            )

    def test_antfly_client_query_method_removed(self):
        """Verify that AntflyClient no longer has a query method."""
        from antfly import AntflyClient

        # The query method was removed since it relied on non-existent endpoints
        assert not hasattr(AntflyClient, "query")


class TestBug4FixedTypeMismatch:
    """Bug #4 Fix: Type mismatch with Client vs AuthenticatedClient.

    The generated API functions type-hint AuthenticatedClient but work with
    Client too since both have identical interfaces. We use a type alias and
    type: ignore comments to document this intentional usage.
    """

    def test_client_and_authenticated_client_have_same_interface(self):
        """Verify both client types have the same interface."""
        from antfly.client_generated.client import AuthenticatedClient, Client

        # Both should have get_httpx_client method
        assert hasattr(Client, "get_httpx_client")
        assert hasattr(AuthenticatedClient, "get_httpx_client")

        # Both should have get_async_httpx_client method
        assert hasattr(Client, "get_async_httpx_client")
        assert hasattr(AuthenticatedClient, "get_async_httpx_client")

    def test_api_client_type_alias_exists(self):
        """Verify ApiClient type alias is defined."""
        from typing import get_args

        from antfly.client import ApiClient
        from antfly.client_generated.client import AuthenticatedClient, Client

        # ApiClient should be Union[Client, AuthenticatedClient]
        args = get_args(ApiClient)
        assert Client in args
        assert AuthenticatedClient in args


class TestBatchWriteHttpStatus:
    """Test that batch_write accepts both HTTP 200 and 201."""

    def test_batch_write_parse_response_accepts_200(self):
        """Verify batch_write._parse_response accepts HTTP 200."""
        from unittest.mock import MagicMock

        from antfly.client_generated import Client
        from antfly.client_generated.api.data_operations import batch_write

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}

        mock_client = MagicMock(spec=Client)

        result = batch_write._parse_response(client=mock_client, response=mock_response)
        assert result is not None

    def test_batch_write_parse_response_accepts_201(self):
        """Verify batch_write._parse_response accepts HTTP 201."""
        from unittest.mock import MagicMock

        from antfly.client_generated import Client
        from antfly.client_generated.api.data_operations import batch_write

        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {}

        mock_client = MagicMock(spec=Client)

        result = batch_write._parse_response(client=mock_client, response=mock_response)
        assert result is not None


class TestClientIntegration:
    """Integration tests for the fixed AntflyClient."""

    def test_client_instantiation(self):
        """Test that AntflyClient can be instantiated."""
        from antfly import AntflyClient

        client = AntflyClient(base_url="http://localhost:8080")
        assert client.base_url == "http://localhost:8080"
        assert client._client is not None

    def test_client_with_auth(self):
        """Test that AntflyClient can be instantiated with auth."""
        from antfly import AntflyClient

        client = AntflyClient(
            base_url="http://localhost:8080/",
            username="admin",
            password="secret",
        )
        assert client.base_url == "http://localhost:8080"
