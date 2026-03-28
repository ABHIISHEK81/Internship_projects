from langchain_community.document_loaders import WebBaseLoader

def load_documents(urls):
    docs = []
    for url in urls:
        loader = WebBaseLoader(url)
        docs.extend(loader.load())
    return docs
