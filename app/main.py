from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from model import Model


class Tweet(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/version")
async def version():
    return {"version": "0.0.1"}


@app.post("/predict")
async def predict(tweet: Tweet):
    if Model.getInstance() != None:
      return {"class" : Model.predict(tweet.text)[0]}
    else:
      raise HTTPException(status_code=500, detail="Internal Server Error")
