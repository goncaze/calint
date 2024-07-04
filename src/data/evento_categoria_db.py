from src.modelo.evento_categoria import EventoCategoria
from src.data.database_singleton import DataDBSingleton


class EventoCategoriaDB:

    def __init__(self, dbs: DataDBSingleton) -> None:
        self.dbs = dbs
        self.criar_tabela_evento_categoria()

    ##
    # CRIAR TABELAS
    ##
    def criar_tabela_evento_categoria(self) -> None:
        criar_tabela_evento_categoria = """CREATE TABLE IF NOT EXISTS evento_categoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        categoria TEXT NOT NULL UNIQUE,
        descricao TEXT DEFAULT "Não cadastrada" NOT NULL
        )"""
        self.dbs.executar_sql(criar_tabela_evento_categoria)

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
        resultado = self.dbs.executar_sql(lista_de_evento_categoria)

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

        cursor = self.dbs.executar_sql(sql, parametro)

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

        self.dbs.executar_sql(sql, parametros)  # .rowcount

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

        self.dbs.executar_sql(sql, parametro)  # .rowcount

    # # -----------------------------------------------------------------------
    # Iserir dados na tabela evento_categoria
    ##
    def insert_evento_categoria(self, evento_categoria: EventoCategoria):

        params = (
            evento_categoria.categoria,
            (
                evento_categoria.descricao
                if evento_categoria.descricao != ""
                else "Não cadastrada"
            ),
        )

        novo_evento_categoria = """
            INSERT INTO 
                evento_categoria(categoria, descricao) 
            VALUES(?,?)
            """

        self.dbs.executar_sql(novo_evento_categoria, params)  # .rowcount
