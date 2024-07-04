import sqlite3

from pathlib import Path


class DataDBSingleton:

    def __init__(self, DB_FILE: Path) -> None:
        self.DB_FILE = DB_FILE
        self.conexao: sqlite3.Connection
        self.cursor: sqlite3.Cursor

    # -----------------------------------------------------------------------
    def executar_sql(self, sql: str, parametros: tuple = ()) -> sqlite3.Cursor:
        # try:
        with sqlite3.connect(self.DB_FILE) as self.conexao:
            self.cursor = self.conexao.cursor()
            self.cursor.execute("PRAGMA foreign_keys = ON")
            self.cursor.execute(sql, parametros)
            self.conexao.commit()

        return self.cursor

    # except sqlite3.Error as e:
    #     print("\n\n \t\t ERROR CPAPTURADO \n")
    #     print(f"{e = }")
