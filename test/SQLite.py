# БД - это таблица. Названия колонок - аргументы, имеют тип (int, text, float...)
# Таблицы можно связывать по ключу в реляционных БД.
# СУБД - системы управления БД. Управляется через свой API (программный интерфейс).
# Популярные СУБД: SQLite, PyMySQL, PostgreSQL.
# SQLite самая популярная, но не поддерживает сетевое взаимодействие и многопоточную запись
# DB Browser for SQLite: https://sqlitebrowser.org

# -- делаем БД в PyCharm --
import sqlite3 as sq

# метод connect устанавливает связь с базой данных saper.db:
# если она есть в том же каталоге, если нету - создает
with sq.connect("saper.db") as con:

# для взаимодействия с БД нужен объект - курсор.
# метод cursor возвращает объект класса Cursor
# работа осуществляется через переменную cur
    cur = con.cursor()

    # cur.execute("""
    # """)
# запускаем код
# появился файл saper.db

# БД обязательно закрыть в конце - либо con.close,
# либо как здесь открывать через контекстный менеджер with и тогда вручную не закрывать:
# with по сути добавляет con.commit() - применить изменения, и con.close()


# -- идем в DB Browser --
# открыть БД - выбрать БД в папке проектов
# создаем таблицу с полями name, sex, old, score - имя, пол, возраст, очки
# типы данных: INTEGER, REAL, TEXT, BLOB...
# пишем в методе execute ("""CREATE TABLE users (
#     name TEXT
#     sex INTEGER
#     old INTEGER
#     score INTEGER
#     )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        sex INTEGER,
        old INTEGER,
        score INTEGER
        )""")

# запускаем код, создался файл saper.db, а в DB Browser - users появилась с параметрами
# лучше написать CREATE TABLE IF NOT EXISTS чтобы избежать ошибки, если создаем уже существующую таблицу

# -- добавление данных --
# в DB Browser - вкладка Данные - выбрать users - нажать добавить запись - добавить - нажать записать изменения
# а на вкладке SQL можно писать запросы, например, SELECT * FROM users
# SELECT rowid, * FROM users - увидеть скрытые уникальные идентификаторы, чтобы связывать таблицы

# cur.execute("DROP TABLE users") - удалить таблицу


# -- ограничители, которые можно указать для полей, примеры --
# name TEXT NOT NULL - не может быть пустым
# sex INTEGER NOT NULL DEFAULT 1 - не пустое и по дефолту мужской пол
# user_id INTEGER PRIMARY KEY - user_id будет главным ключом, примет значение автоматически

    cur.execute("DROP TABLE IF EXISTS users")

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )""")

# к PRIMARY KEY можно дописать AUTOINCREMENT, чтобы гарантировать, что каждый раз значение увеличивалось на 1.


# -- команды SELECT и INSERT для обращения к таблице в DB Browser --
# INSERT INTO <table name>(<column name 1>,<column name 2>, ...) VALUES(<value 1>, <value 2>, ...)
# если будем писать во все поля по порядку, можно INSERT INTO <table name> VALUES(<value 1>, <value 2>, ...)
# идем в DB Browser, вкладка SQL, пишем: INSERT INTO users VALUES('Миха', 1, 19, 1000)
# или INSERT INTO users (name, old, score) VALUES('Федя', 22, 100)

# SELECT col1, col2, ... FROM <table name> - выборка данных
# например, SELECT name, old, score FROM users
# добавление WHERE определяет условия выборки, например: SELECT * FROM users WHERE score < 1000 AND old > 20
# в условии поддерживаются все операторы плюс BETWEEN
# ORDER BY old - если прописать второй строкой в запросе, отсортирует по возрастанию возраста (old DESC - по убыванию)
# LIMIT - сколько записей показать, начиная с первой (OFFSET - начиная с другой):
# SELECT * FROM users
# WHERE score > 100 ORDER BY score DESC LIMIT 5 OFFSET 2

# то же самое, но в PyCharm:
    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")

# -- fetchall(), fetchmany(size), fetchone() --
    result = cur.fetchall() # вернет всё
    result1 = cur.fetchone() # вернет первое
    result2 = cur.fetchmany(2) # вернет первые два
    print(result)
    print(result1)
    print(result2)


# -- UPDATE И DELETE --
# UPDATE <имя таблицы> SET <имя столбца> = <новое значение> WHERE <условие>
# в DB Browser вкладка SQL пишем
# UPDATE users SET score = 0
# или UPDATE users SET score = score+500 WHERE sex = 2
# или UPDATE users SET score = 500 WHERE name LIKE 'М%' - дать 500 очков всем, у кого имя на М ('М_ха%' - М,любая буква,х,а,любые буквы)

# DELETE FROM <имя таблицы> WHERE <условие>
# DELETE FROM users WHERE rowid IN(2, 5) - удалит записи с rowid 2 и 5
# !rowid НЕ РАВНО user_id!


# -- агрегирование и группировка --
# SELECT count(user_id) FROM users WHERE old > 20
# SELECT count(DISTINCT user_id) FROM users - выбор уникальных полей с user_id
# для удобства: после count(user_id) пишем as count (или другое имя синонима)
# агрегирующие функции: count(), sum(), avr(), min(), max(), ...
# SELECT sum(score) FROM users WHERE sex = 1 - суммировать все очки мужчин

# GROUP BY <имя поля> - сгруппировать по полю
# SELECT user_id, sum(score) as sum FROM users GROUP BY sex - даст суммы очков мужчин и женщин

# -- создание сводных отчетов JOIN --
    cur.execute("""CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER,
        score INTEGER,
        time
        )""")
# сформируем сводный отчет, содержащий name, sex, score
# SELECT name, sex, games.score FROM games - команда, список полей сводной таблицы, FROM - какая таблица будет первичной и в нее будут добавляться данные
# JOIN users ON games.user_id=users.rowid - JOIN - какая таблица будет привязана, ON - условие связывания (user_id в games равен rowid в users)
# данные из присоединяемой таблицы (users) будут подставлены в первичную (games)
# записи, для которых не было совпадений, в сводной таблице будут отсутствовать.

# LEFT JOIN - сохраняет все записи первичной таблицы, объединяет те, которые совпали по ключу

# запрос, формирующий топ игроков:
# SELECT name, sex, sum(games.score) as score
# FROM games
# JOIN users ON games.user_id = users.rowid
# GROUP BY games.user_id
# ORDER BY score DESC


# -- построчное объединение UNION --
# выведем пол и время в одной таблице:
# SELECT sex FROM users
# UNION SELECT time FROM games
# UNION при объединении оставляет только записи с уникальными значениями!


# -- вложенные запросы --
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER NOT NULL,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER NOT NULL DEFAULT 20
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS marks (
        id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        mark INTEGER NOT NULL DEFAULT 1
        )""")

# выбрать всех студентов, у которых оценка по Si выше, чем у Маши:
# SELECT mark FROM marks WHERE id = 2 AND subject LIKE 'Si' - нашли Машину оценку по Си
# SELECT name, subject, mark FROM marks # формируем сводную таблицу с тремя колонками
# JOIN students ON students.rowid = marks.id # присоединяем таблицу students при условии совпадения rowid студента и id оценки
# WHERE mark > 3 AND subject LIKE 'Si' # при условии что оценка выше 3 по предмету Si

# другой способ - вложенные запросы (прибегать к ним нужно в последнюю очередь):
# SELECT name, subject, mark FROM marks
# JOIN students ON students.rowid = marks.id
# WHERE mark > (SELECT mark FROM marks WHERE id = 2 AND subject LIKE 'Si')
# AND subject LIKE 'Si'


# -- методы sqlite3 --
# execute - выполнить
# можно так:

    # cur.execute("""CREATE TABLE IF NOT EXISTS cars (
    #     id INTEGER NOT NULL,
    #     subject TEXT NOT NULL,
    #     num INTEGER NOT NULL DEFAULT 1
    #     )""")
    #
    # cur.execute("INSERT INTO cars VALUES(1, 'Audi', 52642)")
    # cur.execute("INSERT INTO cars VALUES(2, 'BMW', 13212)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Mini', 22244)")

# но лучше сперва создать коллекцию и брать значения оттуда:
cars = [
    (1, 'Audi', 52642),
    (2, 'BMW', 13212),
    (3, 'Mini', 22244)
]

with sq.connect("cars.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
        )""")


# и передавать их в SQL запрос:

    # cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars)
    cur.execute("UPDATE cars SET price = price+500 WHERE model = 'Zapor'")


