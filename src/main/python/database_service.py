import sqlite3
from contextlib import closing

TABLE_FILE = "famous_people.db"


def initialize_db():
    with closing(sqlite3.connect(TABLE_FILE)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS famous_people(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        summary TEXT NOT NULL
                        )""")


def add_person(name, summary):
    with closing(sqlite3.connect(TABLE_FILE)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("INSERT INTO famous_people (name, summary) VALUES (:name, :summary)", {"name": name, "summary": summary})
            connection.commit()


def retrieve_all():
    with closing(sqlite3.connect(TABLE_FILE)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM famous_people")
            records = cursor.fetchall()
            for record in records:
                print(record)


initialize_db()
