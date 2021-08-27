# Before
# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page
#


# After
class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page
        return f"Turning to page {self.page + 1}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove(self, book: Book):
        if book in self.books:
            self.books.remove(book)

    def find_book(self, title):
        for booklet in self.books:
            if booklet.title == title:
                return f"Book {booklet.title} is in the Library"
        return f"Book {title} is not the Library"

    def __repr__(self):
        nl = "\n"
        string = ""
        string += f"Books: " + nl
        for x in self.books:
            string += f" - {x.title}, written by {x.author} in {x.location}\n"
        return string


book = Book("Blah", "Ivan", "Pernik")
book1 = Book("Kosh", "Gosho", "Sofia")
book2 = Book("Vampires", "Pesho", "Varna")
lib = Library()
print(book.turn_page(100))
lib.add_book(book)
lib.add_book(book1)
lib.add_book(book2)
print(lib.find_book("Kosh"))
print(lib.find_book("Prop"))
print(lib)