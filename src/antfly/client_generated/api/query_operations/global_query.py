from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.query_request import QueryRequest
from ...models.query_responses import QueryResponses
from ...types import Response


def _get_kwargs(
    *,
    body: QueryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, QueryResponses]]:
    if response.status_code == 200:
        response_200 = QueryResponses.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, QueryResponses]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
) -> Response[Union[Error, QueryResponses]]:
    r"""Perform a global query

     Executes a query across all relevant tables and shards based on the query content.

    ## Query Examples

    **Full-text search:**
    ```json
    {
      \"table\": \"wikipedia\",
      \"full_text_search\": {\"query\": \"body:computer\"},
      \"limit\": 10
    }
    ```

    **Semantic search:**
    ```json
    {
      \"table\": \"articles\",
      \"semantic_search\": \"artificial intelligence applications\",
      \"indexes\": [\"title_body_embedding\"],
      \"limit\": 20
    }
    ```

    **Hybrid search (RRF):**
    ```json
    {
      \"table\": \"products\",
      \"full_text_search\": {\"query\": \"laptop gaming\"},
      \"semantic_search\": \"high performance gaming computers\",
      \"indexes\": [\"product_embedding\"],
      \"filter_query\": {\"query\": \"price:<2000 AND in_stock:true\"},
      \"fields\": [\"name\", \"price\", \"description\"],
      \"limit\": 15
    }
    ```

    **With filtering:**
    ```json
    {
      \"table\": \"users\",
      \"filter_prefix\": \"tenant:acme:\",
      \"full_text_search\": {\"query\": \"active:true\"},
      \"exclusion_query\": {\"query\": \"status:deleted\"},
      \"limit\": 50
    }
    ```

    **NDJSON format:**
    For bulk queries, send multiple queries as NDJSON with `Content-Type: application/x-ndjson`.
    Each line must end with `\n`:
    ```
    {\"table\":\"wiki\",\"semantic_search\":\"AI\",\"indexes\":[\"emb\"],\"limit\":5}
    {\"table\":\"docs\",\"full_text_search\":{\"query\":\"tutorial\"},\"limit\":10}
    ```

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, QueryResponses]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
) -> Optional[Union[Error, QueryResponses]]:
    r"""Perform a global query

     Executes a query across all relevant tables and shards based on the query content.

    ## Query Examples

    **Full-text search:**
    ```json
    {
      \"table\": \"wikipedia\",
      \"full_text_search\": {\"query\": \"body:computer\"},
      \"limit\": 10
    }
    ```

    **Semantic search:**
    ```json
    {
      \"table\": \"articles\",
      \"semantic_search\": \"artificial intelligence applications\",
      \"indexes\": [\"title_body_embedding\"],
      \"limit\": 20
    }
    ```

    **Hybrid search (RRF):**
    ```json
    {
      \"table\": \"products\",
      \"full_text_search\": {\"query\": \"laptop gaming\"},
      \"semantic_search\": \"high performance gaming computers\",
      \"indexes\": [\"product_embedding\"],
      \"filter_query\": {\"query\": \"price:<2000 AND in_stock:true\"},
      \"fields\": [\"name\", \"price\", \"description\"],
      \"limit\": 15
    }
    ```

    **With filtering:**
    ```json
    {
      \"table\": \"users\",
      \"filter_prefix\": \"tenant:acme:\",
      \"full_text_search\": {\"query\": \"active:true\"},
      \"exclusion_query\": {\"query\": \"status:deleted\"},
      \"limit\": 50
    }
    ```

    **NDJSON format:**
    For bulk queries, send multiple queries as NDJSON with `Content-Type: application/x-ndjson`.
    Each line must end with `\n`:
    ```
    {\"table\":\"wiki\",\"semantic_search\":\"AI\",\"indexes\":[\"emb\"],\"limit\":5}
    {\"table\":\"docs\",\"full_text_search\":{\"query\":\"tutorial\"},\"limit\":10}
    ```

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, QueryResponses]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
) -> Response[Union[Error, QueryResponses]]:
    r"""Perform a global query

     Executes a query across all relevant tables and shards based on the query content.

    ## Query Examples

    **Full-text search:**
    ```json
    {
      \"table\": \"wikipedia\",
      \"full_text_search\": {\"query\": \"body:computer\"},
      \"limit\": 10
    }
    ```

    **Semantic search:**
    ```json
    {
      \"table\": \"articles\",
      \"semantic_search\": \"artificial intelligence applications\",
      \"indexes\": [\"title_body_embedding\"],
      \"limit\": 20
    }
    ```

    **Hybrid search (RRF):**
    ```json
    {
      \"table\": \"products\",
      \"full_text_search\": {\"query\": \"laptop gaming\"},
      \"semantic_search\": \"high performance gaming computers\",
      \"indexes\": [\"product_embedding\"],
      \"filter_query\": {\"query\": \"price:<2000 AND in_stock:true\"},
      \"fields\": [\"name\", \"price\", \"description\"],
      \"limit\": 15
    }
    ```

    **With filtering:**
    ```json
    {
      \"table\": \"users\",
      \"filter_prefix\": \"tenant:acme:\",
      \"full_text_search\": {\"query\": \"active:true\"},
      \"exclusion_query\": {\"query\": \"status:deleted\"},
      \"limit\": 50
    }
    ```

    **NDJSON format:**
    For bulk queries, send multiple queries as NDJSON with `Content-Type: application/x-ndjson`.
    Each line must end with `\n`:
    ```
    {\"table\":\"wiki\",\"semantic_search\":\"AI\",\"indexes\":[\"emb\"],\"limit\":5}
    {\"table\":\"docs\",\"full_text_search\":{\"query\":\"tutorial\"},\"limit\":10}
    ```

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, QueryResponses]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
) -> Optional[Union[Error, QueryResponses]]:
    r"""Perform a global query

     Executes a query across all relevant tables and shards based on the query content.

    ## Query Examples

    **Full-text search:**
    ```json
    {
      \"table\": \"wikipedia\",
      \"full_text_search\": {\"query\": \"body:computer\"},
      \"limit\": 10
    }
    ```

    **Semantic search:**
    ```json
    {
      \"table\": \"articles\",
      \"semantic_search\": \"artificial intelligence applications\",
      \"indexes\": [\"title_body_embedding\"],
      \"limit\": 20
    }
    ```

    **Hybrid search (RRF):**
    ```json
    {
      \"table\": \"products\",
      \"full_text_search\": {\"query\": \"laptop gaming\"},
      \"semantic_search\": \"high performance gaming computers\",
      \"indexes\": [\"product_embedding\"],
      \"filter_query\": {\"query\": \"price:<2000 AND in_stock:true\"},
      \"fields\": [\"name\", \"price\", \"description\"],
      \"limit\": 15
    }
    ```

    **With filtering:**
    ```json
    {
      \"table\": \"users\",
      \"filter_prefix\": \"tenant:acme:\",
      \"full_text_search\": {\"query\": \"active:true\"},
      \"exclusion_query\": {\"query\": \"status:deleted\"},
      \"limit\": 50
    }
    ```

    **NDJSON format:**
    For bulk queries, send multiple queries as NDJSON with `Content-Type: application/x-ndjson`.
    Each line must end with `\n`:
    ```
    {\"table\":\"wiki\",\"semantic_search\":\"AI\",\"indexes\":[\"emb\"],\"limit\":5}
    {\"table\":\"docs\",\"full_text_search\":{\"query\":\"tutorial\"},\"limit\":10}
    ```

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, QueryResponses]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
