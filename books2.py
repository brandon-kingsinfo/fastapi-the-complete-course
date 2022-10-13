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
    description: Optional[str] = Field(min_length=1, max_length=200)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "089edac0-4acf-11ed-b878-0242ac120002",
                "title": "example title",
                "author": "example author",
                "description": "description of the book",
                "rating": 7.5
            }
        }


books = []


@app.get("/")
async def get_books(max_books_to_return: Optional[int] = None):
    if len(books) < 1:
        create_books_no_api()
    if max_books_to_return and len(books) >= max_books_to_return > 0:
        index = 0
        books_to_return = []
        while index < max_books_to_return:
            books_to_return.append(books[index])
            index += 1
        return books_to_return
    # not supplying max_books_to_return or max_books_to_return is invalid
    return books


@app.get("/book/{id}")
async def get_book(id: UUID):
    for book in books:
        if book.id == id:
            return book


@app.post("/")
async def create_book(book: Book):
    '''fastapi will expect to receive a book object from request body'''
    books.append(book)

    return book


def create_books_no_api():
    book_1 = Book(id="c6d7993c-4aca-11ed-b878-0242ac120002",
                  title="RIGHTEOUS PREY",
                  author="John Sandford",
                  description="The 32nd book in the Prey series.",
                  rating=6)
    book_2 = Book(id="11c76774-4acb-11ed-b878-0242ac120002",
                  title="VERITY",
                  author="Colleen Hoover",
                  description="Lowen Ashleigh is hired by the husband of an injured writer to complete her popular series and uncovers a horrifying truth.",
                  rating=7)
    book_3 = Book(id="2eb9c99e-4acb-11ed-b878-0242ac120002",
                  title="IT ENDS WITH US",
                  author="Colleen Hoover",
                  description="A battered wife raised in a violent home attempts to halt the cycle of abuse.",
                  rating=8)
    book_4 = Book(id="418fa426-4acb-11ed-b878-0242ac120002",
                  title="MAD HONEY",
                  author="Jodi Picoult and Jennifer Finney Boylan",
                  description="After returning to her hometown, Olivia McAfee’s son gets accused of killing his crush.",
                  rating=5)
    book_5 = Book(id="55654672-4acb-11ed-b878-0242ac120002",
                  title="FAIRY TALE",
                  author="Stephen King",
                  description="A high school kid inherits a shed that is a portal to another world where good and evil are at war.",
                  rating=9)
    books.append(book_1)
    books.append(book_2)
    books.append(book_3)
    books.append(book_4)
    books.append(book_5)


if __name__ == "__main__":
    uvicorn(app)
