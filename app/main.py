from typing import Optional, List
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import Model
from tweepyHelper import TweepyHelper

class Tweet(BaseModel):
    text: str

class Response(BaseModel):
    class_label: str
  
class Status(BaseModel):
    id: int
    label: str
    full_text: str

class Feed(BaseModel):
    feed: List[Status]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/version")
async def version():
    return {"version": "0.0.3"}

@app.post("/predict",response_model=Response)
async def predict(tweet: Tweet):
    try :
      return {"class_label" : Model.predict([tweet.text])[0]}
    except:
      raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/feed")
async def feed(amount: int):
    if(amount > 30):
      raise HTTPException(status_code=400, detail="Number of tweet exceed the limit")
    try:
      TweepyHelper.getInstance()
      tweets = TweepyHelper.fetchTweet(amount)
      reslut = list(map(lambda x : x['full_text'],tweets))
      prediction = Model.predict(reslut)
      for index in range(len(tweets)):
        tweets[index]['label'] = prediction[index]
      return {"feed":tweets}
    except:
      raise HTTPException(status_code=500, detail="Internal Server Error")