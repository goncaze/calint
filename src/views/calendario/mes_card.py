import flet as ft
import datetime
import calendar
from src.views.calendario.cartao import Cartao
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton
from src.modelo.data import Data
from src.modelo.evento import Evento
from src.modelo.evento_categoria import EventoCategoria


class MesCard(Cartao):

    def __init__(
        self,
        page: ft.Page,
        dbs: DataDBSingleton,
        ano: int = 2024,
        mes: int = 10,
        todas_datas: list[Data] = None,
        todas_dt_literal: list[str] = None,
    ):
        super().__init__()
        self.page = page
        self.page.expand = False
        self.width = 350

        self.ano = ano
        self.mes = mes
        self.cor: set = set()
        self.legendas: set = set()
        self.todas_datas: list[Data] = todas_datas
        self.todas_dt_literal: list[str] = todas_dt_literal
        self.titulo_mes = f"{calendar.month_name[mes].capitalize()} de {ano}"

        self.obj_calendar_d0 = calendar.Calendar(firstweekday=6)
        # obj_calendar_d1 = calendar.Calendar(firstweekday=1)
        calendar.setfirstweekday(calendar.SUNDAY)
        self.dbs = dbs
        self.data_db = DataDB(self.dbs)

        ###
        # As listas de containers representam as colunas dos dias da semana.
        # Cada unidade de container contém os dias da semana e o nome do dia.
        #
        self.lista_container_00 = [
            ft.Container(
                content=ft.Text(value="DOM", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_01 = [
            ft.Container(
                content=ft.Text(value="SEG", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_02 = [
            ft.Container(
                content=ft.Text(value="TER", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_03 = [
            ft.Container(
                content=ft.Text(value="QUA", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_04 = [
            ft.Container(
                content=ft.Text(value="QUI", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_05 = [
            ft.Container(
                content=ft.Text(value="SEX", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_06 = [
            ft.Container(
                content=ft.Text(value="SAB", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]

        ###
        # Essa lista dos containers serve para rodar um loop que irá gerar
        # os containers contendo os dias do mês.
        #
        self.listas_containers: list[list] = [
            self.lista_container_00,
            self.lista_container_01,
            self.lista_container_02,
            self.lista_container_03,
            self.lista_container_04,
            self.lista_container_05,
            self.lista_container_06,
        ]

        ###
        # Atributo coluna para conter as cores e o evento
        #
        self.coluna_de_eventos: ft.Column = ft.Column()

        self.preencher_dias()

        ###
        # As colunas para cada dia da semana contendo os dias
        # do mês que estão nas listas de conteiners.
        #
        self.coluna_00 = ft.Column(self.lista_container_00, expand=True)
        self.coluna_01 = ft.Column(self.lista_container_01, expand=True)
        self.coluna_02 = ft.Column(self.lista_container_02, expand=True)
        self.coluna_03 = ft.Column(self.lista_container_03, expand=True)
        self.coluna_04 = ft.Column(self.lista_container_04, expand=True)
        self.coluna_05 = ft.Column(self.lista_container_05, expand=True)
        self.coluna_06 = ft.Column(self.lista_container_06, expand=True)

        ###
        # Uma Row para agrupar as colnas antes de incluir no Card.
        #
        self.linha: ft.Row = ft.Row(
            controls=[
                self.coluna_00,
                self.coluna_01,
                self.coluna_02,
                self.coluna_03,
                self.coluna_04,
                self.coluna_05,
                self.coluna_06,
            ]
        )

        self.content = ft.Container(
            margin=10,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(value=self.titulo_mes),
                                alignment=ft.alignment.center,
                                expand=True,
                            ),
                        ],
                    ),
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            self.coluna_00,
                            self.coluna_01,
                            self.coluna_02,
                            self.coluna_03,
                            self.coluna_04,
                            self.coluna_05,
                            self.coluna_06,
                        ],
                    ),
                ]
            ),
        )

    def filtrar_linha_cor_legenda(self, lista_eventos: list[Evento]) -> None:
        for evento in lista_eventos:
            if evento.evento not in self.legendas:
                # print(" def filtrar_linha_cor_legenda(self, lista_eventos: list[Evento])->None:")
                self.legendas.add(evento.evento)
                self.cor.add(evento.evento_categoria.cor)

                cntn_cor = ft.Container(
                    width=30, height=25, bgcolor=evento.evento_categoria.cor
                )
                legenda = ft.Text(value=evento.evento)

                # linha_cor_legenda = ft.Row( controls = [ cntn_cor, legenda ] )
                self.coluna_de_eventos.controls.append(  # ft.Text('Teste')
                    # self.setar_linha_cor_legenda( evento.evento_categoria.cor, evento )
                    ft.Row(controls=[cntn_cor, legenda])
                )

    def setar_linha_cor_legenda(
        self, cor: str = "#eee222", evento: str = "Legenda"
    ) -> ft.Row:
        cntn_cor = ft.Container(width=30, height=25, bgcolor=cor)
        legenda: str = evento

        linha_cor_legenda = ft.Row(controls=[cntn_cor, legenda])

        return linha_cor_legenda

    def determinar_cor_data(self, dia: int) -> str:
        # # print(f"{self.todas_dt_literal = }")
        # # print(f"{len(self.todas_dt_literal) = }")
        # print(f"{dia = }")
        # print(f"{self.mes = }")
        # print(f"{self.ano = }")

        cor = ""
        data_calendario = datetime.date(self.ano, self.mes, dia).strftime("%Y-%m-%d")
        # print("\n\n--------------")
        # print(f"\n\t\tdata_calendario")
        # print(f"\t\t{data_calendario = }")
        # print("--------------\n\n")

        if calendar.weekday(self.ano, self.mes, dia) in (5, 6):
            # print("\n\n--------------------------------------------------------")
            # print("\t\tif calendar.weekday(self.ano, self.mes, dia) in (5, 6):")
            # print(f"\t\t{calendar.weekday(self.ano, self.mes, dia) = }")
            # print(f"\t\t{calendar.weekday(self.ano, self.mes, dia) in (5, 6) }")
            # print("--------------------------------------------------------\n\n")
            cor = "#ea9999"
        elif data_calendario in self.todas_dt_literal:
            # print("\n\n--------------")
            # print(f" elif data_calendario in self.todas_dt_literal: ")
            # print(f"{data_calendario = }")
            # print(f"{data_calendario in self.todas_dt_literal = }")
            # print("--------------\n\n")

            indice = self.todas_dt_literal.index(data_calendario)

            print("if self.todas_datas[indice].eventos:")
            print(f" {len(self.todas_datas[indice].eventos) = }")
            for ev in self.todas_datas[indice].eventos:
                print(f"{ev = }")

            if self.todas_datas[indice].eventos:

                cor = self.todas_datas[indice].eventos[-1].evento_categoria.cor
                self.filtrar_linha_cor_legenda(self.todas_datas[indice].eventos)

        return cor

    ##
    # Encapsula o dia do mês dentro de um container e o retorna como resultado.
    # Dias zero são encapsulados sem borda e valor.
    #
    def container(self, dia: int) -> ft.Container:
        if dia > 0:
            container = ft.Container(
                content=ft.Text(value=dia),
                bgcolor=self.determinar_cor_data(dia),  #
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
                expand=True,
                alignment=ft.alignment.center,
            )
        else:
            container = ft.Container(
                content=ft.Text(value=""),
                expand=True,
                alignment=ft.alignment.center,
            )

        return container

    ##
    # Para cada um dos sete dias da semana existe uma lista de containers
    # contendo os dias da semana do mês. Por exemplo, self.lista_container_01
    # contém todos os dias da segunda-feira de um determinado mês.
    #
    def preencher_dias(self):
        i = 0
        # todas_datas = self.data_db.select_data_todas()

        for dia in self.obj_calendar_d0.itermonthdays(self.ano, self.mes):
            if i < 7:
                self.listas_containers[i].append(self.container(dia))
                # print(f"{dia}", end="\t")
                i += 1
            else:
                # print(f"\n{dia}", end="\t")
                i = 1
                self.listas_containers[0].append(self.container(dia))

        # self.content = ft.Text("TESTADO")

    #     self.icb_editar = ft.IconButton(
    #         icon=ft.icons.UPDATE,
    #         icon_color="blue",
    #         icon_size=25,
    #         tooltip="Update record",
    #         on_click=self.editar,
    #     )

    #     self.icb_excluir = ft.IconButton(
    #         icon=ft.icons.DELETE_FOREVER_ROUNDED,
    #         icon_color="pink600",
    #         icon_size=25,
    #         tooltip="Delete record",
    #         on_click=self.excluir,
    #     )

    #     self.linha_botoes = ft.Row(
    #         controls=[self.icb_editar, self.icb_excluir],
    #         alignment=ft.MainAxisAlignment.END,
    #     )

    #     # self.content.content.controls[1] = self.linha_botoes

    # def excluir(self, e):
    #     self.filme_db.delete_filme(self.data)
    #     self.page.go("/reload")

    # def editar(self, e):
    #     self.page.go(f"/formulario/{self.data.id}")
