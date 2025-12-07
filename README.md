# Conversational_RAG_agent

## Purpose:
- Respond to user using RAG with agentic AI approach

## Procedure:
```bash
python -m venv env_name
```
```bash
env_name\Scripts\activate.bat
```
```bash
pip install -r requirements.txt
```
```bash
uvicorn app:app --reload
```

## Dependency:
- agent_model.py deals as Q/A agent
- api.py is based on API part
- app.py is functionalized agentic workflow
- config.py is containing dependencies
- embeddings.py deals as embedding response
- pdf_loader.py deals as file reader
- retriever_tool.py deals as retriever portion
- splitter.py is functionalized with document character splitting
- vectorstore.py is equipped with vectordb storage part

## Technology:
- FastAPI
- pydantic
- langchain
- openai
- fitz
