from src.modelo.data_categoria import DataCategoria
from src.data.database_singleton import DataDBSingleton


class DataCategoriaDB:

    def __init__(self, dbs: DataDBSingleton) -> None:
        self.dbs = dbs
        self.criar_tabela_data_categoria()

    ##
    # CRIAR TABELA
    ##
    def criar_tabela_data_categoria(self) -> None:
        criar_tabela_data_categoria = """
        CREATE TABLE IF NOT EXISTS data_categoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        categoria TEXT NOT NULL UNIQUE,
        descricao TEXT
        )"""
        self.dbs.executar_sql(criar_tabela_data_categoria)

    # #
    # SELECT_DATA_CATEGORIA_TODOS registros
    ##
    def select_data_categoria_todos(self) -> list[DataCategoria]:
        """
        Select todas as categorias de data na tabela data_categoria
        sql = 'SELECT * FROM data_categoria'
        """
        lista_data_categoria: list[DataCategoria] = []

        lista_de_evento_categoria = "SELECT * FROM data_categoria"

        cursor = self.dbs.executar_sql(lista_de_evento_categoria)

        for registro in cursor:
            data_categoria = DataCategoria(
                id=registro[0], categoria=registro[1], descricao=registro[2]
            )
            lista_data_categoria.append(data_categoria)

        return lista_data_categoria

    # # -----------------------------------------------------------------------
    # Select um registro data_categoria
    ##
    def select_data_categoria(self, id: int) -> DataCategoria:
        parametro = (id,)

        sql = "SELECT * FROM data_categoria WHERE id = ?"
        cursor = self.dbs.executar_sql(sql, parametro)

        registro = cursor.fetchone()

        data_categoria = DataCategoria(
            id=registro[0], categoria=registro[1], descricao=registro[2]
        )

        return data_categoria

    # # -----------------------------------------------------------------------
    # Inserir um registro na tabela data_categoria
    ##
    def insert_data_categoria(self, data_categoria: DataCategoria):

        params = (
            data_categoria.categoria,
            (
                data_categoria.descricao
                if data_categoria.descricao != ""
                else "Não cadastrada"
            ),
        )

        nova_data_categoria = """
            INSERT INTO 
                data_categoria(categoria, descricao) 
            VALUES(?, ?)
            """

        self.dbs.executar_sql(nova_data_categoria, params)  # .rowcount

    # # -----------------------------------------------------------------------
    # DELETAR um registro na tabela data_categoria
    ##
    def delete_data_categoria(self, id: int):
        parametro = (id,)
        sql = """
            DELETE FROM
                data_categoria
            WHERE id = ?
            """

        self.dbs.executar_sql(sql, parametro)  # .rowcount

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

        self.dbs.executar_sql(sql, parametros)  # .rowcount
