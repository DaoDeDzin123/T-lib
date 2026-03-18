from model import (add_book, get_all_books,
                   delete_book, get_book, change_status_favorite,
                   get_favorite_books, get_read, get_unread, change_details,
                   get_genre_books, get_author_books, search_book_keyword)

directory = [
    "help - выводит список команд",
    "view_books - выводит все книги из вашей библиотеки",
    "view_favorites - выводит все книги из избранного",
    "add_book <название_книги> (Опционально: <автор> <жанр> <дата_издания> <описание> <добавить_в_избранное:Да/Нет> <прочитано:Да/Нет>) - добавляет книгу",
    "look_about <название_книги> - выводит характеристики книги",
    "delete <название_книги> - удаляет книгу",
    "favorite <название_книги> - удаляет из избранного или добавляет в избранное",
    "set_username <имя_пользователя> - задаёт имя пользователя",
    "read - выводит прочитанные книги",
    "unread - выводит непрочитанные книги",
    "change <имя_книги> <параметр> <новое_значение> - изменить параметр книги",
    "genre <имя_жанра> - поиск по жанру",
    "author <имя_автора> - поиск по автору",
    "keyword <ключевое слово> - поиск по ключевому слову"
]

default_config = {
    "default_username": False,
    "username": "Cookie",
    "first_time": False
}

commands = {
    #"help": get_commands,
    "view_books": get_all_books,
    "view_favorites": get_favorite_books,
    "add_book": add_book,
    "look_about": get_book,
    "delete": delete_book,
    "favorite": change_status_favorite,
    #"set_username": set_username,
    "read": get_read,
    "unread": get_unread,
    "change": change_details,
    "genre": get_genre_books,
    "author": get_author_books,
    "keyword": search_book_keyword
}
