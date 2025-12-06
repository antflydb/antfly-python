from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.antfly_chunker_config_full_text import AntflyChunkerConfigFullText


T = TypeVar("T", bound="AntflyChunkerConfig")


@_attrs_define
class AntflyChunkerConfig:
    r"""Configuration for the local Antfly chunking provider.

    This provider runs chunking directly within the storage node process,
    without requiring an external Termite service. It uses simple fixed-size
    tokenizer-based chunking with no caching overhead.

    **Use this when:**
    - Running single-node deployments (swarm mode)
    - You don't need embedding/chunk caching across nodes
    - You want minimal setup complexity

    **Use Termite instead when:**
    - Running multi-node clusters where caching reduces costs
    - You need ONNX-accelerated chunking models
    - You want persistent chunk/embedding caches

        Example:
            {'provider': 'antfly', 'target_tokens': 500, 'overlap_tokens': 50, 'separator': '\n\n', 'max_chunks': 50}

        Attributes:
            target_tokens (Union[Unset, int]): Target number of tokens per chunk. Chunker will aim for chunks around this
                size. Default: 500.
            overlap_tokens (Union[Unset, int]): Number of tokens to overlap between consecutive chunks. Helps maintain
                context across chunk boundaries. Default: 50.
            separator (Union[Unset, str]): Separator string for splitting (e.g., '\n\n' for paragraphs). Default: '\n\n'.
            max_chunks (Union[Unset, int]): Maximum number of chunks to generate per document. Prevents excessive chunking
                of very large documents. Default: 50.
            full_text (Union[Unset, AntflyChunkerConfigFullText]): Configuration for full-text indexing of chunks in Bleve.
                When present (even if empty), chunks will be stored with :cft: suffix and indexed in Bleve's _chunks field.
                When absent, chunks use :c: suffix and are only used for vector embeddings.
                This object is reserved for future options like boosting, field mapping, etc.
    """

    target_tokens: Union[Unset, int] = 500
    overlap_tokens: Union[Unset, int] = 50
    separator: Union[Unset, str] = "\n\n"
    max_chunks: Union[Unset, int] = 50
    full_text: Union[Unset, "AntflyChunkerConfigFullText"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_tokens = self.target_tokens

        overlap_tokens = self.overlap_tokens

        separator = self.separator

        max_chunks = self.max_chunks

        full_text: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.full_text, Unset):
            full_text = self.full_text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_tokens is not UNSET:
            field_dict["target_tokens"] = target_tokens
        if overlap_tokens is not UNSET:
            field_dict["overlap_tokens"] = overlap_tokens
        if separator is not UNSET:
            field_dict["separator"] = separator
        if max_chunks is not UNSET:
            field_dict["max_chunks"] = max_chunks
        if full_text is not UNSET:
            field_dict["full_text"] = full_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.antfly_chunker_config_full_text import AntflyChunkerConfigFullText

        d = dict(src_dict)
        target_tokens = d.pop("target_tokens", UNSET)

        overlap_tokens = d.pop("overlap_tokens", UNSET)

        separator = d.pop("separator", UNSET)

        max_chunks = d.pop("max_chunks", UNSET)

        _full_text = d.pop("full_text", UNSET)
        full_text: Union[Unset, AntflyChunkerConfigFullText]
        if isinstance(_full_text, Unset):
            full_text = UNSET
        else:
            full_text = AntflyChunkerConfigFullText.from_dict(_full_text)

        antfly_chunker_config = cls(
            target_tokens=target_tokens,
            overlap_tokens=overlap_tokens,
            separator=separator,
            max_chunks=max_chunks,
            full_text=full_text,
        )

        antfly_chunker_config.additional_properties = d
        return antfly_chunker_config

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
