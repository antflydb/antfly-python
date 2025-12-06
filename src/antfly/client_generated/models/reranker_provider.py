from enum import Enum


class RerankerProvider(str, Enum):
    COHERE = "cohere"
    OLLAMA = "ollama"
    TERMITE = "termite"
    VERTEX = "vertex"

    def __str__(self) -> str:
        return str(self.value)
