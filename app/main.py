from typing import Optional
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import Model


class Tweet(BaseModel):
    text: str

class Response(BaseModel):
    "class": str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/version")
async def version():
    return {"version": "0.0.2"}

@app.post("/predict",response_model=Response)
async def predict(tweet: Tweet):
    if Model.getInstance() != None:
      return {"class" : Model.predict(tweet.text)[0]}
    else:
      raise HTTPException(status_code=500, detail="Internal Server Error")
