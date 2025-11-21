from enum import Enum


class IndexType(str, Enum):
    AKNN_V0 = "aknn_v0"
    FULL_TEXT_V0 = "full_text_v0"
    GRAPH_V0 = "graph_v0"

    def __str__(self) -> str:
        return str(self.value)
