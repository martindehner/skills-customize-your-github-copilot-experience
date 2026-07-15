import unittest
import importlib.util
from pathlib import Path
from fastapi.testclient import TestClient

MODULE_PATH = Path(__file__).with_name("starter-code.py")
SPEC = importlib.util.spec_from_file_location("starter_code", MODULE_PATH)
starter_code = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(starter_code)

app = starter_code.app
BOOKS = starter_code.BOOKS


class TestBookAPI(unittest.TestCase):
    def setUp(self):
        BOOKS.clear()
        self.client = TestClient(app)

    def test_root_returns_welcome_message(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_create_and_list_books(self):
        payload = {"id": 1, "title": "1984", "author": "George Orwell"}
        create_response = self.client.post("/books", json=payload)
        self.assertEqual(create_response.status_code, 200)

        list_response = self.client.get("/books")
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.json()), 1)

    def test_get_missing_book_returns_404(self):
        response = self.client.get("/books/999")
        self.assertEqual(response.status_code, 404)

    def test_create_book_with_invalid_payload_returns_422(self):
        invalid_payload = {"id": 2, "author": "Unknown"}
        response = self.client.post("/books", json=invalid_payload)
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
