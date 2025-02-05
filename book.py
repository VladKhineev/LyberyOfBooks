import shelve

class Book:
    def __init__(self, title: str, author: str, year: int, status: str = 'в наличии', book_id: str = ''):
        self.book_id = book_id if book_id != '' else ManagerBook.get_last_book_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        res = (f'Книга: {self.book_id}\n'
               f'Название: {self.title}\n'
               f'Автор: {self.author}\n'
               f'Год: {self.year}\n'
               f'Статус: {self.status}')
        return res


class ManagerBook:
    @staticmethod
    def add_book(book):
        with shelve.open('bookData') as file:
            file[book.book_id] = [book.title, book.author, book.year, book.status]
        return 'Success'

    @staticmethod
    def get_all_books():
        books = []
        with shelve.open('bookData') as file:
            for key in file.keys():
                books.append((key, file[key]))

        return books

    @staticmethod
    def find_book(choice: int, sign: str):
        if choice == 3:
            sign = int(sign)
        found_books = []
        with shelve.open('bookData', 'r') as file:
            for key, value in file.items():
                if sign == value[(choice - 1)]:
                    found_books.append((key, value))

        return found_books

    @staticmethod
    def update_book(book_id: str, status: str):
        with shelve.open('bookData') as file:
            update_book = file[book_id]
            update_book[3] = status
            file[book_id] = update_book

            return [(book_id, update_book)]

    @staticmethod
    def delete_book(book_id: str):
        with shelve.open('bookData') as file:
            deleted_book = file.pop(book_id, 'NotFound')

            return [(book_id, deleted_book)]

    @staticmethod
    def get_last_book_id():
        with shelve.open('bookData') as file:
            keys = list(file.keys())
            last_id = int(keys[-1])

            book_id = str(last_id + 1)

        return book_id