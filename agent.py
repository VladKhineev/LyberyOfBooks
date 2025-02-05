from book import Book, ManagerBook
from interfaceCmd import message_output

class Agent:
    @classmethod
    def start_app(cls):
        while True:
            print('What do you do?')
            print('1 - Add book')
            print('2 - Find book')
            print('3 - Watch all books')
            print('4 - Update book')
            print('5 - Delete book')
            print('6 - Exit')
            choice_number = input('Enter a number: ')

            if choice_number == '1':
                cls.try_input_and_output_data_for_add_book()
            elif choice_number == '2':
                cls.try_input_and_output_data_for_find_book()
            elif choice_number == '3':
                cls.get_and_output_all_books()
            elif choice_number == '4':
                cls.try_input_and_output_data_for_update_book()
            elif choice_number == '5':
                cls.try_input_and_output_data_for_delete_book()
            elif choice_number == '6':
                break
            else:
                print('There is no such option')

    @classmethod
    def try_input_and_output_data_for_add_book(cls):
        try:
            cls.input_and_output_data_for_add_book()
        except AssertionError:
            message_output('You cannot enter an empty line')
        except ValueError:
            message_output('The year must be a number')

    @classmethod
    def input_and_output_data_for_add_book(cls):
        book = cls.input_data_for_add_book()

        ManagerBook.add_book(book)

        cls.output_added_book(book)

    @staticmethod
    def input_data_for_add_book():
        title = input('Enter title: ')
        assert title
        author = input('Enter author: ')
        assert author
        year = int(input('Enter year: '))
        assert year

        return Book(title, author, year)

    @staticmethod
    def output_added_book(book):
        print(book)

    @classmethod
    def try_input_and_output_data_for_find_book(cls):
        try:
            cls.input_and_output_data_for_find_book()
        except ValueError:
            message_output('You cannot enter an empty line')
        except AssertionError:
            message_output('There in no such option')

    @classmethod
    def input_and_output_data_for_find_book(cls):
        choice, sign = cls.input_data_for_find_book()

        books = ManagerBook.find_book(choice, sign)

        cls.output_books(books)

    @staticmethod
    def input_data_for_find_book():
        print('What to look for?:')
        print('1 - Title')
        print('2 - Author')
        print('3 - Year')

        choice = int(input('Enter status: '))
        assert 1 <= choice <= 3

        sign = input('Enter: ')

        return choice, sign

    @classmethod
    def get_and_output_all_books(cls):
        all_books = ManagerBook.get_all_books()

        cls.output_books(all_books)

    @classmethod
    def try_input_and_output_data_for_update_book(cls):
        try:
            cls.input_and_output_data_for_update_book()
        except KeyError:
            message_output('There is no such book')
        except ValueError:
            message_output('You cannot enter an empty line')
        except AssertionError:
            message_output('There is no such option')

    @classmethod
    def input_and_output_data_for_update_book(cls):
        book_id, status = cls.input_data_for_update_book()

        updated_book = ManagerBook.update_book(book_id, status)

        cls.output_books(updated_book)

    @staticmethod
    def input_data_for_update_book():
        book_id = input('Enter id: ')

        print('Statues:')
        print('1 - в наличие')
        print('2 - выдана')

        status_id = input('Enter status: ')
        assert 1 <= int(status_id) <= 2

        status_all = {
            '1': 'в наличие',
            '2': 'выдана',
        }
        status = status_all[status_id]

        return book_id, status

    @classmethod
    def try_input_and_output_data_for_delete_book(cls):
        try:
            cls.input_and_output_data_for_delete_book()
        except AssertionError:
            message_output('There is no such book')
        except ValueError:
            message_output('You cannot enter an empty line')

    @classmethod
    def input_and_output_data_for_delete_book(cls):
        book_id = cls.input_data_for_delete_book()

        deleted_book = ManagerBook.delete_book(book_id)
        assert deleted_book == 'NotFound'

        cls.output_books(deleted_book)

    @staticmethod
    def input_data_for_delete_book():
        book_id = input('Enter id: ')

        return book_id

    @classmethod
    def output_books(cls, books):
        count_books = len(books)

        if count_books == 1:
            book_data = books[0]
            cls.print_book(book_data)
        else:
            for book_data in books:
                cls.print_book(book_data)

    @staticmethod
    def print_book(book_data):
        book = Book(book_data[1][0], book_data[1][1], book_data[1][2], book_data[1][3], book_data[0])
        print(book)
        print()


