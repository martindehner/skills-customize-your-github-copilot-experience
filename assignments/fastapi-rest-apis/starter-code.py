from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int


books = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API assignment"}


@app.post("/books")
def create_book(book: Book):
    # TODO: Add duplicate ID check (optional challenge)
    # TODO: Add the new book to the books list
    # TODO: Return the created book
    pass


@app.get("/books")
def list_books():
    # TODO: Return all books
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return the matching book
    # TODO: Raise HTTPException(status_code=404, detail="Book not found") if missing
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    # TODO: Replace the matching book in the list
    # TODO: Raise 404 if the book does not exist
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the matching book from the list
    # TODO: Return a success message
    # TODO: Raise 404 if the book does not exist
    pass
