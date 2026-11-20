class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)
        print(title, "added successfully.")

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(title, "removed successfully.")
        else:
            print(title, "not found.")

    def list_books(self):
        if self.__books:
            print("Available Books:")
            for book in self.__books:
                print(book)
        else:
            print("No books available.")


# Creating Library object
lib = Library()

# Adding books
lib.add_book("Python Programming")
lib.add_book("Java Programming")
lib.add_book("C Programming")

# Display books
lib.list_books()

# Removing a book
lib.remove_book("Java Programming")

# Display updated books
lib.list_books()