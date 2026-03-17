from model import (create_database, add_book, get_all_books,
                   delete_book, get_book, change_status_favorite,
                   get_favorite_books, get_read, get_unread, change_details)
import getpass
import json

#TO DO получение книг по фильтру
# example "Название", "Автор", "Жанр", "Дата", "Описание", True, True

default_username = getpass.getuser()

def get_config():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
    return config

def greeting():
    config = get_config()
    if config["default_username"] is True:
        print(f"Добро пожаловать в библиотеку, {default_username}!")
    else:
        print(f"Добро пожаловать в библиотеку, {config['username']}!")

    if config["first_time"] is True:
        get_commands()
        config["first_time"] = False
        with open("config.json", "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4, ensure_ascii=False)
        print("Давайте добавим вашу первую книгу!\n")


def set_username(new_username):
    config = get_config()
    config["default_username"] = False
    config["username"] = new_username
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4, ensure_ascii=False)
    print(f"Задано имя пользователя {new_username}")


def get_commands():
    print("Вот список команд:")
    for command in directory:
        print(command)


def command_manager(input_command):
    paths_command = input_command.split()
    length = len(paths_command)
    if length > 1:
        commands[paths_command[0]](*paths_command[1:])
    elif length == 1:
        commands[paths_command[0]]()
    else:
        pass

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
    "unread - выводит непрочитанные книги"
]

commands = {
    "help": get_commands,
    "view_books": get_all_books,
    "view_favorites": get_favorite_books,
    "add_book": add_book,
    "look_about": get_book,
    "delete": delete_book,
    "favorite": change_status_favorite,
    "set_username": set_username,
    "read": get_read,
    "unread": get_unread,
    "change": change_details
}

if __name__ == "__main__":
    create_database()
    greeting()
    while True:
        input_command = input()
        command_manager(input_command)