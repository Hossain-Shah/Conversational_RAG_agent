from langchain.tools import Tool

def make_tool(retriever):

    def retrieve(q):
        docs = retriever.get_relevant_documents(q)
        return "\n\n".join(d.page_content for d in docs)

    return Tool(
        name="pdf_retrieve",
        func=retrieve,
        description="Search PDF and return supporting evidence"
    )
