from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0)


class Book(BookInput):
    id: int


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "year": 1962},
]

# Task 1: Add GET routes to list books and retrieve a book by ID.
# Task 2: Add POST, PUT, and DELETE routes to manage books.
