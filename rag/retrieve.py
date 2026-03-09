from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="embeddings/vector_store/chroma_db",
    embedding_function=embeddings
)

def retrieve_logs(query, k=3):
    docs = vectordb.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in docs])
