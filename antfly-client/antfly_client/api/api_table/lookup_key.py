from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.lookup_key_response_200 import LookupKeyResponse200
from ...types import Response


def _get_kwargs(
    table_name: str,
    key: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/table/{table_name}/key/{key}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LookupKeyResponse200]]:
    if response.status_code == 200:
        response_200 = LookupKeyResponse200.from_dict(response.json())

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
) -> Response[Union[Error, LookupKeyResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_name: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, LookupKeyResponse200]]:
    """Lookup a key in a table

    Args:
        table_name (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LookupKeyResponse200]]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table_name: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, LookupKeyResponse200]]:
    """Lookup a key in a table

    Args:
        table_name (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LookupKeyResponse200]
    """

    return sync_detailed(
        table_name=table_name,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    table_name: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Error, LookupKeyResponse200]]:
    """Lookup a key in a table

    Args:
        table_name (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LookupKeyResponse200]]
    """

    kwargs = _get_kwargs(
        table_name=table_name,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_name: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Error, LookupKeyResponse200]]:
    """Lookup a key in a table

    Args:
        table_name (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LookupKeyResponse200]
    """

    return (
        await asyncio_detailed(
            table_name=table_name,
            key=key,
            client=client,
        )
    ).parsed
