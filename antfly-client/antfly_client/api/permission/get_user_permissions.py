from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.permission import Permission
from ...types import Response


def _get_kwargs(
    user_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/user/{user_name}/permission",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, list["Permission"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Permission.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Error, list["Permission"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, list["Permission"]]]:
    """Get user permissions

     Retrieves all permissions for a specific user.

    Args:
        user_name (str):  Example: johndoe.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['Permission']]]
    """

    kwargs = _get_kwargs(
        user_name=user_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, list["Permission"]]]:
    """Get user permissions

     Retrieves all permissions for a specific user.

    Args:
        user_name (str):  Example: johndoe.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['Permission']]
    """

    return sync_detailed(
        user_name=user_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, list["Permission"]]]:
    """Get user permissions

     Retrieves all permissions for a specific user.

    Args:
        user_name (str):  Example: johndoe.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, list['Permission']]]
    """

    kwargs = _get_kwargs(
        user_name=user_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, list["Permission"]]]:
    """Get user permissions

     Retrieves all permissions for a specific user.

    Args:
        user_name (str):  Example: johndoe.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, list['Permission']]
    """

    return (
        await asyncio_detailed(
            user_name=user_name,
            client=client,
        )
    ).parsed
