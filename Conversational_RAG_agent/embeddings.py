import time
from openai import RateLimitError
from langchain_openai import AzureOpenAIEmbeddings
from config import load_env

load_env()


class SafeEmbeddings:

    def __init__(self):
        self.emb = AzureOpenAIEmbeddings(
            azure_deployment="text-embedding-ada-002",
            api_version="2023-05-15"
        )

    def embed_documents(self, texts):
        vectors = []
        for t in texts:
            while True:
                try:
                    vectors.append(self.emb.embed_documents([t])[0])
                    break
                except RateLimitError:
                    print("Embedding rate limit hit → retrying in 5s")
                    time.sleep(5)
        return vectors

    def embed_query(self, q):
        while True:
            try:
                return self.emb.embed_query(q)
            except RateLimitError:
                time.sleep(5)
