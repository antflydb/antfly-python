from enum import Enum


class BatchRequestSyncLevel(str, Enum):
    FULL_TEXT = "full_text"
    PROPOSE = "propose"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
