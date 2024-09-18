### """
BookListView API View:
- Filtering: Users can filter books by `title`, `author__name`, and `publication_year`.
- Searching: Users can search books by `title` and `author__name`.
- Ordering: Users can order the books by `title` or `publication_year`.

Examples:
- Filter by author name: /api/books/?author__name=Hemingway
- Search by title: /api/books/?search=The%20Old%20Man%20and%20the%20Sea
- Order by publication year: /api/books/?ordering=-publication_year
"""

### """
Unit Tests for Book API:
- Tests cover all CRUD operations for the Book model.
- Filtering, searching, and ordering functionalities are tested to ensure they work as expected.
- Permissions and authentication tests ensure security controls are effective.

How to Run:
- Use `python manage.py test api` to run the test suite.

Expected Outputs:
- All tests should pass without errors, indicating that the API is functioning as expected.
"""
