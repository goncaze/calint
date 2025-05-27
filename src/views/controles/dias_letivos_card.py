import flet as ft

# import datetime
from datetime import date, datetime
import calendar
from src.views.controles.cartao import Cartao
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton
from src.modelo.data import Data
from src.modelo.evento import Evento


class DiasLetivosCard(ft.Card):

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
        self.pie_chart: ft.PieChart = None
        self.normal_border = ft.BorderSide(
            0, ft.Colors.with_opacity(0, ft.Colors.WHITE)
        )
        self.hovered_border = ft.BorderSide(6, ft.Colors.WHITE)
        self.data_hoje = datetime.now().date()
        self.data_hoje_str = self.data_hoje.strftime("%Y-%m-%d")
        self.ano = self.data_hoje.year
        self.mes = self.data_hoje.month
        # print(f"{self.data_hoje.strftime("%Y-%m-%d") = }")
        self.legendas: set = set()
        # self.todas_datas: list[Data] = todas_datas
        # self.todas_dt_literal: list[str] = todas_dt_literal

        self.txt_cumpridos = ft.Text(
            value="Cumprimento de dias letivos",
            size=15,
            weight=ft.FontWeight.BOLD,
        )
        self.txt_restantes = ft.Text(
            value="Dias letivos restantes",
            size=15,
            weight=ft.FontWeight.BOLD,
        )
        # self.txt_dia_hoje = ft.Text(
        #     value=str(self.data_hoje.day),
        #     theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
        #     weight=ft.FontWeight.BOLD,
        # )

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

        self.content = ft.Column(
            controls=[
                ft.Row(
                    # spacing=50,
                    controls=[
                        ft.Container(
                            width=15,
                            height=15,
                            bgcolor=ft.Colors.GREEN,
                            margin=ft.margin.only(left=20, top=10),
                        ),
                        ft.Container(
                            margin=ft.margin.only(top=10),
                            content=self.txt_cumpridos,
                        ),
                    ],
                ),
                ft.Row(
                    # spacing=50,
                    controls=[
                        ft.Container(
                            width=15,
                            height=15,
                            bgcolor=ft.Colors.PINK,
                            margin=ft.margin.only(left=20),
                        ),
                        ft.Container(
                            content=self.txt_restantes,
                        ),
                    ],
                ),
                self.gerar_grafico(),
            ]
        )

    def gerar_grafico(self) -> ft.PieChart:

        self.pie_chart = ft.PieChart(
            # width=200,
            height=150,
            sections=[
                ft.PieChartSection(
                    value=25,
                    color=ft.Colors.GREEN,
                    radius=60,
                    border_side=self.normal_border,
                ),
                # ft.PieChartSection(
                #     25,
                #     color=ft.Colors.YELLOW,
                #     radius=65,
                #     border_side=self.normal_border,
                # ),
                ft.PieChartSection(
                    value=45,
                    color=ft.Colors.PINK,
                    radius=60,
                    border_side=self.normal_border,
                ),
                # ft.PieChartSection(
                #     25,
                #     color=ft.Colors.GREEN,
                #     radius=70,
                #     border_side=self.normal_border,
                # ),
            ],
            sections_space=1,
            center_space_radius=0,
            on_chart_event=self.on_chart_event,
            expand=True,
        )

        return self.pie_chart

    def on_chart_event(self, e: ft.PieChartEvent):
        for idx, section in enumerate(self.pie_chart.sections):
            section.border_side = (
                self.hovered_border if idx == e.section_index else self.normal_border
            )
        self.pie_chart.update()
