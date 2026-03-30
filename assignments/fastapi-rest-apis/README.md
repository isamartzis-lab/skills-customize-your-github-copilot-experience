# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a small REST API using FastAPI. You will practice designing endpoints, validating data with Pydantic models, and returning meaningful HTTP responses.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Build a FastAPI app that manages a simple list of books. Implement endpoints to list all books, get a single book by ID, and create a new book.

#### Requirements
Completed program should:

- Create a FastAPI app instance and run successfully.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` and return `404` when a book is not found.
- Implement `POST /books` to add a new book with validated input.


### 🛠️	Add Update and Delete Support

#### Description
Extend your API with update and delete functionality, and make sure your API returns clear status codes for success and failure.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return appropriate status codes (`200`, `201`, `204`, `404`, `422`) where relevant.
- Use Pydantic models for request validation and consistent response data.
