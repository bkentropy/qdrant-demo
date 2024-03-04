from qdrant_client import QdrantClient

# I couldn't actually connect to the endpoint
import os
# qdrant_api_key = os.getenv("QDRANT_API_KEY")
# qdrant_url = os.getenv("QDRANT_URL")
# client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)

# Much slower, but no setup required
# client = QdrantClient(":memory:")

# Have to use docker, but my favorite setup
client = QdrantClient(url="http://localhost:6333")

from qdrant_client.models import VectorParams, Distance

docs = []
ids = []
with open("./data/packages-for-qdrant.txt") as f:
    count = 0
    for line in f:
        docs.append(line.strip())
        ids.append(count)
        count += 1
assert len(docs) == len(ids)
# print(len(docs))
# print(len(ids))
# print(docs[0])
# print(ids[0])

EMBEDDING_VECTOR_SIZE = len(docs)
COLLECTION_NAME="packages"
# client.recreate_collection(
#    collection_name=COLLECTION_NAME,
#    vectors_config=VectorParams(size=EMBEDDING_VECTOR_SIZE, distance=Distance.COSINE),
# )


# Use the new add method
client.add(
    collection_name=COLLECTION_NAME,
    documents=docs,
    # metadata=metadata,
    ids=ids
)

search_result = client.query(
    collection_name=COLLECTION_NAME,
    query_text="archive"
)
print(search_result)

