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
# class Book:
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def get_info(self):
#         return f"This is '{self.title}' by {self.author}"
#
#
# class PageTurner:
#     page = 0
#     max_page = 330
#
#     def turn_page(self, page):
#         if page <= 330:
#             PageTurner.page += page
#             return f"Turning to page {PageTurner.page} ..."
#         return f"This book has only {PageTurner.max_page} pages!"
#
# class Locator:
#     def __init__(self, location):
#         self.location = location
#
#     def get_location(self):
#         return f"This book is located somewhere in {self.location}"
#
# class BookRegister:
#
#     books = []
#
#     def add_book(self, book: Book):
#         current_book = [b for b in BookRegister.books if b.title == book.title]
#         if not current_book:
#             BookRegister.books.append(book)
#             return f"Book '{book.title}' added to the register!"
#         return f"This book is already in the register"
#
#     def __repr__(self):
#         lenny = len(BookRegister.books)
#         nl = "\n"
#         message = f"We currently have {lenny} book(s) in the register:\n"
#         for el in BookRegister.books:
#             message += f">>> '{el.title}', by {el.author}\n"
#
#         return message
#
#
#
#
# b = Book("The Hole", 'Steven King')
# b1 = Book("Maugly", "Emilio Salgary")
# l = Locator("London")
# p = PageTurner()
# br = BookRegister()
# print(br.add_book(b))
# print(br.add_book(b))
# print(br.add_book(b1))
#
# print(l.get_location())
# print(p.turn_page(400))
# print(b.get_info())
# print(br)



# After, another version
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