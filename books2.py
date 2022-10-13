from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: Optional[str] = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)


books = []


@app.get("/")
async def get_books():
    return books


@app.post("/")
async def create_book(book: Book):
    '''fastapi will expect to receive a book object from request body'''
    books.append(book)

    return book


if __name__ == "__main__":
    uvicorn(app)
