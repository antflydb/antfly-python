from enum import Enum


class MergeStrategy(str, Enum):
    FAILOVER = "failover"
    RRF = "rrf"

    def __str__(self) -> str:
        return str(self.value)
