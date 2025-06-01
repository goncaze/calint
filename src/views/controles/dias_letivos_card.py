import flet as ft

# import datetime
from datetime import date, datetime
import calendar

# from src.views.controles.cartao import Cartao
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
        self.color = ft.Colors.WHITE
        self.dbs: DataDBSingleton = dbs
        self.dbs = dbs
        self.data_db = DataDB(self.dbs)
        self.dias_realizados = self.data_db.select_contagem_dias_especificos(
            evento_id=1, restantes=False
        )
        self.dias_restantes = self.data_db.select_contagem_dias_especificos(1)

        self.expand = True
        # self.width = 350
        self.height = 240
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
            value="Dias letivos realizados",
            size=15,
            # weight=ft.FontWeight.BOLD,
        )
        self.txt_restantes = ft.Text(
            value="Dias letivos restantes",
            size=15,
            # weight=ft.FontWeight.BOLD,
        )

        # self.data_obj = self.data_db.select_uma_data(Data(data=self.data_hoje_str))
        # print(self.data_obj)

        ###
        # Atributos da pizza
        #
        self.normal_radius = 40
        self.hover_radius = 50
        self.normal_title_style = ft.TextStyle(
            size=16, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD
        )
        self.hover_title_style = ft.TextStyle(
            size=22,
            color=ft.Colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.Colors.BLACK54),
        )

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
                            border_radius=50,
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
                            border_radius=50,
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

        radius_dias_realizados = (
            60 if self.dias_realizados > self.dias_restantes else 50
        )
        radius_dias_restantes = 110 - radius_dias_realizados

        perc_dias_realizados = (
            100 * self.dias_realizados / (self.dias_realizados + self.dias_restantes)
        )
        perc_dias_restantes = (
            100 * self.dias_restantes / (self.dias_realizados + self.dias_restantes)
        )
        perc_dias_realizados = round(perc_dias_realizados, 2)
        perc_dias_restantes = round(perc_dias_restantes, 2)

        # print(f"{round(perc_dias_realizados,2)}% = ")
        # print(f"{round(perc_dias_restantes,2)}% = ")

        self.pie_chart = ft.PieChart(
            # width=100,
            height=150,
            sections=[
                ft.PieChartSection(
                    title=str(perc_dias_realizados) + "%",
                    title_style=ft.TextStyle(
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    value=self.dias_realizados,
                    color=ft.Colors.GREEN,
                    # radius=radius_dias_realizados,
                    radius=self.normal_radius,
                    border_side=self.normal_border,
                ),
                ft.PieChartSection(
                    title=str(perc_dias_restantes) + "%",
                    title_style=ft.TextStyle(
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    value=self.dias_restantes,
                    color=ft.Colors.RED,
                    # radius=radius_dias_restantes,
                    radius=self.normal_radius,
                    border_side=self.normal_border,
                ),
            ],
            sections_space=0,
            center_space_radius=40,
            on_chart_event=self.on_chart_event,
            # expand=True,
        )

        return self.pie_chart

    # def on_chart_event(self, e: ft.PieChartEvent):
    #     for idx, section in enumerate(self.pie_chart.sections):
    #         section.border_side = (
    #             self.hovered_border if idx == e.section_index else self.normal_border
    #         )
    #     self.pie_chart.update()

    def on_chart_event(self, e: ft.PieChartEvent):
        for idx, section in enumerate(self.pie_chart.sections):
            if idx == e.section_index:
                section.radius = self.hover_radius
                section.title_style = self.hover_title_style
            else:
                section.radius = self.normal_radius
                section.title_style = self.normal_title_style
        self.pie_chart.update()
