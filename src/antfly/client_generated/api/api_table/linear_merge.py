from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.linear_merge_request import LinearMergeRequest
from ...models.linear_merge_result import LinearMergeResult
from ...types import Response


def _get_kwargs(
    table_name: str,
    *,
    body: LinearMergeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/table/{table_name}/merge",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LinearMergeResult]]:
    if response.status_code == 200:
        response_200 = LinearMergeResult.from_dict(response.json())

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
) -> Response[Union[Error, LinearMergeResult]]:
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
    body: LinearMergeRequest,
) -> Response[Union[Error, LinearMergeResult]]:
    """Linear merge sorted records from external source

     Performs a stateless linear merge of sorted records from an external source.
    Records are upserted, and any Antfly records in the key range that are absent
    from the input are deleted. Supports progressive pagination for large datasets.

    WARNING: Not safe for concurrent merge operations with overlapping ranges.
    Designed as a sync/import API for single-client use.

    Args:
        table_name (str):
        body (LinearMergeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LinearMergeResult]]
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
    body: LinearMergeRequest,
) -> Optional[Union[Error, LinearMergeResult]]:
    """Linear merge sorted records from external source

     Performs a stateless linear merge of sorted records from an external source.
    Records are upserted, and any Antfly records in the key range that are absent
    from the input are deleted. Supports progressive pagination for large datasets.

    WARNING: Not safe for concurrent merge operations with overlapping ranges.
    Designed as a sync/import API for single-client use.

    Args:
        table_name (str):
        body (LinearMergeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LinearMergeResult]
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
    body: LinearMergeRequest,
) -> Response[Union[Error, LinearMergeResult]]:
    """Linear merge sorted records from external source

     Performs a stateless linear merge of sorted records from an external source.
    Records are upserted, and any Antfly records in the key range that are absent
    from the input are deleted. Supports progressive pagination for large datasets.

    WARNING: Not safe for concurrent merge operations with overlapping ranges.
    Designed as a sync/import API for single-client use.

    Args:
        table_name (str):
        body (LinearMergeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LinearMergeResult]]
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
    body: LinearMergeRequest,
) -> Optional[Union[Error, LinearMergeResult]]:
    """Linear merge sorted records from external source

     Performs a stateless linear merge of sorted records from an external source.
    Records are upserted, and any Antfly records in the key range that are absent
    from the input are deleted. Supports progressive pagination for large datasets.

    WARNING: Not safe for concurrent merge operations with overlapping ranges.
    Designed as a sync/import API for single-client use.

    Args:
        table_name (str):
        body (LinearMergeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LinearMergeResult]
    """

    return (
        await asyncio_detailed(
            table_name=table_name,
            client=client,
            body=body,
        )
    ).parsed
