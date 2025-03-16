#here we handle the fast api logic simple get request 


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chatbot import Chatbot

app = FastAPI()

chat = Chatbot("AIzaSyD9tBP0NaJ6s-vA_qEOwbBtAMu34g1tw9c")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/home')
def home(query : str):
    response = chat.generate(query)
    return {'response' : response}