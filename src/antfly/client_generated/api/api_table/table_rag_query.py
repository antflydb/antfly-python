from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.rag_request import RAGRequest
from ...types import Response


def _get_kwargs(
    table_name: str,
    *,
    body: RAGRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/table/{table_name}/rag",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, str]]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient,
    body: RAGRequest,
) -> Response[Union[Error, str]]:
    """Perform RAG query on a specific table

     Executes a RAG query on a specific table and streams a summary of the results using the specified
    summarizer. The response is streamed as Server-Sent Events (SSE) for real-time updates or returns
    JSON with citations.

    Args:
        table_name (str):
        body (RAGRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, str]]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table_name: str,
    *,
    client: AuthenticatedClient,
    body: RAGRequest,
) -> Optional[Union[Error, str]]:
    """Perform RAG query on a specific table

     Executes a RAG query on a specific table and streams a summary of the results using the specified
    summarizer. The response is streamed as Server-Sent Events (SSE) for real-time updates or returns
    JSON with citations.

    Args:
        table_name (str):
        body (RAGRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, str]
    """

    return sync_detailed(
        table_name=table_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    table_name: str,
    *,
    client: AuthenticatedClient,
    body: RAGRequest,
) -> Response[Union[Error, str]]:
    """Perform RAG query on a specific table

     Executes a RAG query on a specific table and streams a summary of the results using the specified
    summarizer. The response is streamed as Server-Sent Events (SSE) for real-time updates or returns
    JSON with citations.

    Args:
        table_name (str):
        body (RAGRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, str]]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_name: str,
    *,
    client: AuthenticatedClient,
    body: RAGRequest,
) -> Optional[Union[Error, str]]:
    """Perform RAG query on a specific table

     Executes a RAG query on a specific table and streams a summary of the results using the specified
    summarizer. The response is streamed as Server-Sent Events (SSE) for real-time updates or returns
    JSON with citations.

    Args:
        table_name (str):
        body (RAGRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, str]
    """

    return (
        await asyncio_detailed(
            table_name=table_name,
            client=client,
            body=body,
        )
    ).parsed
