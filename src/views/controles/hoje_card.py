import flet as ft

from datetime import datetime
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton
from src.modelo.data import Data


class HojeCard(ft.Card):

    def __init__(
        self,
        page: ft.Page,
        dbs: DataDBSingleton,
    ):
        super().__init__()
        self.page = page
        # self.expand = True
        self.color = ft.Colors.GREEN_900  # WHITE
        self.margin = ft.margin.all(0)
        self.shape = ft.RoundedRectangleBorder(
            radius=ft.border_radius.only(bottom_left=40, bottom_right=40)
        )
        self.data_hoje = datetime.now().date()
        self.data_hoje_str = self.data_hoje.strftime("%Y-%m-%d")
        self.ano = self.data_hoje.year
        self.mes = self.data_hoje.month
        self.legendas: set = set()
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
            text_align=ft.TextAlign.CENTER,
            color=ft.Colors.WHITE,
        )

        self.txt_dia_hoje = ft.Text(
            value=str(self.data_hoje.day),
            theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD,
        )

        self.dbs = dbs
        self.data_db = DataDB(self.dbs)
        self.data_obj = self.data_db.select_uma_data(Data(data=self.data_hoje_str))
        # print(self.data_obj)

        ###
        # Atributo coluna para conter as cores e o evento
        #
        self.coluna_de_eventos: ft.Column = ft.Column()

        self.content = ft.ResponsiveRow(
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    col=4,
                    # expand=True,
                    # alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        ft.Container(
                            expand=True,
                            content=self.txt_dia_hoje,
                            # bgcolor="blue",
                            # border=ft.border.all(),
                            margin=ft.margin.only(left=15, right=10),
                        ),
                        ft.Container(
                            expand=True,
                            content=self.txt_titulo_mes,
                            # bgcolor="yellow",
                            # border=ft.border.all(),
                            margin=ft.margin.only(left=15, right=10, bottom=15),
                        ),
                    ],
                ),
                ft.Container(
                    col=8,
                    content=ft.Column(
                        expand=True,
                        spacing=0,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        # expand=True,
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(
                                    top=0, left=0, right=10, bottom=10
                                ),
                                content=self.alinhar_eventos(),
                            ),
                        ],
                        # controls=[evento for evento in self.alinhar_eventos()],
                    ),
                ),
                # ft.Container(
                #     width=20, height=100, bgcolor=ft.Colors.AMBER, expand=True
                # ),
                # ft.Column(
                #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                #     expand=True,
                #     spacing=0,
                #     controls=[
                #         ft.Container(
                #             content=self.txt_dia_hoje,
                #             bgcolor="",
                #             margin=ft.margin.only(left=10, right=10),
                #         ),
                #         ft.Container(
                #             content=self.txt_titulo_mes,
                #             bgcolor="",
                #             margin=ft.margin.only(left=10, right=10),
                #         ),
                #     ],
                # ),
            ],
        )

    def alinhar_eventos(self) -> ft.Column:
        col_eventos = ft.Column(spacing=0)
        for evento in self.data_obj.eventos:
            linha = ft.Row(
                expand=True,
                # spacing=0,
                controls=[
                    ft.Container(width=5, height=5, bgcolor=ft.Colors.WHITE),
                    ft.Container(
                        expand=True,
                        content=ft.Text(
                            value=evento.evento,
                            size=16,
                            overflow=ft.TextOverflow.ELLIPSIS,
                            color=ft.Colors.WHITE,
                        ),
                    ),
                ],
            )
            col_eventos.controls.append(linha)
        return col_eventos

    # def alinhar_eventos(self) -> list[ft.Control]:
    #     lista_eventos: list[ft.Control] = []
    #     for evento in self.data_obj.eventos:
    #         linha = ft.Row(
    #             expand=True,
    #             controls=[
    #                 ft.Container(width=5, height=5, bgcolor=ft.Colors.WHITE),
    #                 ft.Container(
    #                     expand=True,
    #                     content=ft.Text(
    #                         value=evento.evento,
    #                         size=16,
    #                         overflow=ft.TextOverflow.ELLIPSIS,
    #                         color=ft.Colors.WHITE,
    #                     ),
    #                 ),
    #             ],
    #         )
    #         lista_eventos.append(linha)
    #     return lista_eventos
