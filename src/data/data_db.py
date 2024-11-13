from src.modelo.data import Data
from src.modelo.evento import Evento
from src.data.evento_db import EventoDB
from src.data.data_categoria_db import DataCategoriaDB
from src.data.database_singleton import DataDBSingleton
from datetime import datetime
from datetime import timedelta


class DataDB:

    def __init__(self, dbs: DataDBSingleton) -> None:
        self.dbs = dbs
        self.dataCategoriaDB = DataCategoriaDB(dbs)
        self.eventoDB = EventoDB(dbs)
        self.criar_tabela_data()
        self.criar_tabela_evento_data()

    ##
    # EXCLUIR TABELAS
    ##
    def excluir_tabela_data(self) -> None:
        excluir_tabela = "DROP TABLE IF EXISTS data"
        self.dbs.executar_sql(excluir_tabela)

    def excluir_tabela_evento_data(self) -> None:
        excluir_tabela_evento = "DROP TABLE IF EXISTS evento_data"
        self.dbs.executar_sql(excluir_tabela_evento)

    ##
    # CRIAR TABELAS
    ##
    def criar_tabela_data(self) -> None:
        criar_tabela_data = """CREATE TABLE IF NOT EXISTS data(
            id INTEGER PRIMARY KEY, 
            data TEXT NOT NULL UNIQUE
        )"""
        # data_categoria_id INTEGER NOT NULL,
        # FOREIGN KEY(data_categoria_id) REFERENCES data_categoria(id) ON DELETE RESTRICT
        self.dbs.executar_sql(criar_tabela_data)
        self.preencher_db_calendario()

    def criar_tabela_evento_data(self) -> None:
        criar_tabela_evento_data = """CREATE TABLE IF NOT EXISTS evento_data(
            data_id INTEGER NOT NULL, 
            evento_id INTEGER NOT NULL, 
            FOREIGN KEY(data_id) REFERENCES data(id),
            FOREIGN KEY(evento_id) REFERENCES evento(id)
        )"""
        self.dbs.executar_sql(criar_tabela_evento_data)

    ###
    # Testar após a criação da tabela data
    #
    def preencher_db_calendario(self) -> None:
        sql = "SELECT * FROM data LIMIT 1"
        cursor = self.dbs.executar_sql(sql)

        if not cursor.fetchone():
            # print("if not cursor.fetchone(): TRUE")
            parametros = []

            hoje = datetime.now().date()

            data_inicial = str(hoje.year - 1) + "-1-1"
            data_final = str(hoje.year + 1) + "-12-31"
            data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
            data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

            dia = 0

            while True:
                dia += 1

                data_incrementada = data_inicial + timedelta(dia)

                if data_incrementada == data_final + timedelta(1):
                    break
                else:
                    parametros.append((data_incrementada.strftime("%Y-%m-%d"),))

            self.insert_data_muitos(parametros)

        # else:
        #     print("if not cursor.fetchone(): FALSE")

    # # # -----------------------------------------------------------------------
    # # UPDATE registro na tabela data
    # ##
    # def update_data(self, data: Data):
    #     parametros = (data.cor, data.id)

    #     sql = """
    #         UPDATE
    #             data
    #         SET
    #             cor = ?
    #         WHERE
    #             id = ?
    #         """

    #     self.dbs.executar_sql(sql, parametros)  # .rowcount
    #     self.update_data_evento(data)

    def update_data_evento(self, data: Data):
        lista_id_eventos_atual = self.select_id_eventos_por_id_data(data)

        nova_lista_id_eventos: list[int] = []
        print("\n\t\t DATA")
        print(f"{data = } \n\n")

        for evento in data.eventos:
            print("----  ----  ----  -----  ----  -----")
            print(f"{evento = }")
            nova_lista_id_eventos.append(evento.id)

        # print(f"\n\n {type(lista_id_eventos_atual) = }")
        # print("lista_id_eventos_atual == None ")
        # print(f"{lista_id_eventos_atual == None }")
        # print("\n{lista_id_eventos_atual is not None }")
        # print(f"{lista_id_eventos_atual is not None }")
        print("\n\n")

        if lista_id_eventos_atual is not None:
            print("\n\t{lista_id_eventos_atual is not None }")
            print(f"\t\t{lista_id_eventos_atual is not None }")
            for id_evento_atual in lista_id_eventos_atual:
                if id_evento_atual not in nova_lista_id_eventos:
                    self.delete_evento_data(data, id_evento_atual)

            for evento_novo_id in nova_lista_id_eventos:
                if evento_novo_id not in lista_id_eventos_atual:
                    self.insert_eventos_data(data.id, evento_novo_id)

        else:
            for evento_novo_id in nova_lista_id_eventos:
                print("-----------------------------")
                print(f"{data.id = }")
                print(f"{evento_novo_id = }")
                print("-----------------------------")
                self.insert_eventos_data(data.id, evento_novo_id)

    # # -----------------------------------------------------------------------
    # DELETAR registro na tabela data
    ##
    def delete_evento_data(self, data: Data, evento_id: int):
        parametros = (data.id, evento_id)
        sql = """
            DELETE FROM
                evento_data
            WHERE 
                data_id = ? and evento_id = ?
            """
        self.dbs.executar_sql(sql, parametros)  # .rowcount

    # # -----------------------------------------------------------------------
    # Select ID de eventos de uma data específica
    ##
    def select_id_eventos_por_id_data(self, data: Data) -> list[int]:

        parametro: tuple = None

        if data.id is not None and data.id > 0:
            parametro = (data.id,)
            sql = "SELECT evento_id FROM evento_data WHERE data_id = ?"
        else:
            return None

        cursor = self.dbs.executar_sql(sql, parametro)

        lista_id_eventos: list[int] = []

        for resultado in cursor.fetchall():
            lista_id_eventos.append(resultado[0])

        return lista_id_eventos

    # # # -----------------------------------------------------------------------
    # # Select EVENTOS de uma data específica
    # ##
    # def select_eventos_por_id_data(self, lista_id_eventos: list[int]) -> list[Evento]:

    #     parametro: tuple = None

    #     for id_evento in lista_id_eventos:
    #         parametro = (id_evento,)
    #         sql = "SELECT * FROM evento WHERE data_id = ?"
    #     else:
    #         return None

    #     cursor = self.dbs.executar_sql(sql, parametro)

    #     lista_eventos: list[Evento] = []

    #     for resultado in cursor.fetchall():
    #         evento = Evento()
    #         lista_eventos.append(resultado[0])

    #     return lista_eventos

    # # -----------------------------------------------------------------------
    # SELECT todas as DATAS
    ##
    def select_data_todas(self) -> list[Data]:
        """
        Select todos os eventos na tabela data
        sql = 'SELECT * FROM data'
        """
        lista_data: list[Data] = []

        sql = """
            SELECT 
                id, data
            FROM 
                data as dt
            ORDER BY 
                dt.data    
            """

        cursor = self.dbs.executar_sql(sql)

        for registro in cursor:
            data = Data(
                id=registro[0],
                data=registro[1],
                # data_categoria=self.dataCategoriaDB.select_data_categoria(registro[2]),
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
        # print(f"\n\n\t\t{data = }")
        # print("\n\t\t{data.data is not None and data.data != ""}")
        # print(f"\n\t\t{data.data is not None and data.data != ""} \n\n")

        if data.id is not None and data.id > 0:
            # print("\n\n\t\t if data.id is not None and data.id > 0: ")
            # print(f"\t\t {data.id is not None and data.id > 0} \n\n")
            parametros = (data.id,)
            # sql = "SELECT * FROM data WHERE id = ?"
            ############## # id, strftime('%d/%m/%Y', data) as data # #############
            sql = """
                SELECT                     
                    id, data
                FROM 
                    data 
                WHERE 
                    id = ?
            """
        elif data.data is not None and data.data != "":
            # print("\n\n\t\t QUASE LÁ ONDE DEVE ENTRAR '' ")
            # print(f"\t\t {data.data is not None and data.data != ""} \n\n")
            # parametros = (
            #     datetime.strftime(datetime.strptime(data.data, "%d/%m/%Y"), "%Y-%m-%d"),
            # )
            parametros = (data.data,)

            sql = """
                SELECT 
                    id, data
                FROM 
                    data
                WHERE 
                    data = ?
            """
            # print("{sql = }")
            # print(f"{sql}")
            # print(f"\n{data.data = }\n")

        else:
            return None

        # if sql is not None:
        #     print("\n{sql is not None}")
        #     print(f"{sql is not None}\n")
        cursor = self.dbs.executar_sql(sql, parametros)

        for registro in cursor:
            data = Data(
                id=registro[0],
                # data=datetime.strftime(registro[1], "%d/%m/%Y"),
                data=registro[1],
                # data_categoria=self.dataCategoriaDB.select_data_categoria(
                #     registro[2]
                # ),
                eventos=self.select_eventos_por_data(registro[0]),
            )
            # print("\n\n\t\t ENTROU ONDE DEVE ENTRAR '' ")
            # print(f"\t\t {data.id = } \n\n")
            # for evento in data.eventos:
            #     print(evento)

            return data

        return None

    # # -----------------------------------------------------------------------
    # Iserir dados na tabela data
    ##
    def insert_data(self, nova_data: Data) -> int:

        # print(f"\n\n\t\t{nova_data = }\n\n")

        data_existente: Data = self.select_uma_data(nova_data)

        if not data_existente:
            parametros: tuple = (
                ## datetime.strftime(nova_data.data, "%Y/%m/%d"),
                # datetime.strftime(
                #     datetime.strptime(nova_data.data, "%d/%m/%Y"), "%Y-%m-%d"
                # ),
                nova_data.data,
            )

            sql = """
                INSERT INTO 
                    data(data)
                VALUES(?)
                """

            data_id = self.dbs.executar_sql(sql, parametros).lastrowid
            nova_data.id = data_id

            for evento in nova_data.eventos:
                self.insert_eventos_data(nova_data.id, evento.id)

            return data_id

        return None

    # # -----------------------------------------------------------------------
    # Iserir dados na tabela data
    ##
    def insert_data_muitos(self, parametros: list[tuple]) -> None:

        sql = """
            INSERT INTO 
                data(data)
            VALUES(?)
            """

        self.dbs.executar_sql_muitos(sql, parametros)

        # return None

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

        self.dbs.executar_sql(sql, parametros)

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

        self.dbs.executar_sql(sql, parametro)  # .rowcount

    # # -----------------------------------------------------------------------
    # Select eventos de uma data específica
    ##
    def select_eventos_por_data(self, data_id: int) -> list[Evento]:
        parametro: tuple = None

        if data_id is not None and data_id > 0:
            parametro = (data_id,)
            sql = "SELECT evento_id FROM evento_data WHERE data_id = ?"
        else:
            return None

        cursor = self.dbs.executar_sql(sql, parametro)

        lista_ids = cursor.fetchall()

        return self.eventoDB.select_evento_alguns(lista_ids)

    # # -----------------------------------------------------------------------
    # SELECT somente a menor DATA
    ##
    def select_menor_data(self) -> Data:
        """
        Seleciona a menor data ou data mais antiga.
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
        else:
            return None

        if sql:
            cursor = self.dbs.executar_sql(sql, parametros)

            for registro in cursor:
                data = Data(
                    id=registro[0],
                    data=registro[1],
                    data_categoria=self.dataCategoriaDB.select_data_categoria(
                        registro[2]
                    ),
                    eventos=self.select_eventos_por_data(registro[0]),
                )
                return data

        return None
