from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str


BOOKS = []


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI testing assignment"}


@app.get("/books")
def list_books():
    return BOOKS


@app.post("/books")
def create_book(book: Book):
    BOOKS.append(book.dict())
    return book


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
