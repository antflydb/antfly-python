from enum import Enum


class AntflyType(str, Enum):
    BLOB = "blob"
    BOOL = "bool"
    BOOLEAN = "boolean"
    DATETIME = "datetime"
    EMBEDDING = "embedding"
    FLOAT = "float"
    GEOPOINT = "geopoint"
    GEOSHAPE = "geoshape"
    INT = "int"
    KEYWORD = "keyword"
    LINK = "link"
    NUMERIC = "numeric"
    SEARCH_AS_YOU_TYPE = "search_as_you_type"
    STRING = "string"
    TEXT = "text"
    TIME = "time"
    UINT = "uint"

    def __str__(self) -> str:
        return str(self.value)
