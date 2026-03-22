### Доброго времени суток!

Я написала консольное приложение, которое:

Принимает строку и разбивает её на подстроки -> первую подстроку сравнивает со списком команд, остальные принимает в качестве аргументов -> обращается к базе данных sqlite

P.s. Я не считаю специальным знание sqlite. К тому же, разрабатывать собственную систему хранения данных мне лень :) К тому же, данные хранятся в файле, так что без претензий :<

### Команды Т-библиотеки
    help - выводит список команд
    view_books - выводит все книги из вашей библиотеки
    view_favorites - выводит все книги из избранного
    add_book <название_книги> (Опционально: <автор> <жанр> <дата_издания> <описание> <добавить_в_избранное:Да/Нет> <прочитано:Да/Нет>) - добавляет книгу
    look_about <название_книги> - выводит характеристики книги
    delete <название_книги> - удаляет книгу
    favorite <название_книги> - удаляет из избранного или добавляет в избранное
    set_username <имя_пользователя> - задаёт имя пользователя
    read - выводит прочитанные книги
    unread - выводит непрочитанные книги
    change <имя_книги> <параметр> <новое_значение> - изменить параметр книги
    genre <имя_жанра> - поиск по жанру
    author <имя_автора> - поиск по автору
    keyword <ключевое слово> - поиск по ключевому слову

### reference_data
В этот файл вынесены объёмные статические данные, чтобы не засорять код

1. [directory](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/reference_data.py#L6) - список, который хранит описания команд
2. [default_config](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/reference_data.py#L23) - словарь(json), который храннит флаг имени пользователя по умоляанию, заданное имя пользователя, флаг первого запуска программы
3. [commands](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/reference_data.py#L29) - словарь, хранит строки(команды) и соответствующие им функции

### model.py
Здесь описана таблица и функции взаимодейсвия с ней

## Таблица
Книги хранятся в таблице [Book](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L20). Она имеет поля:
1. id(int) - обязательное, является первичным ключом и генерируется автоматически
2. name(str) - обязательное, до 48 символов, должно быть уникальным
3. author(str) - опциональное, ограниченние до 48 символов
4. genre(str) - опциональное, ограниченние до 48 символов
5. date(int) - опциональное
6. description(str) - опциональное, ограниченние до 256 символов
7. favorides(bool) - обязательное
8. read(bool) - обязательное

## Конвертация значений
**[convert_bool](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L37)**
Если нам нужно будет вывести, например, прочитана книга или нет, то база данных вернёт True/False. Эта функция переводит логическое значени в более человекочитаемый вид Да/Нет

**[convert_y_n](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L43)**
Тоже самое, только наоборот, чтобы программа могла понять, что ввёл пользователь

**[columns](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L5)**
Сопоставление полей, вводимых пользователем, и названий в программе. Это для функции change_details, чтобы база данных могла распознать поле, значение которой нужно изменить

## Функции взаимодействия с базой данных
1. [add_book](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L52) - принимает аргументы, которые соответствуют полям. Имя - обязательный параметр, остальные о умолчанию None, а параметры-флаги равны False; добавляет новую книгу в таблицу
2. [get_all_books](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L61) - печатает в консоль названия всех существующих книг
3. [get_book](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L71) - принимает название книги и печатает все его поля
4. [get_author_books](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L78) - принимает строку, и печатает все книги, у которых поле author равно этому значению
5. [get_genre_books](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L88) - принимает строку, и печатает все книги, у которых поле genre равно этому значению
6. [get_favorite_books](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L98) - печатает все книги, где favorites = True
7. [get_read](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L108) - печатает все книги, где значение read = True
8. [get_unread](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L118) - печатает все книги, где значение read = False
9. [change_status_favorite](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L128) - меняет флаг favorites
10. [change_details](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L141) - название книги, поле, новое значение и меняет его
11. [delete_book](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L153) - принимает имя книги и удаляет её
12. [search_book_keyword](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/model.py#L163) - ищет книгу по ключевому слову в полях name, description и author

### main.py
Здесь вся логика

## Проверка и загрузка конфигурации
**[check_config](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/main.py#L12)** - проверяет наличие конфигурации, и при её отсутствии создаёт стандартную

**[get_config](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/main.py#L24)** - читает json и преобразует его в словарь

## [greeting](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/main.py#L30)
Приветсвует пользователя, используя либо стандартное, либо заданное имя пользователя. Если человек запустил программу в первый раз, выводит сисок команд и опускает флаг

## [get_commands](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/main.py#L48)
Выводит список команд, соответствует команде help

## [set_username](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/main.py#L53)
Записывает в config.json имя пользователя, опускает флаг имени пользователя по умолчанию

## [command_manager](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/main.py#L61)
Разделяет введёную строку на подстроки, первую сравнивает с существующими командами, остальные, при наличии, передаёт вызванной вункции в качестве аргументов

## [Главный цикл](https://github.com/DaoDeDzin123/T-lib/blob/main/first_solve/main.py#L84)
Сначала создаёт таблицу(если ещё не создана), и приветствует пользователя, затем запускается бесконечный цикл, в котором command_maneger обрабатывает все написанные строки

### Тесты
Я поссорилась с линуксом, поэтому тестов не будет :(
