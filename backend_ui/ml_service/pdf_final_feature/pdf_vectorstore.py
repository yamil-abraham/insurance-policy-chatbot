from qdrant_client import QdrantClient

from langchain_community.vectorstores.qdrant import Qdrant

from ml_service.tools.embeddings import Embeddings
from utils.config import QDRANT_HOST, QDRANT_PORT


def obtain_vectorstore_from_client(
    embedding_name: str = "openai_embeddings",
    collection_name: str = "final_pdf_feature_1710604034_openai_embeddings"
                                   ) -> Qdrant:

    # `emb = Embeddings()` is creating an instance of the `Embeddings` class. This instance can be
    # used to access methods and properties defined within the `Embeddings` class.
    emb = Embeddings()
    embeddings = emb.obtain_embeddings(embedding_name)
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    qdrant = Qdrant(client, collection_name, embeddings)

    return qdrant
