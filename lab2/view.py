from datetime import datetime


class View:

    def show_menu(self):
        self.show_message("\nMenu:")
        self.show_message("1. Add row")
        self.show_message("2. Show table")
        self.show_message("3. Update row")
        self.show_message("4. Delete row")
        self.show_message("5. Exit")
        choice = input("Select your choice: ")
        return choice

    def show_tables(self):
        self.show_message("\nTables:")
        self.show_message("1. Authors")
        self.show_message("2. Books Data")
        self.show_message("3. Books")
        self.show_message("4. Loan")
        self.show_message("5. Readers")
        self.show_message("6. Back to menu")
        table = input("Select table: ")
        return table

    def show_authors(self, authors):
        print("\nAuthors:")
        for author in authors:
            print(f"ID: {author[0]}, Surname: {author[1]}, Name: {author[2]}, Country: {author[3]}")

    def show_books_data(self, books_data):
        print("\nBooks Data:")
        for book_data in books_data:
            print(f"ISBN: {book_data[0]}, ID_Author: {book_data[1]}, Name: {book_data[2]}, Year: {book_data[3]}, Price: {book_data[4]}")

    def show_books(self, books):
        print("\nBooks:")
        for book in books:
            print(f"ID: {book[0]}, ID_Book: {book[1]}")

    def show_loans(self, loans):
        print("\nLoans:")
        for loan in loans:
            print(f"ID: {loan[0]}, ID_Book: {loan[1]}, ID_User: {loan[2]}, Loan_Date: {loan[3]}, Return_Date: {loan[4]}")

    def show_readers(self, readers):
        print("\nReaders:")
        for reader in readers:
            print(f"ID: {reader[0]}, Surname: {reader[1]}, Name: {reader[2]}, Adress: {reader[3]}")

    def get_author_input(self):
        while True:
            try:
                id = input("Enter ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                surname = input("Enter surname: ")
                if surname.strip():
                    break
                else:
                    print("Surname cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                name = input("Enter name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                country = input("Enter country: ")
                if country.strip():
                    break
                else:
                    print("Country cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, surname, name, country

    def get_book_data_input(self):
        while True:
            try:
                isbn = input("Enter ISBN: ")
                if isbn.strip():
                    isbn = int(isbn)
                    break
                else:
                    print("ISBN cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_author = input("Enter ID author: ")
                if id_author.strip():
                    id_author = int(id_author)
                    break
                else:
                    print("ID author cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                name = input("Enter name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                year_input = input("Enter year (YYYY-MM-DD HH:MM:SS+TZ): ")
                if year_input.strip():
                    year = datetime.strptime(year_input, "%Y-%m-%d %H:%M:%S%z")
                    break
                else:
                    print("Year cannot be empty.")
            except ValueError:
                print("Invalid year format. Please use YYYY-MM-DD HH:MM:SS+TZ.")
        while True:
            try:
                price_input = input("Enter price: ")
                if price_input.strip():
                    price = float(price_input)
                    break
                else:
                    print("Price cannot be empty.")
            except ValueError:
                print("Price must be a valid number.")
        return isbn, id_author, name, year, price

    def get_book_input(self):
        while True:
            try:
                id = input("Enter ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_book = input("Enter ID book: ")
                if id_book.strip():
                    id_book = int(id_book)
                    break
                else:
                    print("ID book cannot be empty.")
            except ValueError:
                print("It must be a number.")
        return id, id_book

    def get_loan_input(self):
        while True:
            try:
                id = input("Enter ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_book = input("Enter ID book: ")
                if id_book.strip():
                    id_book = int(id_book)
                    break
                else:
                    print("ID book cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_user = input("Enter ID user: ")
                if id_user.strip():
                    id_user = int(id_user)
                    break
                else:
                    print("ID user cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                loan_date_input = input("Enter loan date (YYYY-MM-DD HH:MM:SS+TZ): ")
                if loan_date_input.strip():
                    loan_date = datetime.strptime(loan_date_input, "%Y-%m-%d %H:%M:%S%z")
                    break
                else:
                    print("Loan date cannot be empty.")
            except ValueError:
                print("Invalid year format. Please use YYYY-MM-DD HH:MM:SS+TZ.")
        while True:
            try:
                return_date_input = input("Enter return date (YYYY-MM-DD HH:MM:SS+TZ): ")
                if return_date_input.strip():
                    return_date = datetime.strptime(return_date_input, "%Y-%m-%d %H:%M:%S%z")
                    break
                else:
                    print("Return date cannot be empty.")
            except ValueError:
                print("Invalid year format. Please use YYYY-MM-DD HH:MM:SS+TZ.")
        return id, id_book, id_user, loan_date, return_date

    def get_reader_input(self):
        while True:
            try:
                id = input("Enter ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                surname = input("Enter surname: ")
                if surname.strip():
                    break
                else:
                    print("Surname cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                name = input("Enter name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                adress = input("Enter adress: ")
                if adress.strip():
                    break
                else:
                    print("Adress cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, surname, name, adress

    def get_author_id(self):
        while True:
            try:
                id = int(input("Enter author ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_book_data_id(self):
        while True:
            try:
                isbn = int(input("Enter ISBN: "))
                break
            except ValueError:
                print("It must be a number.")
        return isbn

    def get_book_id(self):
        while True:
            try:
                id = int(input("Enter book ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_loan_id(self):
        while True:
            try:
                id = int(input("Enter loan ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_reader_id(self):
        while True:
            try:
                id = int(input("Enter reader ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)

    def get_number(self):
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number