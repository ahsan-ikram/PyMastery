"""
Relational database CRUD operations using SQL
The Python Database API (DB-API) defines a standard interface for Python database access modules.
It’s documented in PEP 249.
Not Recommended for serious applications
"""

import sqlite3
from patterns.Singleton import Singleton


class SQLiteDatabase(metaclass=Singleton):
    def __init__(self, mode: str = ':memory:'):
        self.connection = sqlite3.connect(mode)
        self.cursor = self.connection.cursor()

    def select(self, sql: str):
        print(sql)
        for row in self.cursor.execute(sql):
            print(row)

    def execute(self, sql: str) -> bool:
        print(sql)
        self.cursor.execute(sql)
        return True

    def __del__(self):
        self.connection.close()


def main():
    db = SQLiteDatabase()
    # db.execute(f"drop table lang")
    db.execute(f"create table lang ('name', 'first_appeared')")
    db.execute(f"insert into lang values ('C', '1972')")
    db.execute(f"insert into lang values ('A', '1990')")
    db.select(f"select * from lang")


if __name__ == "__main__":
    main()
