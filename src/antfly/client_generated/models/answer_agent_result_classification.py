from enum import Enum


class AnswerAgentResultClassification(str, Enum):
    QUESTION = "question"
    SEARCH = "search"

    def __str__(self) -> str:
        return str(self.value)
