from config import load_env
from pdf_loader import load_pdf
from splitter import split
from vectorstore import build_store
from retriever_tool import make_tool
from agent_model import build_agent
from api import create_api


load_env()


def main():

    raw = load_pdf("hrw_world_report_2019.pdf")

    chunks = split(raw)

    retriever = build_store(chunks)

    tool = make_tool(retriever)

    executor = build_agent(tool)

    app = create_api(executor)

    return app


app = main()
