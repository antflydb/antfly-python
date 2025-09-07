#!/usr/bin/env python3
"""Advanced search examples for Antfly SDK."""

from antfly import AntflyClient


def main():
    """Demonstrate advanced search features."""
    
    client = AntflyClient(
        base_url="http://localhost:8080",
        username="admin",
        password="password"
    )
    
    # Prepare sample data
    print("Setting up sample data...")
    
    # Create articles table with vector index
    client.create_table(
        name="articles",
        num_shards=2,
        indexes={
            "content_embedding": {
                "dimension": 384,
                "embedder_config": {
                    "provider": "openai",
                    "model": "text-embedding-3-small"
                }
            }
        },
        schema={
            "key": "article_id",
            "document_types": {
                "article": {
                    "fields": {
                        "title": {"type": "string"},
                        "content": {"type": "string"},
                        "author": {"type": "keyword"},
                        "tags": {"type": "array"},
                        "published_date": {"type": "time"},
                        "views": {"type": "int"}
                    }
                }
            }
        }
    )
    
    # Insert articles
    client.batch(
        table="articles",
        inserts={
            "article:001": {
                "title": "Introduction to Machine Learning",
                "content": "Machine learning is a subset of artificial intelligence...",
                "author": "john.doe",
                "tags": ["ml", "ai", "tutorial"],
                "published_date": "2024-01-15T10:00:00Z",
                "views": 1500
            },
            "article:002": {
                "title": "Deep Learning Fundamentals",
                "content": "Deep learning uses neural networks with multiple layers...",
                "author": "jane.smith",
                "tags": ["dl", "neural-networks", "ai"],
                "published_date": "2024-02-20T14:30:00Z",
                "views": 2300
            },
            "article:003": {
                "title": "Natural Language Processing Basics",
                "content": "NLP enables computers to understand human language...",
                "author": "john.doe",
                "tags": ["nlp", "ai", "text-processing"],
                "published_date": "2024-03-10T09:15:00Z",
                "views": 890
            }
        }
    )
    
    # Full-text search
    print("\n1. Full-text search for 'neural networks':")
    results = client.query(
        table="articles",
        full_text_search={
            "query": "neural networks",
            "fields": ["title", "content"]
        },
        limit=5
    )
    print_results(results)
    
    # Faceted search
    print("\n2. Search with facets (aggregations):")
    results = client.query(
        table="articles",
        full_text_search={"query": "ai"},
        facets={
            "authors": {
                "field": "author",
                "size": 10
            },
            "tags": {
                "field": "tags",
                "size": 20
            }
        },
        limit=10
    )
    print_results(results)
    if results.facets:
        print("  Facets:")
        for facet_name, facet_data in results.facets.items():
            print(f"    {facet_name}:")
            if facet_data.terms:
                for term in facet_data.terms:
                    print(f"      - {term.term}: {term.count}")
    
    # Range queries
    print("\n3. Articles with high view count (>1000):")
    results = client.query(
        table="articles",
        filter_query={
            "range": {
                "views": {
                    "min": 1000
                }
            }
        },
        order_by={"views": False},  # Descending order
        limit=10
    )
    print_results(results)
    
    # Semantic search (if embeddings are configured)
    print("\n4. Semantic search for similar content:")
    results = client.query(
        table="articles",
        semantic_search="How do computers understand human language?",
        indexes=["content_embedding"],
        limit=3
    )
    print_results(results)
    
    # Combined search (hybrid)
    print("\n5. Hybrid search (full-text + semantic):")
    results = client.query(
        table="articles",
        full_text_search={"query": "machine learning"},
        semantic_search="practical applications of AI",
        indexes=["content_embedding"],
        limit=5
    )
    print_results(results)
    
    # Clean up
    print("\nCleaning up...")
    client.drop_table("articles")
    print("Done!")


def print_results(results):
    """Helper to print search results."""
    if results.hits and results.hits.hits:
        print(f"  Found {results.hits.total} results:")
        for i, hit in enumerate(results.hits.hits, 1):
            print(f"    {i}. {hit.source.get('title')} (score: {hit.score:.3f})")
            print(f"       Author: {hit.source.get('author')}, Views: {hit.source.get('views')}")
    else:
        print("  No results found")


if __name__ == "__main__":
    main()
