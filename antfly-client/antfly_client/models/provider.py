from enum import Enum


class Provider(str, Enum):
    BEDROCK = "bedrock"
    GEMINI = "gemini"
    OLLAMA = "ollama"
    OPENAI = "openai"

    def __str__(self) -> str:
        return str(self.value)
