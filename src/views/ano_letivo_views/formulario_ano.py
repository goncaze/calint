import flet as ft
from datetime import datetime
from datetime import timedelta
from src.data.database_singleton import DataDBSingleton
from src.modelo.data import Data

# from src.modelo.data_categoria import DataCategoria
from src.modelo.evento import Evento
from src.modelo.evento_categoria import EventoCategoria
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton

# from src.data.data_categoria_db import DataCategoriaDB
from src.data.evento_db import EventoDB
from src.data.evento_categoria_db import EventoCategoriaDB


class FormularioAno(ft.Card):
    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.page: ft.Page = page
        self.data_db: DataDB = DataDB(dbs)
        # self.dataCategoria_db :DataCategoriaDB = DataCategoriaDB(dbs)
        self.evento_db: EventoDB = EventoDB(dbs)
        self.evento_cat_db: EventoCategoriaDB = EventoCategoriaDB(dbs)

        self.ttf_inicio_letivo = ft.TextField(
            label="Início ano letivo", value="05-02-2024", expand=True
        )
        self.ttf_fim_letivo = ft.TextField(
            label="Fim ano letivo", value="10-12-2024", expand=True
        )
        self.ttf_inicio_ferias_1 = ft.TextField(
            label="Início férias coletivas 1", value="08-07-2024", expand=True
        )
        self.ttf_fim_ferias_1 = ft.TextField(
            label="Fim férias coletivas 1", value="22-07-2024", expand=True
        )
        self.ttf_inicio_ferias_2 = ft.TextField(
            label="Início férias coletivas 2", value="01-01-2025", expand=True
        )
        self.ttf_fim_ferias_2 = ft.TextField(
            label="Fim férias coletivas 2", value="31-01-2025", expand=True
        )

        self.dtpkr_i_letivo = ft.DatePicker(
            on_change=self.change_date_i_letivo,
        )
        self.dtpkr_f_letivo = ft.DatePicker(
            on_change=self.change_date_f_letivo,
        )
        self.dtpkr_i_ferias_1 = ft.DatePicker(
            on_change=self.change_date_i_ferias_1,
        )
        self.dtpkr_f_ferias_1 = ft.DatePicker(
            on_change=self.change_date_f_ferias_1,
        )
        self.dtpkr_i_ferias_2 = ft.DatePicker(
            on_change=self.change_date_i_ferias_2,
        )
        self.dtpkr_f_ferias_2 = ft.DatePicker(
            on_change=self.change_date_f_ferias_2,
        )

        self.icb_letivo_1 = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_i_letivo),
        )

        self.icb_letivo_2 = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_f_letivo),
        )

        self.icb_i_ferias_1 = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_i_ferias_1),
        )

        self.icb_f_ferias_1 = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_f_ferias_1),
        )

        self.icb_i_ferias_2 = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_i_ferias_2),
        )

        self.icb_f_ferias_2 = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_f_ferias_2),
        )

        self.ttb_salvar = ft.TextButton(text="Salvar", on_click=self.salvar)
        # self.ttb_salvar = ft.TextButton(text="Salvar", on_click=self.resetar_banco)

        self.linha_ttb = ft.Row(
            controls=[
                self.ttb_salvar,
            ],
            alignment=ft.MainAxisAlignment.END,
        )

        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.ttf_inicio_letivo,
                        self.icb_letivo_1,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_fim_letivo,
                        self.icb_letivo_2,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_inicio_ferias_1,
                        self.icb_i_ferias_1,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_fim_ferias_1,
                        self.icb_f_ferias_1,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_inicio_ferias_2,
                        self.icb_i_ferias_2,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_fim_ferias_2,
                        self.icb_f_ferias_2,
                    ],
                ),
                self.linha_ttb,
            ]
        )

    def change_date_i_letivo(self, e: ft.ControlEvent):
        self.ttf_inicio_letivo.value = self.dtpkr_i_letivo.value.strftime("%d-%m-%Y")
        self.ttf_inicio_letivo.update()

    def change_date_f_letivo(self, e: ft.ControlEvent):
        self.ttf_fim_letivo.value = self.dtpkr_f_letivo.value.strftime("%d-%m-%Y")
        self.ttf_fim_letivo.update()

    def change_date_i_ferias_1(self, e: ft.ControlEvent):
        self.ttf_inicio_ferias_1.value = self.dtpkr_i_ferias_1.value.strftime(
            "%d-%m-%Y"
        )
        self.ttf_inicio_ferias_1.update()

    def change_date_f_ferias_1(self, e: ft.ControlEvent):
        self.ttf_fim_ferias_1.value = self.dtpkr_f_ferias_1.value.strftime("%d-%m-%Y")
        self.ttf_fim_ferias_1.update()

    def change_date_i_ferias_2(self, e: ft.ControlEvent):
        self.ttf_inicio_ferias_2.value = self.dtpkr_i_ferias_2.value.strftime(
            "%d-%m-%Y"
        )
        self.ttf_inicio_ferias_2.update()

    def change_date_f_ferias_2(self, e: ft.ControlEvent):
        self.ttf_fim_ferias_2.value = self.dtpkr_f_ferias_2.value.strftime("%d-%m-%Y")
        self.ttf_fim_ferias_2.update()

    # def limpar_formulario(self):
    #     self.ttf_titulo.value = ""
    #     self.ttf_genero.value = ""
    #     self.ttf_lancamento.value = ""
    #     self.update()

    def validar(self) -> bool:
        is_valido: bool = True
        if self.ttf_inicio_letivo.value == "":
            is_valido = False
            self.ttf_inicio_letivo.error_text = "Data do início do ano letivo"

        if self.ttf_fim_letivo.value == "":
            is_valido = False
            self.ttf_fim_letivo.error_text = "Data do fim do ano letivo"

        if self.ttf_inicio_ferias_1.value == "":
            is_valido = False
            self.ttf_inicio_ferias_1.error_text = "Data de início das férias 1"

        if self.ttf_inicio_ferias_2.value == "":
            is_valido = False
            self.ttf_inicio_ferias_2.error_text = "Data de início das férias 2"

        if self.ttf_fim_ferias_1.value == "":
            is_valido = False
            self.ttf_fim_ferias_1.error_text = "Data de fim das férias 1"

        if self.ttf_fim_ferias_2.value == "":
            is_valido = False
            self.ttf_fim_ferias_2.error_text = "Data de fim das férias 2"

        return is_valido

    def salvar(self, e):
        if self.validar():
            ##
            #  Resetar tabelas
            #
            self.resetar_tabelas()

            ##
            #  Inserir categoria de evento no banco de dados
            #
            evento_cat_Letivo = EventoCategoria(categoria="Letivo", cor="#C8EBB0")
            evento_cat_ferias = EventoCategoria("Férias", cor="#7DD6EB")

            # print(f"\n\n\t {evento_cat_Letivo = } \n\n")
            # print(f"evento_cat_Letivo = {evento_cat_Letivo} \n\n")
            # print(f"\n\n\t {evento_cat_ferias = } \n\n")
            # print(f"evento_cat_ferias = {evento_cat_ferias} \n\n")

            evento_cat_Letivo.id = self.evento_cat_db.insert_evento_categoria(
                evento_cat_Letivo
            )
            evento_cat_ferias.id = self.evento_cat_db.insert_evento_categoria(
                evento_cat_ferias
            )

            ##
            #  Inserir eventos no banco de dados
            #
            evento_letivo: Evento = Evento(evento_cat_Letivo, "Dia letivo")
            evento_i_letivo: Evento = Evento(evento_cat_Letivo, "Início ano letivo")
            evento_f_letivo: Evento = Evento(evento_cat_Letivo, "Fim ano letivo")
            evento_ferias: Evento = Evento(evento_cat_ferias, "Férias")
            evento_i_ferias_1: Evento = Evento(evento_cat_ferias, "Início férias 1")
            evento_f_ferias_1: Evento = Evento(evento_cat_ferias, "Fim férias 1")
            evento_i_ferias_2: Evento = Evento(evento_cat_ferias, "Início férias 2")
            evento_f_ferias_2: Evento = Evento(evento_cat_ferias, "Fim férias 2")

            evento_letivo.id = self.evento_db.insert_evento(evento_letivo)
            evento_ferias.id = self.evento_db.insert_evento(evento_ferias)

            evento_i_letivo.id = self.evento_db.insert_evento(evento_i_letivo)
            evento_f_letivo.id = self.evento_db.insert_evento(evento_f_letivo)

            evento_i_ferias_1.id = self.evento_db.insert_evento(evento_i_ferias_1)
            evento_f_ferias_1.id = self.evento_db.insert_evento(evento_f_ferias_1)

            evento_i_ferias_2.id = self.evento_db.insert_evento(evento_i_ferias_2)
            evento_f_ferias_2.id = self.evento_db.insert_evento(evento_f_ferias_2)

            ##
            #  Preparar datas para inserção
            #
            # Data do início letivo
            data_i_letivo = self.data_db.select_uma_data(
                Data(
                    data=datetime.strftime(
                        datetime.strptime(self.ttf_inicio_letivo.value, "%d-%m-%Y"),
                        "%Y-%m-%d",
                    )
                )
            )
            data_i_letivo.eventos = [evento_i_letivo, evento_letivo]


            # Data do fim letivo
            data_f_letivo = self.data_db.select_uma_data(
                Data(
                    data=datetime.strftime(
                        datetime.strptime(self.ttf_fim_letivo.value, "%d-%m-%Y"),
                        "%Y-%m-%d",
                    )
                )
            )
            data_f_letivo.eventos = [evento_f_letivo, evento_letivo]


            # Data do início das férias
            data_i_ferias_1 = self.data_db.select_uma_data(
                Data(
                    data=datetime.strftime(
                        datetime.strptime(self.ttf_inicio_ferias_1.value, "%d-%m-%Y"),
                        "%Y-%m-%d",
                    )
                )
            )
            data_i_ferias_1.eventos = [evento_i_ferias_1, evento_ferias]


            # Data do fim das férias
            data_f_ferias_1 = self.data_db.select_uma_data(
                Data(
                    data=datetime.strftime(
                        datetime.strptime(self.ttf_fim_ferias_1.value, "%d-%m-%Y"),
                        "%Y-%m-%d",
                    )
                )
            )
            data_f_ferias_1.eventos = [evento_f_ferias_1, evento_ferias]


            # Data do início das férias parte 2
            data_i_ferias_2 = self.data_db.select_uma_data(
                Data(
                    data=datetime.strftime(
                        datetime.strptime(self.ttf_inicio_ferias_2.value, "%d-%m-%Y"),
                        "%Y-%m-%d",
                    )
                )
            )
            data_i_ferias_2.eventos = [evento_i_ferias_2, evento_ferias]


            # Data do fim das férias parte 2
            data_f_ferias_2 = self.data_db.select_uma_data(
                Data(
                    data=datetime.strftime(
                        datetime.strptime(self.ttf_fim_ferias_2.value, "%d-%m-%Y"),
                        "%Y-%m-%d",
                    )
                )
            )
            data_f_ferias_2.eventos = [evento_f_ferias_2, evento_ferias]


            ##
            #  Atualizar eventos_datas na tabela evento_data
            #
            self.data_db.update_data_evento(data_i_letivo)
            self.data_db.update_data_evento(data_f_letivo)
            self.data_db.update_data_evento(data_i_ferias_1)
            self.data_db.update_data_evento(data_f_ferias_1)
            self.data_db.update_data_evento(data_i_ferias_2)
            self.data_db.update_data_evento(data_f_ferias_2)

            ##
            #  Inserir datas das férias
            #
            lista_dias_ferias_1: list[datetime.date] = self.preencher_db_ferias(
                data_i_ferias_1, data_f_ferias_1, evento_ferias
            )

            lista_dias_ferias_2: list[datetime.date] = self.preencher_db_ferias(
                data_i_ferias_2, data_f_ferias_2, evento_ferias
            )

            ##
            #  Inserir datas para os dias letivos
            #
            self.preencher_db_dias_letivos(
                data_i_letivo,
                data_f_letivo,
                evento_letivo,
                lista_dias_ferias_1,
                lista_dias_ferias_2,
            )

            self.page.go("/")
        else:
            self.update()


    ###
    #   Configurar as datas de dias letivos no database 
    #
    def preencher_db_dias_letivos(
        self,
        data_i_letivo: Data,
        data_f_letivo: Data,
        evento_letivo: Evento,
        lista_dias_ferias_1: list[datetime.date],
        lista_dias_ferias_2: list[datetime.date],
    ):
        dia = 0
        dias_letivos = 1


        # Converter a string para objeto de data
        dt_i_letivo = datetime.strptime(data_i_letivo.data, "%Y-%m-%d").date()
        dt_f_letivo = datetime.strptime(data_f_letivo.data, "%Y-%m-%d").date()

        # while dias_letivos <= 200:
        while True:
            dia += 1

            data_incrementada: datetime.date = dt_i_letivo + timedelta(dia)

            if data_incrementada == dt_f_letivo:
                break

            if data_incrementada.isoweekday() < 6:
                if (data_incrementada not in lista_dias_ferias_1) and (
                    data_incrementada not in lista_dias_ferias_2
                ):
                    ##
                    #  inserir dia letivo na tabela
                    data_com_id = self.data_db.select_uma_data(
                        Data(data=data_incrementada.strftime("%Y-%m-%d"))
                    )
                    data_com_id.eventos = [evento_letivo]
                                        
                    # novo_dia_letivo = Data(
                    #     data=data_incrementada.strftime("%Y-%m-%d"),
                    #     eventos=[evento_letivo],
                    # )

                    self.data_db.update_data_evento(data_com_id)

                #### >>>>>>>>>> print(f"{data_incrementada = }")
                dias_letivos += 1


    ###
    #   Configurar as datas de férias no database 
    #
    def preencher_db_ferias(
        self, data_i_ferias: Data, data_f_ferias: Data, evento_ferias: Evento
    ) -> list[datetime.date]:      

        lista_dias_ferias: list[datetime.date] = [datetime.strptime(data_i_ferias.data, "%Y-%m-%d").date()]

        dt_i_ferias = datetime.strptime(data_i_ferias.data, "%Y-%m-%d").date()
        dt_f_ferias = datetime.strptime(data_f_ferias.data, "%Y-%m-%d").date()

        dia = 0

        while True:
            dia += 1

            data_incrementada = dt_i_ferias + timedelta(dia)

            if data_incrementada == dt_f_ferias:
                # última data inserida previamente
                break
            else:
                lista_dias_ferias.append(data_incrementada)

                ##
                #  inserir dia de férias na tabela
                data_com_id = self.data_db.select_uma_data(
                    Data(data=data_incrementada.strftime("%Y-%m-%d"))
                )
                data_com_id.eventos = [evento_ferias]

                # self.data_db.insert_data(nova_data)
                self.data_db.update_data_evento(data_com_id)

        return lista_dias_ferias


    ###
    #   Excluir tabelas e recriá-las 
    #
    def resetar_tabelas(self):
        self.data_db.excluir_tabela_evento_data()
        self.evento_db.excluir_tabela()
        self.evento_cat_db.excluir_tabela()
        self.data_db.excluir_tabela_data()

        self.data_db.criar_tabela_data()
        self.evento_cat_db.criar_tabela_evento_categoria()
        self.evento_db.criar_tabela_evento()
        self.data_db.criar_tabela_evento_data()

    ###
    # Testar na após a criação da tabela data
    #
    def resetar_banco(self, e):
        self.resetar_tabelas()

    # ###
    # # Testar na após a criação da tabela data
    # #
    # def preencher_db_calendario(self) -> None:

    #     hoje = datetime.now().date()

    #     data_inicial = str(hoje.year - 1) + "-1-1"
    #     data_final = str(hoje.year + 1) + "-12-31"

    #     data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
    #     data_final = datetime.strptime(data_final, "%Y-%m-%d").date()

    #     dia = 0

    #     while True:
    #         dia += 1

    #         # data = datetime.strftime(
    #         #     datetime.strptime(data_i_ferias.data,"%d/%m/%Y") +
    #         #     timedelta(dia), "%d/%m/%Y"
    #         # )
    #         data_incrementada = data_inicial + timedelta(dia)

    #         # lista_dias_ferias.append(data_incrementada)

    #         #### >>>>>>>>>> print(f"{data_incrementada = }")

    #         if data_incrementada == data_final + timedelta(1):
    #             # última data inserida previamente
    #             break
    #         else:
    #             ##
    #             #  inserir dia na tabela data
    #             nova_data = Data(data=data_incrementada.strftime("%Y-%m-%d"))
    #             self.data_db.insert_data(nova_data)
