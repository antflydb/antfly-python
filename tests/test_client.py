"""Tests for Antfly client."""

import sys
from unittest.mock import Mock, patch, MagicMock

import pytest
from httpx import Timeout

# Mock the generated client modules before importing antfly
sys.modules["antfly_client"] = MagicMock()
sys.modules["antfly_client.api"] = MagicMock()
sys.modules["antfly_client.api.api_table"] = MagicMock()
sys.modules["antfly_client.api.api_index"] = MagicMock()
sys.modules["antfly_client.models"] = MagicMock()

from antfly import AntflyClient, AntflyException  # noqa: E402
from antfly.client_generated.types import UNSET  # noqa: E402


class TestAntflyClient:
    """Test cases for AntflyClient."""

    @patch("antfly.client.Client")
    def test_client_initialization(self, mock_client):
        """Test client initialization with and without auth."""
        # Without auth
        client = AntflyClient(base_url="http://localhost:8080")
        assert client.base_url == "http://localhost:8080"
        mock_client.assert_called_once_with(
            base_url="http://localhost:8080",
            timeout=Timeout(30.0),
            httpx_args={},
        )

        # With auth
        mock_client.reset_mock()
        client = AntflyClient(base_url="http://localhost:8080/", username="admin", password="password")
        assert client.base_url == "http://localhost:8080"
        mock_client.assert_called_once_with(
            base_url="http://localhost:8080",
            timeout=Timeout(30.0),
            httpx_args={"auth": ("admin", "password")},
        )

    @patch("antfly.client.Client")
    @patch("antfly.client.list_tables")
    def test_list_tables(self, mock_list_tables, mock_client_class):
        """Test listing tables."""
        # Setup mock
        mock_list_tables.sync.return_value = []

        client = AntflyClient(base_url="http://localhost:8080")
        tables = client.list_tables()

        assert tables == []
        mock_list_tables.sync.assert_called_once_with(client=client._client)

    @patch("antfly.client.Client")
    @patch("antfly.client.create_table")
    @patch("antfly.client.CreateTableRequest")
    def test_create_table(self, mock_request_class, mock_create_table, mock_client_class):
        """Test creating a table."""
        # Setup mocks
        mock_table = Mock()
        mock_table.name = "test_table"
        mock_create_table.sync.return_value = mock_table

        client = AntflyClient(base_url="http://localhost:8080")
        result = client.create_table(name="test_table", num_shards=2)

        assert result.name == "test_table"
        mock_request_class.assert_called_once_with(num_shards=2, indexes=UNSET, schema=UNSET)
        mock_create_table.sync.assert_called_once()

    @patch("antfly.client.Client")
    @patch("antfly.client.lookup_key")
    def test_get_record(self, mock_lookup_key, mock_client_class):
        """Test getting a record by key."""
        # Setup mock
        mock_response = Mock()
        mock_response.to_dict.return_value = {"name": "John Doe"}
        mock_lookup_key.sync.return_value = mock_response

        client = AntflyClient(base_url="http://localhost:8080")
        record = client.get(table="users", key="user:1")

        assert record == {"name": "John Doe"}
        mock_lookup_key.sync.assert_called_once_with(table_name="users", key="user:1", client=client._client)

    @patch("antfly.client.Client")
    @patch("antfly.client.lookup_key")
    def test_get_record_failure(self, mock_lookup_key, mock_client_class):
        """Test handling of get record failure."""
        # Setup mock to return None (failure)
        mock_lookup_key.sync.return_value = None

        client = AntflyClient(base_url="http://localhost:8080")

        with pytest.raises(AntflyException) as exc_info:
            client.get(table="users", key="user:1")

        assert "Failed to get key 'user:1' from table 'users'" in str(exc_info.value)
