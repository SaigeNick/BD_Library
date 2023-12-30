import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='library',
            user='postgres',
            password='1111',
            host='localhost',
            port=3000
        )

    def add_author(self, id, surname, name, country):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."Authors"("ID", "Surname", "Name", "Country") VALUES(%s, %s, %s, %s);', (id, surname, name, country))
        self.conn.commit()

    def add_book_data(self, isbn, id_author, name, year, price):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."Books_Data"("ISBN", "ID_Author", "Name", "Year", "Price") VALUES(%s, %s, %s, %s, %s);', (isbn, id_author, name, year, price))
        self.conn.commit()

    def add_book(self, id, id_book):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."Books"("ID", "ID_Book") VALUES(%s, %s);', (id, id_book))
        self.conn.commit()

    def add_loan(self, id, id_book, id_user, loan_date, return_date):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."Loan"("ID", "ID_Book", "ID_User", "Loan_Date", "Return_Date") VALUES(%s, %s, %s, %s, %s);', (id, id_book, id_user, loan_date, return_date))
        self.conn.commit()

    def add_reader(self, id, surname, name, adress):
        c = self.conn.cursor()
        c.execute('INSERT INTO public."Readers"("ID", "Surname", "Name", "Address") VALUES(%s, %s, %s, %s);', (id, surname, name, adress))
        self.conn.commit()

    def get_authors(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Authors";')
        return c.fetchall()

    def get_books_data(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Books_Data";')
        return c.fetchall()

    def get_books(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Books";')
        return c.fetchall()

    def get_loans(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Loan";')
        return c.fetchall()

    def get_readers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Readers";')
        return c.fetchall()

    def update_author(self, author_id, surname, name, country, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."Authors" SET "ID"=%s, "Surname"=%s, "Name"=%s, "Country"=%s WHERE "ID"=%s', (author_id, surname, name, country, id))
        self.conn.commit()

    def update_book_data(self, isbn, id_author, name, year, price, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."Books_Data" SET "ISBN"=%s, "ID_Author"=%s, "Name"=%s, "Year"=%s, "Price"=%s WHERE "ISBN"=%s', (isbn, id_author, name, year, price, id))
        self.conn.commit()

    def update_book(self, book_id, id_book, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."Books" SET "ID"=%s, "ID_Book"=%s WHERE "ID"=%s', (book_id, id_book, id))
        self.conn.commit()

    def update_loan(self, loan_id, id_book, id_user, loan_date, return_date, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."Loan" SET "ID"=%s, "ID_Book"=%s, "ID_User"=%s, "Loan_Date"=%s, "Return_Date"=%s WHERE "ID"=%s', (loan_id, id_book, id_user, loan_date, return_date, id))
        self.conn.commit()

    def update_reader(self, reader_id, surname, name, adress, id):
        c = self.conn.cursor()
        c.execute('UPDATE public."Readers" SET "ID"=%s, "Surname"=%s, "Name"=%s, "Address"=%s WHERE "ID"=%s', (reader_id, surname, name, adress, id))
        self.conn.commit()

    def delete_author(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."Authors" WHERE "ID"=%s', (id,))
        self.conn.commit()

    def delete_book_data(self, isbn):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."Books_Data" WHERE "ISBN"=%s', (isbn,))
        self.conn.commit()

    def delete_book(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."Books" WHERE "ID"=%s', (id,))
        self.conn.commit()

    def delete_loan(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."Loan" WHERE "ID"=%s', (id,))
        self.conn.commit()

    def delete_reader(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM public."Readers" WHERE "ID"=%s', (id,))
        self.conn.commit()

    def get_top_authors(self):
        c = self.conn.cursor()
        c.execute('SELECT "Authors"."Name", "Authors"."Surname", COUNT("Books_Data"."ISBN") AS BookCount '
                  'FROM "Authors" '
                  'JOIN "Books_Data" ON "Authors"."ID" = "Books_Data"."ID_Author" '
                  'GROUP BY "Authors"."Name", "Authors"."Surname" '
                  'ORDER BY BookCount DESC '
                  'LIMIT 3;')
        return c.fetchall()

    def get_returned_books(self):
        c = self.conn.cursor()
        c.execute('''
            SELECT "ID_User", "Readers"."Name" AS UserName, "Readers"."Surname" AS UserSurname, COUNT("ID_Book") AS ReturnedBooksCount
            FROM "Loan"
            JOIN "Readers" ON "Loan"."ID_User" = "Readers"."ID"
            GROUP BY "ID_User", UserName, UserSurname
            ORDER BY "ID_User";
        ''')
        return c.fetchall()

    def get_cheapest_books(self):
        c = self.conn.cursor()
        c.execute('''
            SELECT "Books_Data"."ISBN" AS BookID, "Books_Data"."Name" AS BookName, CONCAT("Authors"."Name", ' ', "Authors"."Surname") AS AuthorFullName, "Books_Data"."Price"
            FROM "Books_Data"
            JOIN "Authors" ON "Books_Data"."ID_Author" = "Authors"."ID"
            ORDER BY "Books_Data"."Price"
            LIMIT 5;
        ''')
        return c.fetchall()

    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute("""
            INSERT INTO "Readers" ("ID", "Surname", "Name", "Address")
            SELECT
            row_number() OVER () + (SELECT COALESCE(MAX("ID"), 0) FROM "Readers"),
            chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int),
            chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int),
            chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int)
            FROM generate_series(1, %s);
        """, (number,))
        self.conn.commit()