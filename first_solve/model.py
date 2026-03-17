from typing import  Optional
from sqlalchemy import create_engine, String, select, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///library.db")

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(48), unique= True)
    author: Mapped[Optional[str]] = mapped_column(String(48))
    genre: Mapped[Optional[str]] = mapped_column(String(48))
    date: Mapped[Optional[str]] = mapped_column(String(48))
    description: Mapped[Optional[str]] = mapped_column(String(256))
    favorites: Mapped[bool] = mapped_column(Boolean)
    read: Mapped[bool] = mapped_column(Boolean)

def create_database():
    Base.metadata.create_all(engine)

def convert_bool(val):
    if val is True:
        return "Дa"
    else:
        return "Нет"

def add_book(name: str, author = None, genre = None, date = None,
             description = None, favorites = False, read = False):
    with Session(engine) as session:
        new_book = Book(name= name, author= author, genre= genre, date= date,
                        description= description, favorites= favorites, read = read)
        session.add(new_book)
        session.commit()
    print("Книга успешно добавлена")

def get_all_books():
    print("Книги из вашей библиотеки:")
    with Session(engine) as session:
        books = session.execute(select(Book)).scalars()
        for book in books:
            print(book.name)

def get_book(name):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.name == name).first()
        print(f"О книге: \nНазвание: {book.name} \nАвтор: {book.author} \nЖанр: {book.genre}"
              f" \nДата издания: {book.date} \nИзбранное: {convert_bool(book.favorites)}"
              f" \nПрочитано: {convert_bool(book.read)} \nОписание: {book.description}")

def delete_book(name):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.name == name).first()
        if book:
            session.delete(book)
            session.commit()
            print("Книга успешно удалена")
        else:
            print("Такой книги не существует")
