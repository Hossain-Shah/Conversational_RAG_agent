from langchain_community.vectorstores import FAISS
from embeddings import SafeEmbeddings

def build_store(chunks):
    emb = SafeEmbeddings()
    store = FAISS.from_texts(chunks, emb)
    retriever = store.as_retriever(search_kwargs={"k":5})
    return retriever
