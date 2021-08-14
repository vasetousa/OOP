
class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    # add book to user's book list, remove book from library available books, add book to rented books in library
    def get_book(self, author: str, book_name: str, days_to_return: int, library: "Library"):
        if author in library.books_available:
            for i in library.books_available[author]:
                if i == book_name:
                    self.books.append(book_name)    # add to user's book list
                    library.books_available[author].remove(i)   # remove from library available books
                    # print(library.rented_books)     # remove after testing
                    if self.username not in library.rented_books:
                        library.rented_books[self.username] = {}
                        library.rented_books[self.username].update({book_name: days_to_return})
                        # print(library.rented_books)     # remove after testing
                    else:
                        if i not in library.rented_books[self.username]:
                            library.rented_books[self.username].update({book_name: days_to_return})     # add to rented books in library
                            # print(library.rented_books)  # remove after testing
                    return f"{book_name} successfully rented for the next {days_to_return} days!"

        # print(library.rented_books)
        for el in library.rented_books.values():     # check if book has been rented
            for l, j in el.items():
                if book_name in l:
                    return f'The book "{book_name}" is already rented and will be available in {j} days!'

    # add book back to library available books, remove book from user's book list, remove book from rented books list
    def return_book(self, author: str, book_name: str, library: "Library"):
        if book_name in self.books:
            library.books_available[author].append(book_name)   # returning book to library
            # print(library.books_available[author])
            # print(library.rented_books)  # remove after testing

        if book_name in self.books:
            self.books.remove(book_name)

        for el in library.rented_books[self.username]:
            if el == book_name:
                del library.rented_books[self.username][book_name]
                return
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        booklets = sorted(self.books)
        return ', '.join(booklets)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"