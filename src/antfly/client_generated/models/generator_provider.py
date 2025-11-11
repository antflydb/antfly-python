from enum import Enum


class GeneratorProvider(str, Enum):
    ANTHROPIC = "anthropic"
    BEDROCK = "bedrock"
    GEMINI = "gemini"
    MOCK = "mock"
    OLLAMA = "ollama"
    OPENAI = "openai"
    VERTEX = "vertex"

    def __str__(self) -> str:
        return str(self.value)
