import flet as ft
from src.views.navegacao import Navegador
from src.views.controles.hoje_card import HojeCard
from src.views.controles.dias_letivos_card import DiasLetivosCard
from src.views.calendario.mes_card import MesCard
from src.data.data_db import DataDB


class PrimeiroDashboard(ft.View):
    def __init__(
        self,
        page: ft.Page,
        dbs,
    ):
        super().__init__()

        self.page = page
        self.dbs = dbs
        self.data_db = DataDB(self.dbs)
        self.hoje_card = HojeCard(self.page, self.dbs)  # Card de Hoje
        self.dias_letivos_card = DiasLetivosCard(self.page, self.dbs)  # Card de Pizza
        self.dias_letivos_card.margin = ft.margin.only(top=10)

        self.route = "/"
        self.vertical_alignment = ft.MainAxisAlignment.START
        self.cor_fundo = ft.Colors.WHITE  # "#afffbf"
        self.bgcolor = self.cor_fundo  # ft.Colors.WHITE
        self.padding = 0
        self.spacing = 0
        self.navegador = Navegador(self.page)
        self.drawer_pagelet = self.navegador.drawer()

        self.dias_mes_corrente = self.data_db.select_dias_mes_corrente()
        self.todas_dt_literal = self.extrair_dt_literal()

        self.my_base_area = ft.Container(
            height=50,
        )

        self.mes_card = MesCard(
            self.page,
            self.dbs,
            self.hoje_card.ano,  # Atribuir ano
            self.hoje_card.mes,  # Atribuir mês
            self.dias_mes_corrente,
            self.todas_dt_literal,
        )

        self.mes_card.margin = ft.margin.only(left=10, right=10, top=10)

        self.sublayout = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS)

        self.sublayout.controls.append(self.hoje_card)
        self.sublayout.controls.append(self.mes_card)
        self.sublayout.controls.append(
            ft.Container(
                content=self.mes_card.coluna_de_eventos,
                bgcolor="#F7F7F7",
                expand=True,
                width=self.mes_card.width,
                margin=2,
                padding=ft.padding.only(left=7, top=10, bottom=2),
            )
        )

        self.sublayout.controls.append(self.dias_letivos_card)
        self.sublayout.controls.append(self.my_base_area)

        self.pagelet = ft.Pagelet(
            expand=True,
            content=ft.SafeArea(self.sublayout),
            bgcolor=self.cor_fundo,
            bottom_app_bar=ft.BottomAppBar(
                height=65,
                bgcolor=ft.Colors.GREEN_900,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Container(
                    alignment=ft.alignment.bottom_center,
                    content=ft.Text(
                        value="Calendário Acadêmico do IFMA Campus Viana",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                        color=ft.Colors.WHITE,
                    ),
                ),
            ),
            end_drawer=self.drawer_pagelet,
            floating_action_button=ft.FloatingActionButton(
                content=ft.Icon(name=ft.Icons.SETTINGS, color=ft.Colors.WHITE, size=40),
                on_click=self.open_pagelet_end_drawer,
                shape=ft.CircleBorder(),
                bgcolor=ft.Colors.RED,
            ),
            floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        )
        #
        # ################################################################################
        self.controls = [self.pagelet]

    def open_pagelet_end_drawer(self, e):
        self.pagelet.show_drawer(self.drawer_pagelet)

    def extrair_dt_literal(self) -> list[str]:
        lista_data: list[str] = []
        [lista_data.append(data.data) for data in self.dias_mes_corrente]
        return lista_data
