from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


books: list[Book] = [
    Book(id=1, title="The Pragmatic Programmer", author="Andrew Hunt", year=1999),
    Book(id=2, title="Clean Code", author="Robert C. Martin", year=2008),
]


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(book: Book):
    for existing in books:
        if existing.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return book


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, existing in enumerate(books):
        if existing.id == book_id:
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for index, existing in enumerate(books):
        if existing.id == book_id:
            books.pop(index)
            return
    raise HTTPException(status_code=404, detail="Book not found")
