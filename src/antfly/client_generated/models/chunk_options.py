from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChunkOptions")


@_attrs_define
class ChunkOptions:
    r"""Per-request configuration for chunking. All fields are optional - zero/omitted values use chunker defaults.

    Attributes:
        max_chunks (Union[Unset, int]): Maximum number of chunks to generate per document.
        overlap_tokens (Union[Unset, int]): Number of tokens to overlap between consecutive chunks. Helps maintain
            context across chunk boundaries. Only used by fixed-size chunkers.
        separator (Union[Unset, str]): Separator string for splitting (e.g., '\n\n' for paragraphs). Only used by fixed-
            size chunkers.
        threshold (Union[Unset, float]): Minimum confidence threshold for separator detection (0.0-1.0). Only used by
            ONNX models.
        target_tokens (Union[Unset, int]): Target number of tokens per chunk.
        window_duration_ms (Union[Unset, int]): Window duration in milliseconds for audio chunking (default: 30000).
        overlap_duration_ms (Union[Unset, int]): Overlap duration in milliseconds between audio chunks (default: 0).
    """

    max_chunks: Union[Unset, int] = UNSET
    overlap_tokens: Union[Unset, int] = UNSET
    separator: Union[Unset, str] = UNSET
    threshold: Union[Unset, float] = UNSET
    target_tokens: Union[Unset, int] = UNSET
    window_duration_ms: Union[Unset, int] = UNSET
    overlap_duration_ms: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_chunks = self.max_chunks

        overlap_tokens = self.overlap_tokens

        separator = self.separator

        threshold = self.threshold

        target_tokens = self.target_tokens

        window_duration_ms = self.window_duration_ms

        overlap_duration_ms = self.overlap_duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_chunks is not UNSET:
            field_dict["max_chunks"] = max_chunks
        if overlap_tokens is not UNSET:
            field_dict["overlap_tokens"] = overlap_tokens
        if separator is not UNSET:
            field_dict["separator"] = separator
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if target_tokens is not UNSET:
            field_dict["target_tokens"] = target_tokens
        if window_duration_ms is not UNSET:
            field_dict["window_duration_ms"] = window_duration_ms
        if overlap_duration_ms is not UNSET:
            field_dict["overlap_duration_ms"] = overlap_duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_chunks = d.pop("max_chunks", UNSET)

        overlap_tokens = d.pop("overlap_tokens", UNSET)

        separator = d.pop("separator", UNSET)

        threshold = d.pop("threshold", UNSET)

        target_tokens = d.pop("target_tokens", UNSET)

        window_duration_ms = d.pop("window_duration_ms", UNSET)

        overlap_duration_ms = d.pop("overlap_duration_ms", UNSET)

        chunk_options = cls(
            max_chunks=max_chunks,
            overlap_tokens=overlap_tokens,
            separator=separator,
            threshold=threshold,
            target_tokens=target_tokens,
            window_duration_ms=window_duration_ms,
            overlap_duration_ms=overlap_duration_ms,
        )

        chunk_options.additional_properties = d
        return chunk_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
