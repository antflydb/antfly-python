from enum import Enum


class ChatToolName(str, Enum):
    ADD_FILTER = "add_filter"
    ASK_CLARIFICATION = "ask_clarification"
    FETCH = "fetch"
    SEARCH = "search"
    WEBSEARCH = "websearch"

    def __str__(self) -> str:
        return str(self.value)
