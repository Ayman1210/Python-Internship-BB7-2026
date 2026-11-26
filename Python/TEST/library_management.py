class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)

        if self.is_available:
            print("Status: Available")
        else:
            print("Status: Issued")



class Library:

    def __init__(self):
        self.books = []

    
    def add_book(self, book):

        for b in self.books:
            if b.book_id == book.book_id:
                print("Error: Book ID already exists!")
                return

        self.books.append(book)
        print("Book added successfully!")


    def view_books(self):

        if len(self.books) == 0:
            print("No books available in library.")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books:
            book.display_book()
            print("-------------------------------")

    def search_book(self, book_id):

        for book in self.books:
            if book.book_id == book_id:
                return book

        return None

    
    def issue_book(self, book_id):

        book = self.search_book(book_id)

        if book is None:
            print("Error: Book not found!")

        elif book.is_available:
            book.is_available = False
            print("Book issued successfully!")

        else:
            print("Sorry! This book is already issued.")

  
    def return_book(self, book_id):

        book = self.search_book(book_id)

        if book is None:
            print("Error: Book not found!")

        elif not book.is_available:
            book.is_available = True
            print("Book returned successfully!")

        else:
            print("This book was not issued.")



def main():

    library = Library()

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Please enter a valid Book ID.")
                continue

            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == "2":

            library.view_books()

        elif choice == "3":

            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Please enter a valid Book ID.")
                continue

            book = library.search_book(book_id)

            if book is not None:
                print("\nBook Found!\n")
                book.display_book()
            else:
                print("Error: Book not found!")

        elif choice == "4":

            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Please enter a valid Book ID.")
                continue

            library.issue_book(book_id)

        elif choice == "5":

            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Please enter a valid Book ID.")
                continue

            library.return_book(book_id)

        elif choice == "6":

            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")



if __name__ == "__main__":
    main()
