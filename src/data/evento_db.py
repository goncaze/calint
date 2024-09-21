from src.data.database_singleton import DataDBSingleton
from src.data.evento_categoria_db import EventoCategoriaDB
from src.modelo.evento_categoria import EventoCategoria
from src.modelo.evento import Evento


class EventoDB:

    def __init__(self, dbs: DataDBSingleton) -> None:
        self.dbs = dbs
        self.eventoCategoriaDB = EventoCategoriaDB(dbs)
        self.criar_tabela_evento()

    ##
    # CRIAR TABELAS
    ##
    def criar_tabela_evento(self) -> None:
        criar_tabela_evento = """CREATE TABLE IF NOT EXISTS evento(
        id INTEGER PRIMARY KEY AUTOINCREMENT,             
        evento_categoria_id INTEGER NOT NULL, 
        evento TEXT NOT NULL UNIQUE,    
        descricao TEXT DEFAULT "Não cadastrada" NOT NULL,
        FOREIGN KEY(evento_categoria_id) REFERENCES evento_categoria(id)
        )"""
        self.dbs.executar_sql(criar_tabela_evento)

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

        self.dbs.executar_sql(sql, parametros)  # .rowcount

    # # -----------------------------------------------------------------------
    # SELECT_EVENTO
    ##
    def select_evento(self, id: int) -> Evento:
        # print(f"\n\n\t\t def select_evento(self, id: int) -> Evento: \n\n")
        """
        Select um evento para um evento especificado (id)
        sql = 'SELECT * FROM evento WHERE id = ?'
        """
        parametro = (id,)  # Tipo tupla
        sql = "SELECT * FROM evento WHERE id = ?"

        cursor = self.dbs.executar_sql(sql, parametro)

        registro = cursor.fetchone()

        # print(f"\n\n\t\t{registro[0] = }\n\n")

        evento = Evento(
            id=registro[0],
            evento_categoria=self.eventoCategoriaDB.select_evento_categoria(
                registro[1]
            ),
            evento=registro[2],
            descricao=registro[3],
        )

        return evento

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

        cursor = self.dbs.executar_sql(sql)

        for registro in cursor:
            evento = Evento(
                id=registro[0],
                evento_categoria=self.eventoCategoriaDB.select_evento_categoria(
                    # str(registro[1])
                    registro[1]
                ),
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

        self.dbs.executar_sql(sql, parametro)  # .rowcount

    # # -----------------------------------------------------------------------
    # Iserir dados na tabela evento
    ##
    def insert_evento(self, evento: Evento):
        # print(f"\t\t\n{evento = }\n\n")
        # print(f"\t\t\n{evento.evento_categoria = }\n\n")

        params = (
            evento.evento,
            (evento.descricao if evento.descricao != "" else "Não cadastrada"),
            evento.evento_categoria.id,
        )

        novo_evento = """
            INSERT INTO 
                evento(evento, descricao, evento_categoria_id)
            VALUES(?,?,?)
            """

        self.dbs.executar_sql(novo_evento, params)  # .rowcount

    # # -----------------------------------------------------------------------
    # Select somente eventos relacionados a uma data específica
    ##
    def select_evento_alguns(self, lista_ids: list[tuple]) -> list[Evento]:

        lista_evento: list[Evento] = []

        for parametro in lista_ids:
            # parametro = id
            sql = "SELECT * FROM evento WHERE id = ?"

            cursor = self.dbs.executar_sql(sql, parametro)

            registro = cursor.fetchone()

            evento = Evento(
                id=registro[0],
                evento_categoria=self.eventoCategoriaDB.select_evento_categoria(
                    registro[1]
                ),
                evento=registro[2],
                descricao=registro[3],
            )
            lista_evento.append(evento)

        return lista_evento
