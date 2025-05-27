import flet as ft

# import datetime
from datetime import date, datetime
import calendar
from src.views.controles.cartao import Cartao
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton
from src.modelo.data import Data
from src.modelo.evento import Evento


class HojeCard(ft.Card):

    def __init__(
        self,
        page: ft.Page,
        dbs: DataDBSingleton,
    ):
        super().__init__()
        self.page = page
        # self.color = "#afffbf"
        # self.expand = True

        # self.width = 350
        # self.height = 200

        self.data_hoje = datetime.now().date()
        self.data_hoje_str = self.data_hoje.strftime("%Y-%m-%d")
        self.ano = self.data_hoje.year
        self.mes = self.data_hoje.month
        # print(f"{self.data_hoje.strftime("%Y-%m-%d") = }")
        self.legendas: set = set()
        # self.todas_datas: list[Data] = todas_datas
        # self.todas_dt_literal: list[str] = todas_dt_literal
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
        self.txt_titulo_mes = ft.Text(
            value=f"{self.meses[self.mes]} de {self.ano}",
            size=20,
            weight=ft.FontWeight.BOLD,
        )

        self.txt_dia_hoje = ft.Text(
            value=str(self.data_hoje.day),
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
            weight=ft.FontWeight.BOLD,
        )

        self.obj_calendar_d0 = calendar.Calendar(firstweekday=6)
        # obj_calendar_d1 = calendar.Calendar(firstweekday=1)
        calendar.setfirstweekday(calendar.SUNDAY)
        self.dbs = dbs
        self.data_db = DataDB(self.dbs)
        self.data_obj = self.data_db.select_uma_data(Data(data=self.data_hoje_str))
        print(self.data_obj)

        ###
        # Atributo coluna para conter as cores e o evento
        #
        self.coluna_de_eventos: ft.Column = ft.Column()

        self.content = ft.Row(
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        ft.Container(
                            # border=ft.border.all(1, "pink"),
                            content=self.txt_dia_hoje,
                            bgcolor="",
                            margin=ft.margin.only(left=10, right=10),
                        ),
                        ft.Container(
                            # border=ft.border.all(1, "green"),
                            content=self.txt_titulo_mes,
                            bgcolor="",
                            margin=ft.margin.only(left=10, right=10),
                        ),
                    ],
                ),
                ft.Container(
                    # border=ft.border.all(1, "brown"),
                    # margin=ft.margin.only(top=15),
                    content=ft.Column(
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        expand=True,
                        controls=[
                            # ft.Text(value=evento.evento)
                            # for evento in self.data_obj.eventos
                            evento
                            for evento in self.alinhar_eventos()
                        ],
                    ),
                ),
            ]
        )

    def alinhar_eventos(self) -> list[ft.Control]:
        lista_eventos: list[ft.Control] = []
        for evento in self.data_obj.eventos:
            linha = ft.Row(
                controls=[
                    ft.Container(width=5, height=5, bgcolor="black"),
                    ft.Text(value=evento.evento),
                ]
            )
            lista_eventos.append(linha)
        return lista_eventos

        ...

        # ft.Column(
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #     spacing=0,
        #     controls=[
        #         ft.Container(content=self.txt_dia_hoje, bgcolor=""),
        #         ft.Container(content=self.txt_titulo_mes, bgcolor=""),
        #         ft.Container(
        #             # border=ft.border.all(2, "black"),
        #             margin=ft.margin.only(top=15),
        #             content=ft.Column(
        #                 horizontal_alignment=ft.CrossAxisAlignment.START,
        #                 expand=True,
        #                 controls=[
        #                     ft.Text(value=evento.evento)
        #                     for evento in self.data_obj.eventos
        #                 ],
        #             ),
        #         ),
        #     ],
        # )

        # self.content = ft.Container(
        #     expand=False,
        #     margin=25,
        #     padding=20,
        #     content=ft.Column(
        #         spacing=0,
        #         controls=[
        #             ft.Row(
        #                 spacing=0,
        #                 controls=[
        #                     ft.Container(
        #                         content=ft.Text(value=self.titulo_mes),
        #                         alignment=ft.alignment.center,
        #                         expand=True,
        #                     ),
        #                 ],
        #             ),
        #             ft.Row(
        #                 spacing=0,
        #                 vertical_alignment=ft.CrossAxisAlignment.START,
        #                 controls=[
        #                     ft.Text(value="Teste")
        #                     # self.coluna_00,
        #                     # self.coluna_01,
        #                     # self.coluna_02,
        #                     # self.coluna_03,
        #                     # self.coluna_04,
        #                     # self.coluna_05,
        #                     # self.coluna_06,
        #                 ],
        #             ),
        #         ],
        #     ),
        # )

    # def filtrar_linha_cor_legenda(self, dia: int, lista_eventos: list[Evento]) -> None:
    #     # Para cada evento na lista de eventos
    #     for evento in lista_eventos:
    #         # Se um determinado evento não está no set de legendas
    #         if evento.evento not in self.legendas:
    #             # print(" def filtrar_linha_cor_legenda(self, lista_eventos: list[Evento])->None:")
    #             # Incluir o determinado evento no set de legendas
    #             self.legendas.add(evento.evento)
    #             # Container de cor para a legenda do evento
    #             cntn_cor = ft.Container(
    #                 width=30,
    #                 height=25,
    #                 bgcolor=evento.evento_categoria.cor,
    #                 border_radius=50,
    #                 # Preciso evitar a inclusão do dia caso exista mais da mesma categoria
    #                 content=ft.Text(
    #                     value="" if evento.evento in ("Dia letivo", "Férias") else dia
    #                 ),
    #                 alignment=ft.alignment.center,
    #             )
    #             legenda = ft.Text(value=evento.evento)

    #             # linha_cor_legenda = ft.Row( controls = [ cntn_cor, legenda ] )
    #             self.coluna_de_eventos.controls.append(  # ft.Text('Teste')
    #                 # self.setar_linha_cor_legenda( evento.evento_categoria.cor, evento )
    #                 ft.Row(controls=[cntn_cor, legenda])
    #             )

    # def setar_linha_cor_legenda(
    #     self, cor: str = "#eee222", evento: str = "Legenda"
    # ) -> ft.Row:
    #     cntn_cor = ft.Container(width=30, height=25, bgcolor=cor)
    #     legenda: str = evento

    #     linha_cor_legenda = ft.Row(controls=[cntn_cor, legenda])

    #     return linha_cor_legenda

    # def determinar_cor_data(self, dia: int) -> str:

    #     cor = ""
    #     # data_calendario = datetime.date(self.ano, self.mes, dia).strftime("%Y-%m-%d")
    #     data_calendario = date(self.ano, self.mes, dia).strftime("%Y-%m-%d")

    #     # if calendar.weekday(self.ano, self.mes, dia) in (5, 6):
    #     if calendar.weekday(self.ano, self.mes, dia) == 6:
    #         cor = "#ea9999"

    #     elif data_calendario in self.todas_dt_literal:
    #         indice = self.todas_dt_literal.index(data_calendario)

    #         if self.todas_datas[indice].eventos:

    #             cor = self.todas_datas[indice].eventos[-1].evento_categoria.cor
    #             self.filtrar_linha_cor_legenda(dia, self.todas_datas[indice].eventos)

    #         elif calendar.weekday(self.ano, self.mes, dia) == 5:
    #             cor = "#ea9999"

    #     return cor
