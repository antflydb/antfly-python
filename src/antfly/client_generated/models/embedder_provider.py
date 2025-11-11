from enum import Enum


class EmbedderProvider(str, Enum):
    BEDROCK = "bedrock"
    GEMINI = "gemini"
    MOCK = "mock"
    OLLAMA = "ollama"
    OPENAI = "openai"
    VERTEX = "vertex"

    def __str__(self) -> str:
        return str(self.value)
