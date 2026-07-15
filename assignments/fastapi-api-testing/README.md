# 📘 Assignment: Testing FastAPI APIs

## 🎯 Objective

Learn how to test FastAPI endpoints using Python's built-in `unittest` framework and FastAPI's `TestClient`. By the end of this assignment, you will write automated tests that verify both successful API behavior and common error cases.

## 📝 Tasks

### 🛠️ Set Up a Testable FastAPI App

#### Description
Create a simple in-memory FastAPI app for managing books so there is a clear target for automated tests. Keep the API small and focused so it can be fully tested in one class period.

#### Requirements
Completed program should:

- Define a FastAPI app in `starter-code.py`.
- Include endpoints: `GET /`, `GET /books`, `POST /books`, and `GET /books/{book_id}`.
- Use an in-memory list to store books (no database and no Docker).
- Return `404` with a clear message when a requested book is missing.

### 🛠️ Write Automated Endpoint Tests

#### Description
Use `unittest` and `TestClient` to verify that the API works as expected. Tests should include both passing scenarios and error handling behavior.

#### Requirements
Completed program should:

- Create tests in `test_api.py` using `unittest.TestCase`.
- Test that `GET /` returns status code `200` and a welcome message.
- Test creating a book with `POST /books` and listing books with `GET /books`.
- Test that requesting a missing book ID returns `404`.

### 🛠️ Strengthen Test Coverage

#### Description
Add at least one validation test to confirm that the API rejects bad input. This helps students understand why automated testing is important for reliability.

#### Requirements
Completed program should:

- Add a test where `POST /books` sends invalid data (for example, missing `title`).
- Confirm that invalid input returns a validation error status (such as `422`).
- Keep tests readable with clear method names and assertions.
- Run all tests and confirm they pass.
