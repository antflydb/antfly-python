from enum import Enum


class IndexType(str, Enum):
    BLEVE_V2 = "bleve_v2"
    VECTOR_V2 = "vector_v2"

    def __str__(self) -> str:
        return str(self.value)
