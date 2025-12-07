from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Chat(BaseModel):
    message: str


def create_api(executor):

    app = FastAPI()

    @app.post("/ask")
    def ask(c: Chat):
        try:
            r = executor.invoke({"input": c.message})
            return {"answer": r["output"]}
        except Exception as e:
            raise HTTPException(500, str(e))

    return app
