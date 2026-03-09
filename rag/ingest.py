import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def ingest_data():
    df = pd.read_csv("data/raw/telecom_logs.csv")

    documents = []
    for _, row in df.iterrows():
        text = f"""
        Region: {row['Region']}
        Tower ID: {row['Tower_ID']}
        Date: {row['Date']}
        Call Drops: {row['Call_Drops']}
        Signal Strength: {row['Signal_Strength']} dBm
        Congestion Level: {row['Congestion_Level']}
        Handoff Failure: {row['Handoff_Failure']}%
        Notes: {row['Notes']}
        """
        documents.append(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_texts(
        documents,
        embeddings,
        persist_directory="embeddings/vector_store/chroma_db"
    )

    vectordb.persist()
    print("✅ Data ingested and embeddings stored")

if __name__ == "__main__":
    ingest_data()
