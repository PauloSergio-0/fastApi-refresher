from fastapi import FastAPI
from data.books import BOOKS

app = FastAPI()

@app.get('/ola')
async def saudar():
    return {"message":"ola"}

@app.get('/books')
async def read_All_dBooks():
    return BOOKS

@app.get('/books/search/{book_title}')
async def searchTitle(book_title: str):
    message = {"message": f"erro"}
    
    for book in BOOKS:
        
        if book_title.casefold() in book['title'].casefold():
            
            if book_title.casefold() == '1984':
                message ={"message": f"O livro {book_title.casefold()} é o meu livro favorito!"}
                break
            else:
                message ={"message": f"O livro {book_title.casefold()} está disponivel"}
                break
        else:
            message ={"message": f"O livro {book_title.casefold()} não está disponivel"}
    
    return message
        
            
@app.get("/books/{book_id}")
def searchBook(book_id):
    return {'message': book_id}

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
