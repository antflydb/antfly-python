from enum import Enum


class ValueType(str, Enum):
    ARRAY = "array"
    BLOB = "blob"
    BOOL = "bool"
    EMBEDDING = "embedding"
    FLOAT = "float"
    GEOPOINT = "geopoint"
    GEOSHAPE = "geoshape"
    INT = "int"
    KEYWORD = "keyword"
    LINK = "link"
    OBJECT = "object"
    STRING = "string"
    TIME = "time"
    UINT = "uint"

    def __str__(self) -> str:
        return str(self.value)
