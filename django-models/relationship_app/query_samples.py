from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Sample Queries
if __name__ == "__main__":
    # Query all books by a specific author
    books_by_author = query_all_books_by_author("Author Name")
    print(f"Books by the author: {', '.join([book.title for book in books_by_author])}")

    # List all books in a library
    books_in_library = list_all_books_in_library("Library Name")
    print(f"Books in the library: {', '.join([book.title for book in books_in_library])}")

    # Retrieve the librarian for a library
    librarian = retrieve_librarian_for_library("Library Name")
    print(f"Librarian for the library: {librarian.name}")