from fastapi import FastAPI
from data.books import BOOKS

app = FastAPI()

@app.get('/ola')
async def saudar():
    return {"message":"ola"}

@app.get('/books')
async def read_All_dBooks():
    return BOOKS

@app.post("/username")
def username(username):
    
    return {"user": f"Usuário é {username}"}


@app.put('/update')
def update(valor: int):
    idade = 90
    idade = valor
    return {"message": f"Sua idade é {idade}"}

@app.delete('/delete')
def apagar(idLoja: int):
    
    return{"message": f"Loja com o id {idLoja} foi deletada"}


#fastapi dev src/main.py
#if __name__ == "__main__":
