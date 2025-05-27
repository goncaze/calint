import flet as ft
from src.views.navegacao import Navegador
from src.views.controles.hoje_card import HojeCard


class PrimeiroDashboard(ft.View):
    def __init__(
        self,
        page: ft.Page,
        dbs,
        route=None,
        controls=None,
        appbar=None,
        bottom_appbar=None,
        floating_action_button=None,
        floating_action_button_location=None,
        navigation_bar=None,
        drawer=None,
        end_drawer=None,
        vertical_alignment=None,
        horizontal_alignment=None,
        spacing=None,
        padding=None,
        bgcolor=None,
        decoration=None,
        foreground_decoration=None,
        scroll=None,
        auto_scroll=None,
        fullscreen_dialog=None,
        on_scroll_interval=None,
        on_scroll=None,
        adaptive=None,
    ):
        super().__init__()

        self.page = page
        self.dbs = dbs
        self.hoje_card = HojeCard(self.page, self.dbs)
        self.route = "/"
        self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
        self.cor_fundo = "#afffbf"
        self.bgcolor = self.cor_fundo  # ft.Colors.WHITE
        self.padding = 0
        self.spacing = 0
        # self.appbar = ft.AppBar(title=ft.Text("CALINT"))
        self.navegador = Navegador(self.page)
        self.drawer_pagelet = self.navegador.drawer()
        ##################################################################################
        #
        self.pagelet = ft.Pagelet(
            expand=True,
            # appbar=ft.AppBar(
            #     title=ft.Text("Pagelet AppBar Title"), bgcolor=ft.Colors.AMBER_900
            # ),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                # expand=True,
                controls=[
                    ft.Container(height=5),
                    ft.Image(
                        src="http://10.0.0.61:8000/Campus_Viana_edited.png",
                        # color="green",
                    ),
                    self.hoje_card,
                ],
            ),
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
                        theme_style=ft.TextThemeStyle.BODY_LARGE,
                        color=ft.Colors.WHITE,
                    ),
                ),
            ),
            end_drawer=self.drawer_pagelet,
            floating_action_button=ft.FloatingActionButton(
                # text="Menu",
                content=ft.Text(value="Menu", color=ft.Colors.WHITE),
                on_click=self.open_pagelet_end_drawer,
                shape=ft.CircleBorder(),
                bgcolor=ft.Colors.RED,
            ),
            floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        )
        #
        # ################################################################################
        self.controls = [
            # ft.Image(src="Campus_Viana_edited.png", color="green"),
            # self.hoje_card,
            self.pagelet,
        ]

    def open_pagelet_end_drawer(self, e):
        self.pagelet.show_drawer(self.drawer_pagelet)
