
class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {
            "title": title,
            "author": author
        }

        self.books.append(book)
        print(f"Book '{title}' is added.")

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' is removed.")
                return

        print(f"Book '{title}' not found.")

    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book

        return None

    def show_books(self):
        if not self.books:
            print("Library is empty.")
            return

        for book in self.books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print("--------------------")
