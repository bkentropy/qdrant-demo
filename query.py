from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

COLLECTION_NAME="packages"

search_result = client.query(
    collection_name=COLLECTION_NAME,
    # query_text="help me build interactive visualizations",
    query_text="plotting functions",
    # filter={
    #     "must": [
    #         {"key": }
    #     ]
    # }
    limit=5,
)

for result in search_result:
    # print(result.metadata["document"])
    print(result.document)

print("Done.")