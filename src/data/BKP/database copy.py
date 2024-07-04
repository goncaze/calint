import sqlite3
from pathlib import Path, WindowsPath
from src.modelo.data import Data
from src.modelo.data_categoria import DataCategoria
from src.modelo.evento_categoria import EventoCategoria
from src.modelo.evento import Evento


class DataDB:

    def __init__(self, DB_FILE: WindowsPath) -> None:
        self.DB_FILE = DB_FILE
        self.conexao: sqlite3.Connection = None
        self.cursor: sqlite3.Cursor = None
        self.criar_tabela_data_categoria()
        self.criar_tabela_evento_categoria()
        self.criar_tabela_evento()
        self.criar_tabela_data()
        self.criar_tabela_evento_data()

    # -----------------------------------------------------------------------
    def executar_sql(self, sql: str, parametros: tuple = ()) -> sqlite3.Cursor:

        with sqlite3.connect(self.DB_FILE) as self.conexao:
            self.cursor = self.conexao.cursor()
            self.cursor.execute(sql, parametros)
            self.conexao.commit()
        return self.cursor

    ##
    # CRIAR TABELAS
    ##
    def criar_tabela_evento_categoria(self) -> None:
        criar_tabela_evento_categoria = """CREATE TABLE IF NOT EXISTS evento_categoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        categoria TEXT NOT NULL UNIQUE,
        descricao TEXT
        )"""
        self.executar_sql(criar_tabela_evento_categoria)

    def criar_tabela_evento(self) -> None:
        criar_tabela_evento = """CREATE TABLE IF NOT EXISTS evento(
        id INTEGER PRIMARY KEY AUTOINCREMENT,             
        evento_categoria_id INTEGER NOT NULL, 
        evento TEXT NOT NULL,    
        descricao TEXT,
        FOREIGN KEY(evento_categoria_id) REFERENCES evento_categoria(id)
        )"""
        self.executar_sql(criar_tabela_evento)

    def criar_tabela_data_categoria(self) -> None:
        criar_tabela_data_categoria = """CREATE TABLE IF NOT EXISTS data_categoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        categoria TEXT NOT NULL UNIQUE,
        descricao TEXT
        )"""
        self.executar_sql(criar_tabela_data_categoria)

    def criar_tabela_data(self) -> None:
        criar_tabela_data = """CREATE TABLE IF NOT EXISTS data(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        data TEXT NOT NULL,         
        data_categoria_id INTEGER NOT NULL,
        FOREIGN KEY(data_categoria_id) REFERENCES data_categoria(id)
        )"""
        self.executar_sql(criar_tabela_data)

    def criar_tabela_evento_data(self) -> None:
        criar_tabela_evento_data = """CREATE TABLE IF NOT EXISTS evento_data(
        data_id INTEGER NOT NULL, 
        evento_id INTEGER NOT NULL, 
        FOREIGN KEY(data_id) REFERENCES data(id),
        FOREIGN KEY(evento_id) REFERENCES evento(id)
        )"""
        self.executar_sql(criar_tabela_evento_data)

    # # -----------------------------------------------------------------------
    # Select eventos de uma data específica
    ##
    def select_eventos_por_data(self, data_id: int) -> list[Evento]:
        # print(f"\n\n ====== {data_id = } ======== \n\n")
        lista_eventos: list[Evento] = []
        parametro = (data_id,)
        # print(f"\n\n ====== {parametro = } ======== \n\n")
        sql = "SELECT evento_id FROM evento_data WHERE data_id = ?"

        cursor = self.executar_sql(sql, parametro)

        lista_ids = cursor.fetchall()

        return self.select_evento_alguns(lista_ids)

    # # -----------------------------------------------------------------------
    # Select eventos de uma data específica
    ##
    def select_eventos_data(self, data_id: int) -> list[Evento]:

        lista_eventos: list[Evento] = []
        parametro = (data_id,)
        sql = "SELECT evento_id FROM evento_data WHERE data_id = ?"

        cursor = self.executar_sql(sql, parametro)

        lista_ids = cursor.fetchall()

        return self.select_evento_alguns(lista_ids)

    # # -----------------------------------------------------------------------
    # INSERT evento para uma data específica na tabela evento_data
    ##
    def insert_eventos_data(self, data_id: int, evento_id: int) -> None:
        parametros = (data_id, evento_id)
        sql = """
            INSERT INTO 
                evento_data(data_id, evento_id) 
            values(?,?)
        """

        self.executar_sql(sql, parametros)

    # # -----------------------------------------------------------------------
    # SELECT_EVENTO_CATEGORIA_TODOS
    ##
    def select_evento_categoria_todos(self) -> list[EventoCategoria]:
        """
        Select todas as categorias de evento na tabela evento_categoria
        sql = 'SELECT * FROM evento_categoria'
        """
        lista_evento_categoria = []
        lista_de_evento_categoria = "SELECT * FROM evento_categoria"
        resultado = self.executar_sql(lista_de_evento_categoria)

        for registro in resultado:
            evento_categoria = EventoCategoria(
                id=registro[0], categoria=registro[1], descricao=registro[2]
            )
            lista_evento_categoria.append(evento_categoria)

        return lista_evento_categoria

    # # -----------------------------------------------------------------------
    # SELECT_EVENTO_CATEGORIA
    ##
    def select_evento_categoria(self, id: int) -> EventoCategoria:
        """
        Select uma categoria de evento para um evento especificado (id)
        sql = 'SELECT * FROM evento_categoria WHERE id = ?'
        """
        parametro = (id,)  # Tipo tupla
        sql = "SELECT * FROM evento_categoria WHERE id = ?"

        cursor = self.executar_sql(sql, parametro)

        registro = cursor.fetchone()

        evento_categoria = EventoCategoria(
            id=registro[0], categoria=registro[1], descricao=registro[2]
        )

        return evento_categoria

    # # -----------------------------------------------------------------------
    # UPDATE registro na tabela evento_categoria
    ##
    def update_evento_categoria(self, id: int, categoria: str, descricao: str):

        parametros = (categoria, descricao, id)

        sql = """
            UPDATE 
                evento_categoria
            SET categoria = ?, descricao = ?
            WHERE id = ?
            """

        self.executar_sql(sql, parametros)  # .rowcount

    # # -----------------------------------------------------------------------
    # SELECT_DATA_CATEGORIA_TODOS
    ##
    def select_data_categoria_todos(self) -> list[DataCategoria]:
        """
        Select todas as categorias de data na tabela data_categoria
        sql = 'SELECT * FROM data_categoria'
        """
        lista_data_categoria: list[DataCategoria] = []

        lista_de_evento_categoria = "SELECT * FROM data_categoria"
        cursor = self.executar_sql(lista_de_evento_categoria)

        for registro in cursor:
            data_categoria = DataCategoria(
                id=registro[0], categoria=registro[1], descricao=registro[2]
            )
            lista_data_categoria.append(data_categoria)

        return lista_data_categoria

    # # -----------------------------------------------------------------------
    # UPDATE registro na tabela evento
    ##
    def update_evento(
        self, id: int, evento_categoria: EventoCategoria, evento: str, descricao: str
    ):

        parametros = (evento_categoria.id, evento, descricao, id)

        sql = """
            UPDATE
                evento
            SET  
                evento_categoria_id = ?, evento = ?, descricao = ?
            WHERE 
                id = ?
            """

        self.executar_sql(sql, parametros)  # .rowcount

    # # -----------------------------------------------------------------------
    # SELECT_EVENTOS
    ##
    def select_evento(self, id: int) -> Evento:
        """
        Select um evento para um evento especificado (id)
        sql = 'SELECT * FROM evento WHERE id = ?'
        """
        parametro = (id,)  # Tipo tupla
        sql = "SELECT * FROM evento WHERE id = ?"

        cursor = self.executar_sql(sql, parametro)

        registro = cursor.fetchone()

        evento = Evento(
            id=registro[0],
            evento_categoria=self.select_evento_categoria(registro[1]),
            evento=registro[2],
            descricao=registro[3],
        )

        return evento

    # # -----------------------------------------------------------------------
    # Select somente eventos relacionados a uma data específica
    ##
    def select_evento_alguns(self, lista_ids: list[tuple]) -> list[Evento]:

        lista_evento: list[Evento] = []

        for parametro in lista_ids:
            # parametro = id
            sql = "SELECT * FROM evento WHERE id = ?"

            cursor = self.executar_sql(sql, parametro)

            registro = cursor.fetchone()

            evento = Evento(
                id=registro[0],
                evento_categoria=self.select_evento_categoria(registro[1]),
                evento=registro[2],
                descricao=registro[3],
            )
            lista_evento.append(evento)

        return lista_evento

    # # -----------------------------------------------------------------------
    # Select dados na tabela data_categoria
    ##
    def select_data_categoria(self, id: int) -> DataCategoria:
        parametro = (id,)

        sql = "SELECT * FROM data_categoria WHERE id = ?"
        cursor = self.executar_sql(sql, parametro)

        registro = cursor.fetchone()

        # print(f"""
        #       \n\n ====== select_data_categoria() ====== \n
        #       {registro[0] = }
        #       {registro[1] = }
        #       {registro[2] = }
        #       \n
        #       """
        # )

        data_categoria = DataCategoria(
            id=registro[0], categoria=registro[1], descricao=registro[2]
        )

        return data_categoria

    # # -----------------------------------------------------------------------
    # SELECT todas as DATAS
    ##
    def select_data_todas(self) -> list[Data]:
        """
        Select todos os eventos na tabela data
        sql = 'SELECT * FROM data'
        """
        lista_data: list[Data] = []

        sql = "SELECT * FROM data"

        cursor = self.executar_sql(sql)

        for registro in cursor:
            # print(f"\n\n select_data_todas() ====== {type(registro[0]) = } ======== \n\n")
            data = Data(
                id=registro[0],
                data=registro[1],
                data_categoria=self.select_data_categoria(registro[2]),
                eventos=self.select_eventos_por_data(registro[0]),
            )
            lista_data.append(data)

        return lista_data

    # # -----------------------------------------------------------------------
    # SELECT somente uma DATA
    ##
    def select_uma_data(self, data: Data) -> Data:
        """
        Seleciona uma data por id primeiramente.
        Se não houver id usa-se a data literal ex.: '01/01/2010'
        sql = 'SELECT * FROM data WHERE id = id?'
        sql = 'SELECT * FROM data WHERE data = data?'
        """
        sql: str = None
        parametros: tuple = None

        if data.id is not None and data.id > 0:
            parametros = (data.id,)
            sql = "SELECT * FROM data WHERE id = ?"
        elif data.data is not None and data.data != "":
            parametros = (data.data,)
            sql = "SELECT * FROM data WHERE data = ?"

        if sql:
            cursor = self.executar_sql(sql, parametros)

            for registro in cursor:
                data = Data(
                    id=registro[0],
                    data=registro[1],
                    data_categoria=self.select_data_categoria(registro[2]),
                    eventos=self.select_eventos_por_data(registro[0]),
                )
                return data

        return None

    # # -----------------------------------------------------------------------
    # DELETAR registro na tabela data_categoria
    ##
    def delete_evento_categoria(self, id: int):
        parametro = (id,)
        sql = """
            DELETE FROM
                evento_categoria
            WHERE id = ?
            """

        self.executar_sql(sql, parametro)  # .rowcount

    # # -----------------------------------------------------------------------
    # SELECT_EVENTO
    ##
    def select_evento_todos(self) -> list[Evento]:
        """
        Select todos os eventos na tabela evento
        sql = 'SELECT * FROM evento'
        """
        lista_evento: list[Evento] = []

        sql = "SELECT * FROM evento"

        cursor = self.executar_sql(sql)

        for registro in cursor:
            evento = Evento(
                id=registro[0],
                evento_categoria=self.select_evento_categoria(str(registro[1])),
                evento=registro[2],
                descricao=registro[3],
            )
            lista_evento.append(evento)

        return lista_evento

    # # -----------------------------------------------------------------------
    # DELETAR registro na tabela data_categoria
    ##
    def delete_evento(self, id: int):
        parametro = (id,)
        sql = """
            DELETE FROM
                evento
            WHERE id = ?
            """

        self.executar_sql(sql, parametro)  # .rowcount

    # # -----------------------------------------------------------------------
    # Iserir dados na tabela data_categoria
    ##
    def insert_data_categoria(self, data_categoria: DataCategoria):

        params = (data_categoria.categoria, data_categoria.descricao)

        nova_data_categoria = """
            INSERT INTO 
                data_categoria(categoria, descricao) 
            VALUES(?, ?)
            """

        self.executar_sql(nova_data_categoria, params)  # .rowcount

    # # -----------------------------------------------------------------------
    # DELETAR registro na tabela data_categoria
    ##
    def delete_data_categoria(self, id: int):
        parametro = (id,)
        sql = """
            DELETE FROM
                data_categoria
            WHERE id = ?
            """

        self.executar_sql(sql, parametro)  # .rowcount

    # # -----------------------------------------------------------------------
    # UPDATE registro na tabela data_categoria
    ##
    def update_data_categoria(self, id: int, categoria: str, descricao: str):

        parametros = (categoria, descricao, id)

        sql = """
            UPDATE 
                data_categoria
            SET categoria = ?, descricao = ?
            WHERE id = ?
            """

        self.executar_sql(sql, parametros)  # .rowcount

    # # -----------------------------------------------------------------------
    # Iserir dados na tabela evento_categoria
    ##
    def insert_evento_categoria(self, evento_categoria: EventoCategoria):

        params = (evento_categoria.categoria, evento_categoria.descricao)

        novo_evento_categoria = """
            INSERT INTO 
                evento_categoria(categoria, descricao) 
            VALUES(?,?)
            """

        self.executar_sql(novo_evento_categoria, params)  # .rowcount

    # # -----------------------------------------------------------------------
    # Iserir dados na tabela evento
    ##
    def insert_evento(self, evento: Evento):

        params = (evento.evento, evento.descricao, evento.evento_categoria.id)

        novo_evento = """
            INSERT INTO 
                evento(evento, descricao, evento_categoria_id)
            VALUES(?,?,?)
            """

        self.executar_sql(novo_evento, params)  # .rowcount

    # # -----------------------------------------------------------------------
    # Iserir dados na tabela evento
    ##
    def insert_data(self, nova_data: Data) -> int:

        data_existente: Data = self.select_uma_data(nova_data)

        if not data_existente:
            parametros: tuple = (nova_data.data, nova_data.data_categoria.id)

            sql = """
                INSERT INTO 
                    data(data, data_categoria_id)
                VALUES(?,?)
                """

            data_id = self.executar_sql(sql, parametros).lastrowid
            nova_data.id = data_id

            for evento in nova_data.eventos:
                self.insert_eventos_data(nova_data.id, evento.id)

            return data_id

        return None

    # # -----------------------------------------------------------------------
    # DELETAR registro na tabela data
    ##
    def delete_data(self, data: Data):
        parametro = (data.id,)
        sql = """
            DELETE FROM
                data
            WHERE id = ?
            """

        self.executar_sql(sql, parametro)  # .rowcount


# # nova_data--------------------------------------------------------------
#     def delete_jogo(self, id:int):
#         params = (id,)
#         deletar_um_jogo = "DELETE FROM jogo WHERE id = ?"

#         self.executar_sql(deletar_um_jogo, params)

# # -----------------------------------------------------------------------
#     def update_jogo(self, jogo:Jogo):
#         params = (jogo.data, jogo.campeonato, jogo.time1, jogo.gols1, jogo.time2, jogo.gols2, jogo.id)

#         atualizar_um_jogo = "UPDATE jogo SET data = ?, campeonato = ?, time1 = ?, gols1 = ?, time2 = ?, gols2 = ? WHERE id = ?"

#         self.executar_sql(atualizar_um_jogo, params)

# # -----------------------------------------------------------------------


if __name__ == "__main__":
    dataDB = DataDB()
