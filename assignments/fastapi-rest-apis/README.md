# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using FastAPI by creating endpoints for creating, reading, updating, and deleting resources. You will practice request handling, validation, and clear API responses.

## 📝 Tasks

### 🛠️ Create a FastAPI App and Data Model

#### Description
Set up a FastAPI project and define a simple resource model for a `Book` object. Use Pydantic to validate request data so invalid input is rejected automatically.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Define a Pydantic model named `Book` with fields: `id` (int), `title` (str), `author` (str), and `published_year` (int).
- Keep an in-memory list to store books.
- Add a root endpoint `GET /` that returns a short welcome message.

### 🛠️ Implement Core REST Endpoints

#### Description
Implement the main CRUD endpoints so users can add books, list all books, and retrieve a single book by ID.

#### Requirements
Completed program should:

- Implement `POST /books` to add a new book.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return a single book by ID.
- Return a 404 error with a clear message when a requested book ID does not exist.

### 🛠️ Add Update and Delete Operations

#### Description
Complete the API by adding update and delete functionality. Confirm that each endpoint returns useful responses for success and failure cases.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to replace an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return a success confirmation message for delete operations.
- Test all endpoints with FastAPI docs at `/docs` or a tool like curl/Postman.
