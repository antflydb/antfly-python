from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.termite_chunker_config_full_text import TermiteChunkerConfigFullText


T = TypeVar("T", bound="TermiteChunkerConfig")


@_attrs_define
class TermiteChunkerConfig:
    r"""Configuration for the Termite chunking provider.

    Termite is a centralized HTTP service that provides chunking with multi-tier caching.
    The model name maps to ONNX model directory names (similar to how Ollama works).

    **Chunking Models:**
    - fixed: Simple fixed-size chunking by token count (built-in, no ONNX required)
    - Any other name will attempt to load from models/chunkers/{name}/ directory

    **Caching:**
    - L1: Memory cache with 2-minute TTL
    - L2: Persistent Pebble database
    - Singleflight deduplication for concurrent identical requests

        Example:
            {'provider': 'termite', 'api_url': 'http://localhost:8080', 'model': 'fixed', 'target_tokens': 500,
                'overlap_tokens': 50, 'separator': '\n\n', 'max_chunks': 50, 'full_text': {}}

        Attributes:
            model (str): The chunking model to use. Either 'fixed' for simple token-based chunking, or a model name from
                models/chunkers/{name}/. Default: 'fixed'. Example: fixed.
            max_chunks (Union[Unset, int]): Maximum number of chunks to generate per document.
            overlap_tokens (Union[Unset, int]): Number of tokens to overlap between consecutive chunks. Helps maintain
                context across chunk boundaries. Only used by fixed-size chunkers.
            separator (Union[Unset, str]): Separator string for splitting (e.g., '\n\n' for paragraphs). Only used by fixed-
                size chunkers.
            threshold (Union[Unset, float]): Minimum confidence threshold for separator detection (0.0-1.0). Only used by
                ONNX models.
            target_tokens (Union[Unset, int]): Target number of tokens per chunk.
            api_url (Union[Unset, str]): The URL of the Termite API endpoint (e.g., 'http://localhost:8080'). Can also be
                set via ANTFLY_TERMITE_URL environment variable. Example: http://localhost:8080.
            full_text (Union[Unset, TermiteChunkerConfigFullText]): Configuration for full-text indexing of chunks in Bleve.
                When present (even if empty), chunks will be stored with :cft: suffix and indexed in Bleve's _chunks field.
                When absent, chunks use :c: suffix and are only used for vector embeddings.
                This object is reserved for future options like boosting, field mapping, etc.
    """

    model: str = "fixed"
    max_chunks: Union[Unset, int] = UNSET
    overlap_tokens: Union[Unset, int] = UNSET
    separator: Union[Unset, str] = UNSET
    threshold: Union[Unset, float] = UNSET
    target_tokens: Union[Unset, int] = UNSET
    api_url: Union[Unset, str] = UNSET
    full_text: Union[Unset, "TermiteChunkerConfigFullText"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        max_chunks = self.max_chunks

        overlap_tokens = self.overlap_tokens

        separator = self.separator

        threshold = self.threshold

        target_tokens = self.target_tokens

        api_url = self.api_url

        full_text: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.full_text, Unset):
            full_text = self.full_text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
            }
        )
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
        if api_url is not UNSET:
            field_dict["api_url"] = api_url
        if full_text is not UNSET:
            field_dict["full_text"] = full_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.termite_chunker_config_full_text import TermiteChunkerConfigFullText

        d = dict(src_dict)
        model = d.pop("model")

        max_chunks = d.pop("max_chunks", UNSET)

        overlap_tokens = d.pop("overlap_tokens", UNSET)

        separator = d.pop("separator", UNSET)

        threshold = d.pop("threshold", UNSET)

        target_tokens = d.pop("target_tokens", UNSET)

        api_url = d.pop("api_url", UNSET)

        _full_text = d.pop("full_text", UNSET)
        full_text: Union[Unset, TermiteChunkerConfigFullText]
        if isinstance(_full_text, Unset):
            full_text = UNSET
        else:
            full_text = TermiteChunkerConfigFullText.from_dict(_full_text)

        termite_chunker_config = cls(
            model=model,
            max_chunks=max_chunks,
            overlap_tokens=overlap_tokens,
            separator=separator,
            threshold=threshold,
            target_tokens=target_tokens,
            api_url=api_url,
            full_text=full_text,
        )

        termite_chunker_config.additional_properties = d
        return termite_chunker_config

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
