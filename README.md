# Antfly Python SDK

Python SDK for [Antfly](https://github.com/antflydb/antfly) - a distributed key-value store and search engine.

## Installation

```bash
pip install antfly-sdk
```

## Quick Start

```python
from antfly import AntflyClient

# Initialize client
client = AntflyClient(
    base_url="http://localhost:8080",
    username="admin",
    password="password"
)

# Create a table
client.create_table(
    name="users",
    num_shards=4,
    schema={
        "key": "user_id",
        "document_types": {
            "user": {
                "fields": {
                    "name": {"type": "string"},
                    "email": {"type": "keyword"},
                    "age": {"type": "int"},
                    "created_at": {"type": "time"}
                }
            }
        }
    }
)

# Insert data
client.batch(
    table="users",
    inserts={
        "user:1": {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30
        },
        "user:2": {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "age": 25
        }
    }
)

# Query data
results = client.query(
    table="users",
    full_text_search={"query": "John"},
    limit=10
)

# Get specific record
user = client.get(table="users", key="user:1")
```

## Features

- **Simple API**: Intuitive interface for all Antfly operations
- **Type Safety**: Full type hints for better IDE support
- **Authentication**: Built-in support for basic authentication
- **Error Handling**: Comprehensive error handling with custom exceptions
- **Auto-generated Client**: Based on OpenAPI specification for accuracy

## Development

### Setup

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -e .[dev]
   ```

### Generate Client

The SDK uses an auto-generated client based on the Antfly OpenAPI specification:

```bash
make generate
```

### Run Tests

```bash
make test
```

### Build Package

```bash
make build
```

## Documentation

Full documentation is available at [https://antfly-sdk-python.readthedocs.io](https://antfly-sdk-python.readthedocs.io)

## License

Apache License 2.0
