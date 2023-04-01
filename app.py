from fastapi import FastAPI
from pydantic import BaseModel
from src.utils import get_similarity_score


app = FastAPI()


class Sentences(BaseModel):
    sentence1: str
    sentence2: str


@app.get("/")
async def root():
    return {"message": "Go to similarity endpoint to get similarity score"}

@app.post("/similarity")
async def compute_similarity(sentences: Sentences):
    score = get_similarity_score(sentences.sentence1, sentences.sentence2)
    return {"score": score}