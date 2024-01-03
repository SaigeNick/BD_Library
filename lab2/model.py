from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, BigInteger

s = Session()


class Author(Base):
    __tablename__ = 'Authors'
    ID = Column(BigInteger, primary_key=True)
    Surname = Column(String)
    Name = Column(String)
    Country = Column(String)

    book_data = relationship("BookData")

    def __init__(self, id, surname, name, country):
        self.ID = id
        self.Surname = surname
        self.Name = name
        self.Country = country

    def __repr__(self):
        return f"<Authors(ID={self.ID}, Surname={self.Surname}, Name={self.Name}, Country={self.Country})>"


class BookData(Base):
    __tablename__ = 'Books_Data'
    ISBN = Column(BigInteger, primary_key=True)
    Name = Column(String)
    Year = Column(DateTime)
    Price = Column(Numeric)

    ID_Author = Column(Integer, ForeignKey('Authors.ID'))

    book = relationship("Book")

    def __init__(self, isbn, id_author, name, year, price):
        self.ISBN = isbn
        self.ID_Author = id_author
        self.Name = name
        self.Year = year
        self.Price = price

    def __repr__(self):
        return f"<BooksData(ISBN={self.ISBN}, ID_Author={self.ID_Author}, Name={self.Name}, Year={self.Year}, Price={self.Price})>"


class Book(Base):
    __tablename__ = 'Books'
    ID = Column(BigInteger, primary_key=True)

    ID_Book = Column(Integer, ForeignKey('Books_Data.ISBN'))

    loan = relationship("Loan")

    def __init__(self, id, id_book):
        self.ID = id
        self.ID_Book = id_book

    def __repr__(self):
        return f"<Books(ID={self.ID}, ID_Book={self.ID_Book})>"



class Loan(Base):
    __tablename__ = 'Loan'
    ID = Column(BigInteger, primary_key=True)
    Loan_Date = Column(DateTime)
    Return_Date = Column(DateTime)

    ID_Book = Column(Integer, ForeignKey('Books.ID'))
    ID_User = Column(Integer, ForeignKey('Readers.ID'))

    def __init__(self, id, id_book, id_user, loan_date, return_date):
        self.ID = id
        self.ID_Book = id_book
        self.ID_User = id_user
        self.Loan_Date = loan_date
        self.Return_Date = return_date

    def __repr__(self):
        return f"<Loans(ID={self.ID}, ID_Book={self.ID_Book}, ID_User={self.ID_User}, Loan_Date={self.Loan_Date}, Return_Date={self.Return_Date})>"



class Reader(Base):
    __tablename__ = 'Readers'
    ID = Column(BigInteger, primary_key=True)
    Surname = Column(String)
    Name = Column(String)
    Address = Column(String)

    loan = relationship("Loan")

    def __init__(self, id, surname, name, address):
        self.ID = id
        self.Surname = surname
        self.Name = name
        self.Address = address

    def __repr__(self):
        return f"<Readers(ID={self.ID}, Surname={self.Surname}, Name={self.Name}, Address={self.Address})>"


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def insert_author(self, id: int, surname: str, name: str, country: str) -> None:
        author = Author(id=id, surname=surname, name=name, country=country)
        s.add(author)
        s.commit()

    def insert_book_data(self, isbn: int, id_author: int, name: str, year: DateTime, price: Numeric) -> None:
        book_data = BookData(isbn=isbn, id_author=id_author, name=name, year=year, price=price)
        s.add(book_data)
        s.commit()

    def insert_book(self, id: int, id_book: int) -> None:
        book = Book(id=id, id_book=id_book)
        s.add(book)
        s.commit()

    def insert_loan(self, id: int, id_book: int, id_user: int, loan_date: DateTime, return_date: DateTime) -> None:
        loan = Loan(id=id, id_book=id_book, id_user=id_user, loan_date=loan_date, return_date=return_date)
        s.add(loan)
        s.commit()

    def insert_reader(self, id: int, surname: str, name: str, address: str) -> None:
        reader = Reader(id=id, surname=surname, name=name, address=address)
        s.add(reader)
        s.commit()

    def show_authors(self):
        return s.query(Author.ID, Author.Surname, Author.Name, Author.Country).all()

    def show_books_data(self):
        return s.query(BookData.ISBN, BookData.ID_Author, BookData.Name, BookData.Year, BookData.Price).all()

    def show_books(self):
        return s.query(Book.ID, Book.ID_Book).all()

    def show_loans(self):
        return s.query(Loan.ID, Loan.ID_Book, Loan.ID_User, Loan.Loan_Date, Loan.Return_Date).all()

    def show_readers(self):
        return s.query(Reader.ID, Reader.Surname, Reader.Name, Reader.Address).all()

    def update_author(self, author_id: int, surname: str, name: str, country: str, id: int) -> None:
        s.query(Author).filter_by(ID=id).update(
            {Author.ID: author_id, Author.Surname: surname, Author.Name: name, Author.Country: country})
        s.commit()

    def update_book_data(self, isbn: int, id_author: int, name: str, year: DateTime, price: Numeric, id: int) -> None:
        s.query(BookData).filter_by(ISBN=id).update(
            {BookData.ISBN: isbn, BookData.ID_Author: id_author, BookData.Name: name, BookData.Year: year, BookData.Price: price})
        s.commit()

    def update_book(self, book_id: int, id_book: int, id: int) -> None:
        s.query(Book).filter_by(ID=id).update(
            {Book.ID: book_id, Book.ID_Book: id_book})
        s.commit()

    def update_loan(self, loan_id: int, id_book: int, id_user: int, loan_date: DateTime, return_date: DateTime, id: int) -> None:
        s.query(Loan).filter_by(ID=id).update(
            {Loan.ID: loan_id, Loan.ID_Book: id_book, Loan.ID_User: id_user, Loan.Loan_Date: loan_date, Loan.Return_Date: return_date})
        s.commit()

    def update_reader(self, reader_id: int, surname: str, name: str, address: str, id: int) -> None:
        s.query(Reader).filter_by(ID=id).update(
            {Reader.ID: reader_id, Reader.Surname: surname, Reader.Name: name, Reader.Address: address})
        s.commit()

    def delete_author(self, id) -> None:
        author = s.query(Author).filter_by(ID=id).one()
        s.delete(author)
        s.commit()

    def delete_book_data(self, isbn) -> None:
        book_data = s.query(BookData).filter_by(ISBN=isbn).one()
        s.delete(book_data)
        s.commit()

    def delete_book(self, id) -> None:
        book = s.query(Book).filter_by(ID=id).one()
        s.delete(book)
        s.commit()

    def delete_loan(self, id) -> None:
        loan = s.query(Loan).filter_by(ID=id).one()
        s.delete(loan)
        s.commit()

    def delete_reader(self, id) -> None:
        reader = s.query(Reader).filter_by(ID=id).one()
        s.delete(reader)
        s.commit()