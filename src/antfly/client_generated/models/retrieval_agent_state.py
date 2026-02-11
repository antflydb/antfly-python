from enum import Enum


class RetrievalAgentState(str, Enum):
    AWAITING_CLARIFICATION = "awaiting_clarification"
    COMPLETE = "complete"
    TOOL_CALLING = "tool_calling"

    def __str__(self) -> str:
        return str(self.value)
