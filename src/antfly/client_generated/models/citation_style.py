from enum import Enum


class CitationStyle(str, Enum):
    FOOTNOTE = "footnote"
    INLINE = "inline"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
