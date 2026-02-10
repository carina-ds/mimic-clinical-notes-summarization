
from fastapi import FastAPI
from pydantic import BaseModel
from .service import summarize_text

app = FastAPI(title="Clinical Summarizer (Research)")

class SummarizeRequest(BaseModel):
    text: str
    max_tokens: int = 128

class SummarizeResponse(BaseModel):
    summary: str

@app.post('/summarize', response_model=SummarizeResponse)
async def summarize(req: SummarizeRequest):
    summary = summarize_text(req.text, req.max_tokens)
    return SummarizeResponse(summary=summary)
