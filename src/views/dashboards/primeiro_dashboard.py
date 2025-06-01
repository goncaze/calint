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

        # self.expand = True
        # self.scroll = True
        self.page = page
        self.dbs = dbs
        self.data_db = DataDB(self.dbs)
        self.hoje_card = HojeCard(self.page, self.dbs)  # Card de Hoje
        self.dias_letivos_card = DiasLetivosCard(self.page, self.dbs)  # Card de Pizza
        self.dias_letivos_card.margin = ft.margin.only(top=10)

        self.route = "/"
        # self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
        self.vertical_alignment = ft.MainAxisAlignment.START
        self.cor_fundo = ft.Colors.WHITE  # "#afffbf"
        self.bgcolor = self.cor_fundo  # ft.Colors.WHITE
        self.padding = 0
        self.spacing = 0
        # self.appbar = ft.AppBar(title=ft.Text("CALINT"))
        self.navegador = Navegador(self.page)
        self.drawer_pagelet = self.navegador.drawer()

        self.dias_mes_corrente = self.data_db.select_dias_mes_corrente()
        self.todas_dt_literal = self.extrair_dt_literal()

        # print(f"self.hoje_card: {self.hoje_card}")
        # print(f"self.hoje_card.ano: {self.hoje_card.ano}")
        # print(f"self.hoje_card.mes: {self.hoje_card.mes}")

        self.my_safe_area = ft.Container(
            height=40,
            # bgcolor=self.cor_fundo,
            bgcolor=ft.Colors.GREEN_900,
            margin=ft.margin.all(0),
            padding=ft.padding.all(0),
        )
        self.my_base_area = ft.Container(
            height=50,
            # bgcolor=self.cor_fundo,
            # bgcolor=ft.Colors.GREEN_900,
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

        self.lv_pagelet = ft.ListView(
            spacing=0,
            padding=0,
            expand=True,
            # horizontal=True,
        )
        ##################################################################################
        #
        # self.lv_pagelet.controls.append(
        #     ft.Container(
        #         height=50,
        #         # bgcolor=self.cor_fundo,
        #         bgcolor=ft.Colors.GREEN_900,
        #     )
        # )

        self.lv_pagelet.controls.append(self.hoje_card)
        self.lv_pagelet.controls.append(self.mes_card)
        self.lv_pagelet.controls.append(
            ft.Container(
                content=self.mes_card.coluna_de_eventos,
                bgcolor="#F7F7F7",
                expand=True,
                width=self.mes_card.width,
                margin=2,
                padding=ft.padding.only(left=7, top=10, bottom=2),
            )
        )
        self.lv_pagelet.controls.append(self.dias_letivos_card)
        self.lv_pagelet.controls.append(self.my_base_area)

        self.pagelet = ft.Pagelet(
            expand=True,
            content=self.lv_pagelet,
            bgcolor=self.cor_fundo,
            bottom_app_bar=ft.BottomAppBar(
                height=65,
                bgcolor=ft.Colors.GREEN_900,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Container(
                    alignment=ft.alignment.bottom_center,
                    # bgcolor=ft.Colors.PINK,
                    content=ft.Text(
                        value="Calendário Acadêmico do IFMA Campus Viana",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                        color=ft.Colors.WHITE,
                    ),
                ),
            ),
            end_drawer=self.drawer_pagelet,
            floating_action_button=ft.FloatingActionButton(
                # text="Menu",
                # content=ft.Text(value="Menu", color=ft.Colors.WHITE),
                content=ft.Icon(name=ft.Icons.SETTINGS, color=ft.Colors.WHITE, size=40),
                on_click=self.open_pagelet_end_drawer,
                shape=ft.CircleBorder(),
                bgcolor=ft.Colors.RED,
                # icon=ft.Icons.AC_UNIT,
            ),
            floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        )
        #
        # ################################################################################
        self.controls = [
            # ft.Image(src="Campus_Viana_edited.png", color="green"),
            # self.hoje_card,
            self.my_safe_area,
            self.pagelet,
        ]

    def open_pagelet_end_drawer(self, e):
        self.pagelet.show_drawer(self.drawer_pagelet)

    def extrair_dt_literal(self) -> list[str]:
        lista_data: list[str] = []
        [lista_data.append(data.data) for data in self.dias_mes_corrente]
        return lista_data
