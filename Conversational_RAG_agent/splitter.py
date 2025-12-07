from langchain.text_splitter import RecursiveCharacterTextSplitter

def split(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200
    )
    return splitter.split_text(text)
