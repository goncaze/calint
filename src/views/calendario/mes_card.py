import flet as ft

import datetime
import calendar
from src.views.controles.cartao import Cartao
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton
from src.modelo.data import Data
from src.modelo.evento import Evento


class MesCard(Cartao):

    def __init__(
        self,
        page: ft.Page,
        dbs: DataDBSingleton,
        ano: int,
        mes: int,
        todas_datas: list[Data] = None,
        todas_dt_literal: list[str] = None,
    ):
        super().__init__()
        self.page = page
        self.expand = True
        self.width = 350

        self.ano = ano
        self.mes = mes
        self.legendas: set = set()
        self.todas_datas: list[Data] = todas_datas
        self.todas_dt_literal: list[str] = todas_dt_literal
        self.meses = [
            "",
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        self.titulo_mes = f"{self.meses[mes]} de {ano}"

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
                bgcolor="#429629",  # ft.Colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.Colors.GREY_300),
                expand=True,
            )
        ]
        self.lista_container_01 = [
            ft.Container(
                content=ft.Text(value="SEG", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.Colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.Colors.GREY_300),
                expand=True,
            )
        ]
        self.lista_container_02 = [
            ft.Container(
                content=ft.Text(value="TER", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.Colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.Colors.GREY_300),
                expand=True,
            )
        ]
        self.lista_container_03 = [
            ft.Container(
                content=ft.Text(value="QUA", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.Colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.Colors.GREY_300),
                expand=True,
            )
        ]
        self.lista_container_04 = [
            ft.Container(
                content=ft.Text(value="QUI", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.Colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.Colors.GREY_300),
                expand=True,
            )
        ]
        self.lista_container_05 = [
            ft.Container(
                content=ft.Text(value="SEX", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.Colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.Colors.GREY_300),
                expand=True,
            )
        ]
        self.lista_container_06 = [
            ft.Container(
                content=ft.Text(value="SAB", color="#FFFFFF"),
                alignment=ft.alignment.center,
                bgcolor="#429629",  # ft.Colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.Colors.GREY_300),
                expand=True,
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
        self.coluna_00 = ft.Column(self.lista_container_00, expand=True, spacing=1)
        self.coluna_01 = ft.Column(self.lista_container_01, expand=True, spacing=1)
        self.coluna_02 = ft.Column(self.lista_container_02, expand=True, spacing=1)
        self.coluna_03 = ft.Column(self.lista_container_03, expand=True, spacing=1)
        self.coluna_04 = ft.Column(self.lista_container_04, expand=True, spacing=1)
        self.coluna_05 = ft.Column(self.lista_container_05, expand=True, spacing=1)
        self.coluna_06 = ft.Column(self.lista_container_06, expand=True, spacing=1)

        # ###
        # # Uma Row para agrupar as colnas antes de incluir no Card.
        # #
        # self.linha: ft.Row = ft.Row(
        #     spacing=0,
        #     controls=[
        #         self.coluna_00,
        #         self.coluna_01,
        #         self.coluna_02,
        #         self.coluna_03,
        #         self.coluna_04,
        #         self.coluna_05,
        #         self.coluna_06,
        #     ]
        # )

        self.content = ft.Container(
            expand=True,
            margin=5,
            padding=0,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                content=ft.Text(value=self.titulo_mes),
                                alignment=ft.alignment.center,
                                expand=True,
                            ),
                        ],
                    ),
                    ft.Row(
                        spacing=0,
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
                ],
            ),
        )

    def filtrar_linha_cor_legenda(self, dia: int, lista_eventos: list[Evento]) -> None:
        # Para cada evento na lista de eventos
        for evento in lista_eventos:
            # Se um determinado evento não está no set de legendas
            if evento.evento not in self.legendas:
                # print(" def filtrar_linha_cor_legenda(self, lista_eventos: list[Evento])->None:")
                # Incluir o determinado evento no set de legendas
                self.legendas.add(evento.evento)
                # Container de cor para a legenda do evento
                cntn_cor = ft.Container(
                    width=30,
                    height=25,
                    bgcolor=evento.evento_categoria.cor,
                    border_radius=50,
                    # Preciso evitar a inclusão do dia caso exista mais da mesma categoria
                    content=ft.Text(
                        value="" if evento.evento in ("Dia letivo", "Férias") else dia
                    ),
                    alignment=ft.alignment.center,
                )
                legenda = ft.Text(value=evento.evento)
                # print("{legenda = }")
                # print(f"{legenda = }")

                # linha_cor_legenda = ft.Row( controls = [ cntn_cor, legenda ] )
                self.coluna_de_eventos.controls.append(  # ft.Text('Teste')
                    # self.setar_linha_cor_legenda( evento.evento_categoria.cor, evento )
                    ft.Row(controls=[cntn_cor, legenda])
                )

    def determinar_cor_data(self, dia: int) -> str:

        cor = ""
        data_calendario = datetime.date(self.ano, self.mes, dia).strftime("%Y-%m-%d")

        # if calendar.weekday(self.ano, self.mes, dia) in (5, 6):

        # Determinar se é final de semana (Domingo)
        if calendar.weekday(self.ano, self.mes, dia) == 6:
            cor = "#ea9999"

        elif data_calendario in self.todas_dt_literal:
            indice = self.todas_dt_literal.index(data_calendario)

            if self.todas_datas[indice].eventos:

                cor = self.todas_datas[indice].eventos[-1].evento_categoria.cor
                self.filtrar_linha_cor_legenda(dia, self.todas_datas[indice].eventos)

            # Determinar se é final de semana (Sábado)
            elif calendar.weekday(self.ano, self.mes, dia) == 5:
                cor = "#ea9999"

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
                border=ft.border.all(width=1, color=ft.Colors.GREY_300),
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

        for dia in self.obj_calendar_d0.itermonthdays(self.ano, self.mes):
            if i < 7:
                self.listas_containers[i].append(self.container(dia))
                i += 1
            else:
                i = 1
                self.listas_containers[0].append(self.container(dia))

    # def contar_eventos(self, evento: Evento, lista_eventos: list[Evento]) -> bool:
    #     contagem: int = 0

    #     for item_evento in lista_eventos:
    #         print(f"{item_evento.evento = }")
    #         if item_evento.evento == evento.evento:
    #             contagem += 1
    #         print(f"{evento.evento = } \t| {contagem = }")

    #     return contagem == 1

    # def setar_linha_cor_legenda(
    #     self, cor: str = "#eee222", evento: str = "Legenda"
    # ) -> ft.Row:
    #     cntn_cor = ft.Container(width=30, height=25, bgcolor=cor)
    #     legenda: str = evento

    #     linha_cor_legenda = ft.Row(controls=[cntn_cor, legenda])

    #     return linha_cor_legenda
