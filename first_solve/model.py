from typing import  Optional
from sqlalchemy import create_engine, String, select, Boolean, or_, Date
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
    date: Mapped[Optional[int]] = mapped_column()
    description: Mapped[Optional[str]] = mapped_column(String(256))
    favorites: Mapped[bool] = mapped_column(Boolean)
    read: Mapped[bool] = mapped_column(Boolean)

columns = {
    "название": "name",
    "автор": "author",
    "жанр": "genre",
    "дата": "date",
    "описание": "description",
    "избранное": "favorites",
    "прочитано": "read",
}

def create_database():
    Base.metadata.create_all(engine)

def convert_bool(val):
    if val is True:
        return "Дa"
    else:
        return "Нет"

def convert_y_n(val):
    val_1 = val.lower()
    if val_1 == "да":
        return True
    elif val_1 == "нет":
        return False
    else:
        return val

def add_book(name: str, author = None, genre = None, date = None,
             description = None, favorites = False, read = False):
    with Session(engine) as session:
        new_book = Book(name= name, author= author, genre= genre, date= date,
                        description= description, favorites= favorites, read = read)
        session.add(new_book)
        session.commit()
    print(f"Книга {name} успешно добавлена")

def get_all_books():
    with Session(engine) as session:
        books = session.execute(select(Book)).scalars()
        if books:
            print("Книги из вашей библиотеки:")
            for book in books:
                print(book.name)
        else:
            print("В вашей библиотеке нет книг")

def get_book(name: str):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.name == name).one()
        print(f"О книге: \nНазвание: {book.name} \nАвтор: {book.author} \nЖанр: {book.genre}"
              f" \nДата издания: {book.date} \nИзбранное: {convert_bool(book.favorites)}"
              f" \nПрочитано: {convert_bool(book.read)} \nОписание: {book.description}")

def get_author_books(author):
    with Session(engine) as session:
        books = session.query(Book).filter(Book.author == author).all()
        if books:
            print(f"Ваши автора {author}:")
            for book in books:
                print(book.name)
        else:
            print("У вас нет книг этого автора")

def get_genre_books(genre):
    with Session(engine) as session:
        books = session.query(Book).filter(Book.genre == genre).all()
        if books:
            print(f"Ваши книги в жанре {genre}:")
            for book in books:
                print(book.name)
        else:
            print("У вас нет книг этого жанра")

def get_favorite_books():
    with Session(engine) as session:
        books = session.query(Book).filter(Book.favorites == True).all()
        if books:
            print("Избранные книги:")
            for book in books:
                print(book.name)
        else:
            print("У вас нет избранных книг")

def get_read():
    with Session(engine) as session:
        books = session.query(Book).filter(Book.read == True).all()
        if books:
            print("Прочитанные книги:")
            for book in books:
                print(book.name)
        else:
            print("У вас нет прочитанных книг")

def get_unread():
    with Session(engine) as session:
        books = session.query(Book).filter(Book.read == False).all()
        if books:
            print("Непрочитанные книги:")
            for book in books:
                print(book.name)
        else:
            print("У вас нет непрочитанных книг")

def change_status_favorite(name: str):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.name == name).first()
        if book:
            book.favorites = not book.favorites
            session.commit()
            if book.favorites is True:
                print(f"Книга {name} добавлена в избранное")
            else:
                print(f"Книга {name} убрана из избранного")
        else:
            print("Такой книги не существует")

def change_details(name, field, value):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.name == name).one()
        if book:
            setattr(book, columns[field], value)
            session.commit()
            print("Значение изменено")
        else:
            print("Такой книги не существует")



def delete_book(name):
    with Session(engine) as session:
        book = session.query(Book).filter(Book.name == name).one()
        if book:
            session.delete(book)
            session.commit()
            print(f"Книга {name} успешно удалена")
        else:
            print("Такой книги не существует")

def search_book_keyword(keyword):
    with Session(engine) as session:
        books = session.query(Book).filter(
            or_(
                Book.name.ilike(f"%{keyword}%"),
                Book.author.ilike(f"%{keyword}%"),
                Book.description.ilike(f"%{keyword}%")
            )
        ).all()
        if books:
            print("Результаты поиска:")
            for book in books:
                print(book.name)
        else:
            print("Ничего не найдено")