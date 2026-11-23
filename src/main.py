from fastapi import FastAPI
from data.books import BOOKS

app = FastAPI()

@app.get('/ola')
async def saudar():
    return {"message":"ola"}

@app.get('/books')
async def read_All_dBooks():
    return BOOKS

#fastapi dev src/main.py
#if __name__ == "__main__":
