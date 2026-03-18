from json import JSONDecodeError
from reference_data import directory, default_config
import os

from model import (create_database, add_book, get_all_books,
                   delete_book, get_book, change_status_favorite,
                   get_favorite_books, get_read, get_unread, change_details,
                   get_genre_books, get_author_books, search_book_keyword, convert_y_n)
from getpass import getuser
import json

# example "Название", "Автор", "Жанр", "Дата", "Описание", True, True

default_username = getuser()

def check_config():
    try:
        if os.path.exists("config.json"):
            pass
        else:
            # default_json = json.dumps(default_config, ensure_ascii=False, indent=4)
            with open("config.json", "w") as file:
                json.dump(default_config, file)
    except JSONDecodeError or TypeError:
        os.remove("config.json")
        # default_json = json.dumps(default_config, ensure_ascii=False, indent=4)
        with open("config.json", "w") as file:
            json.dump(default_config, file)

def get_config():
    check_config()
    with open("config.json", "r") as file:
        config = json.load(file)
    return config

def greeting():
    config = get_config()
    if config["default_username"] is True:
        print(f"Добро пожаловать в библиотеку, {default_username}!")
    else:
        print(f"Добро пожаловать в библиотеку, {config['username']}!")

    if config["first_time"] is True:
        try:
            get_commands()
            config["first_time"] = False
            with open("config.json", "w") as file:
                json.dump(config, file)
            print("Давайте добавим вашу первую книгу!\n")
        except Exception as e:
            print(f"Ошибка в greeting {e}")


def get_commands():
    print("Вот список команд:")
    for command in directory:
        print(command)

def set_username(new_username):
    config = get_config()
    config["default_username"] = False
    config["username"] = new_username
    with open("config.json", "w") as file:
        json.dump(config, file)
    print(f"Задано имя пользователя {new_username}")

def command_manager(input_command):
    try:
        paths_command = input_command.split()
        length = len(paths_command)
        if length > 1:
                new_paths_command = []
                for i in paths_command:
                    new_paths_command.append(convert_y_n(i))
                commands[paths_command[0]](*new_paths_command[1:])
        elif length == 1:
            commands[paths_command[0]]()
        else:
            pass
    except KeyError:
        print("Нет такой команды. Введите help для списка доступных команд")
    except ValueError or TypeError:
        print("Введите корректные данные")
    except Exception as e:
        print(f"Ошибка в command_maneger {e}")

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
    "change": change_details,
    "genre": get_genre_books,
    "author": get_author_books,
    "keyword": search_book_keyword
}

if __name__ == "__main__":
    create_database()
    greeting()
    while True:
        input_command = input()
        command_manager(input_command)