from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional
import uvicorn

app = FastAPI()

books = {
    "book_1": {"title": "title1", "author": "author1"},
    "book_2": {"title": "title2", "author": "author2"},
    "book_3": {"title": "title3", "author": "author3"},
    "book_4": {"title": "title4", "author": "author4"},
    "book_5": {"title": "title5", "author": "author5"},
}


@app.get("/")
async def get_books(skip_book: Optional[str] = None):
    '''return all books from the books collection, 
    skip_book is an optional "query parameter"'''
    filtered_books = books.copy()
    if skip_book:
        del filtered_books[skip_book]
        return filtered_books
    return books


@app.get("/book/{book_name}")
async def get_book(book_name: str):
    '''book_name is a required "path parameter"'''
    book = books.get(book_name, None)
    if book is None:
        return JSONResponse(status_code=404, content="cannot find book {}".format(id))
    return book


@app.post("/")
async def create_book(title, author):
    last_id = 0
    if len(books) > 0:
        for book in books:
            id = int(book.split('_')[-1])
            if id > last_id:
                last_id = id

    print(last_id)
    books[f"book_{last_id + 1}"] = {"title": title, "author": author}
    return books[f"book_{last_id + 1}"]


if __name__ == "__main__":
    uvicorn(app)
