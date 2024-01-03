import time
from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '5':
                break
            elif choice in ['1', '2', '3', '4']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()

            if table == '6':
                break

            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_view_option(table)
            elif choice == '3':
                self.process_update_option(table)
            elif choice == '4':
                self.process_delete_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding author:")
            self.add_author()
        elif table == '2':
            self.view.show_message("\nAdding book data:")
            self.add_book_data()
        elif table == '3':
            self.view.show_message("\nAdding book:")
            self.add_book()
        elif table == '4':
            self.view.show_message("\nAdding loan:")
            self.add_loan()
        elif table == '5':
            self.view.show_message("\nAdding reader:")
            self.add_reader()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.show_authors()
        elif table == '2':
            self.show_books_data()
        elif table == '3':
            self.show_books()
        elif table == '4':
            self.show_loans()
        elif table == '5':
            self.show_readers()
        elif table == '6':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating author:")
            self.update_author()
        elif table == '2':
            self.view.show_message("\nUpdating book data:")
            self.update_book_data()
        elif table == '3':
            self.view.show_message("\nUpdating book:")
            self.update_book()
        elif table == '4':
            self.view.show_message("\nUpdating loan:")
            self.update_loan()
        elif table == '5':
            self.view.show_message("\nUpdating reader:")
            self.update_reader()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting author:")
            self.delete_author()
        elif table == '2':
            self.view.show_message("\nDeleting book data:")
            self.delete_book_data()
        elif table == '3':
            self.view.show_message("\nDeleting book:")
            self.delete_book()
        elif table == '4':
            self.view.show_message("\nDeleting loan:")
            self.delete_loan()
        elif table == '5':
            self.view.show_message("\nDeleting reader:")
            self.delete_reader()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def add_author(self):
        try:
            id, surname, name, country = self.view.get_author_input()
            self.model.insert_author(id, surname, name, country)
            self.view.show_message("Author added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_book_data(self):
        try:
            isbn, id_author, name, year, price = self.view.get_book_data_input()
            self.model.insert_book_data(isbn, id_author, name, year, price)
            self.view.show_message("Book Data added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_book(self):
        try:
            id, id_book = self.view.get_book_input()
            self.model.insert_book(id, id_book)
            self.view.show_message("Book added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_loan(self):
        try:
            id, id_book, id_user, loan_date, return_date = self.view.get_loan_input()
            self.model.insert_loan(id, id_book, id_user, loan_date, return_date)
            self.view.show_message("Loan added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_reader(self):
        try:
            id, surname, name, adress = self.view.get_reader_input()
            self.model.insert_reader(id, surname, name, adress)
            self.view.show_message("Reader added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_authors(self):
        try:
            authors = self.model.show_authors()
            self.view.show_authors(authors)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_books_data(self):
        try:
            books_data = self.model.show_books_data()
            self.view.show_books_data(books_data)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_books(self):
        try:
            books = self.model.show_books()
            self.view.show_books(books)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_loans(self):
        try:
            loans = self.model.show_loans()
            self.view.show_loans(loans)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_readers(self):
        try:
            readers = self.model.show_readers()
            self.view.show_readers(readers)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_author(self):
        try:
            id = self.view.get_author_id()
            author_id, surname, name, country = self.view.get_author_input()
            self.model.update_author(author_id, surname, name, country, id)
            self.view.show_message("Author updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_book_data(self):
        try:
            id = self.view.get_book_data_id()
            isbn, id_author, name, year, price = self.view.get_book_data_input()
            self.model.update_book_data(isbn, id_author, name, year, price, id)
            self.view.show_message("Book Data updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_book(self):
        try:
            id = self.view.get_book_id()
            book_id, id_book = self.view.get_book_input()
            self.model.update_book(book_id, id_book, id)
            self.view.show_message("Book updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_loan(self):
        try:
            id = self.view.get_loan_id()
            loan_id, id_book, id_user, loan_date, return_date = self.view.get_loan_input()
            self.model.update_loan(loan_id, id_book, id_user, loan_date, return_date, id)
            self.view.show_message("Loan updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_reader(self):
        try:
            id = self.view.get_reader_id()
            reader_id, surname, name, adress = self.view.get_reader_input()
            self.model.update_reader(reader_id, surname, name, adress, id)
            self.view.show_message("Reader updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_author(self):
        try:
            id = self.view.get_author_id()
            self.model.delete_author(id)
            self.view.show_message("Author deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_book_data(self):
        try:
            isbn = self.view.get_book_data_id()
            self.model.delete_book_data(isbn)
            self.view.show_message("Book Data deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_book(self):
        try:
            id = self.view.get_book_id()
            self.model.delete_book(id)
            self.view.show_message("Book deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_loan(self):
        try:
            id = self.view.get_loan_id()
            self.model.delete_loan(id)
            self.view.show_message("Loan deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_reader(self):
        try:
            id = self.view.get_reader_id()
            self.model.delete_reader(id)
            self.view.show_message("Reader deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")