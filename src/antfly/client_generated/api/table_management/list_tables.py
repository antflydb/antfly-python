from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.table_status import TableStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    prefix: Union[Unset, str] = UNSET,
    pattern: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["prefix"] = prefix

    params["pattern"] = pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tables",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, list["TableStatus"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TableStatus.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Error, list["TableStatus"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    prefix: Union[Unset, str] = UNSET,
    pattern: Union[Unset, str] = UNSET,
) -> Response[Union[Error, list["TableStatus"]]]:
    """List all tables

    Args:
        prefix (Union[Unset, str]):
        pattern (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['TableStatus']]]
    """

    kwargs = _get_kwargs(
        prefix=prefix,
        pattern=pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    prefix: Union[Unset, str] = UNSET,
    pattern: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, list["TableStatus"]]]:
    """List all tables

    Args:
        prefix (Union[Unset, str]):
        pattern (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['TableStatus']]
    """

    return sync_detailed(
        client=client,
        prefix=prefix,
        pattern=pattern,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    prefix: Union[Unset, str] = UNSET,
    pattern: Union[Unset, str] = UNSET,
) -> Response[Union[Error, list["TableStatus"]]]:
    """List all tables

    Args:
        prefix (Union[Unset, str]):
        pattern (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['TableStatus']]]
    """

    kwargs = _get_kwargs(
        prefix=prefix,
        pattern=pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    prefix: Union[Unset, str] = UNSET,
    pattern: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, list["TableStatus"]]]:
    """List all tables

    Args:
        prefix (Union[Unset, str]):
        pattern (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['TableStatus']]
    """

    return (
        await asyncio_detailed(
            client=client,
            prefix=prefix,
            pattern=pattern,
        )
    ).parsed
