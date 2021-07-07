from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # {all users}
        self.books_available = {}  # {author: [book1, book2]}
        self.rented_books = {}  # {username: {book name: days to return}}

    def add_user(self, user_n: User):
        if user_n not in self.user_records:
            self.user_records.append(user_n)
        else:
            return f"User with id = {user_n.user_id} already registered in the library!"

    def remove_user(self, user_n: User):
        if user_n in self.user_records:
            self.user_records.remove(user_n)
        else:
            return "We could not find such user to remove!"

    # change username in user records, change username in rented books
    def change_username(self, user_id: int, new_user: str):
        for u in self.user_records:
            if u.user_id == user_id:
                if not u.username == new_user:
                    if u.username in self.rented_books:
                        self.rented_books[new_user] = self.rented_books.pop(u.username)  # changing the name in rented_books
                    u.username = new_user  # change the name in records
                    print(self.user_records)
                    return f"Username successfully changed to: {new_user} for userid: {u.user_id}"
                else:
                    return "Please check again the provided username - " \
                           "it should be different than the username used so far!"
            else:
                return f"There is no user with id = {user_id}!"



# user = User(12, 'Peter')
# library = Library()
# library.add_user(user)
#
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
#                                                 'The Prisoner of Azkaban',
#                                                 'The Goblet of Fire',
#                                                 'The Order of the Phoenix',
#                                                 'The Half-Blood Prince',
#                                                 'The Deathly Hallows']})
#
# print(user.get_book('J.K.Rowling', 'The Dick', 10, library))
# user.get_book('J.K.Rowling', 'The Goblet of Fire', 5, library)
# print(user.get_book('J.K.Rowling', 'The Goblet of Fire', 5, library))
# print(user.return_book('J.K.Rowling', 'The Dick', library))
# user.get_book('J.K.Rowling', 'The Half-Blood Prince', 15, library)
# print(user)
# print(library.books_available)
# print(library.rented_books)
# print(user.info())
#
# print(library.change_username(2, 'Igor'))
# print(library.change_username(12, 'Peter'))
# print(library.change_username(12, 'George'))
# print(user)
