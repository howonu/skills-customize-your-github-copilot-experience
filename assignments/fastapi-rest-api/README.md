# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small book-library REST API with FastAPI. Practice defining API routes, using Pydantic models for request data, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create the API and Read Books

#### Description
Use the provided starter code to create a FastAPI application for a book library. Add endpoints that let a client list all books and retrieve one book by its ID.

Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, then run the application with `uvicorn main:app --reload`. Open `http://127.0.0.1:8000/docs` to try the endpoints.

#### Requirements
Completed program should:

- Create a FastAPI application using the provided `app` instance
- Implement `GET /books` to return all books as JSON
- Implement `GET /books/{book_id}` to return a matching book, or HTTP 404 when its ID does not exist


### 🛠️ Add, Update, and Delete Books

#### Description
Extend the API so clients can manage the library. Use the provided Pydantic model to validate book details sent in request bodies.

#### Requirements
Completed program should:

- Implement `POST /books` to add a book and return it with a unique ID and HTTP 201
- Implement `PUT /books/{book_id}` to replace a book's details, or return HTTP 404 when its ID does not exist
- Implement `DELETE /books/{book_id}` to remove a book and return HTTP 204, or HTTP 404 when its ID does not exist
- Reject empty titles or authors and years below zero using request validation
