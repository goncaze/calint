import flet as ft
import locale

from src.data.database_singleton import DataDBSingleton
from pathlib import Path

from src.views.data_views.data_view import DataView

# from src.views.data_views.BKP_selecionar_data_view import SelecionarDataView
from src.views.data_views.selecionar_data_view import SelecionarDataView
from src.views.data_views.data_add_evento_view import DataAddEventoView

from src.views.evento_categoria_views.categoria_evento_view import CategoriaEventoView
from src.views.evento_categoria_views.categoria_evento_create_view import (
    CategoriaEventoCreateView,
)
from src.views.evento_categoria_views.categoria_evento_edit_view import (
    CategoriaEventoEditView,
)
from src.views.categoria_data_views.categoria_data_view import CategoriaDataView
from src.views.categoria_data_views.categoria_data_edit_view import (
    CategoriaDataEditView,
)
from src.views.categoria_data_views.categoria_data_create_view import (
    CategoriaDataCreateView,
)

from src.views.ano_letivo_views.ano_letivo_view import AnoLetivoView

from src.views.evento_views.evento_view import EventoView
from src.views.evento_views.evento_create_view import EventoCreateView
from src.views.evento_views.evento_edit_view import EventoEditView
from src.views.calendario.calendario import CalendarioView
from src.views.navegacao import Navegador

# locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

ROOT_DIR = Path(__file__).parent
DB_NAME = "calendario_db.sqlite3"
DB_FILE: Path = ROOT_DIR / DB_NAME


class App:

    def __init__(self, page: ft.Page):
        self.page = page

        # def main(page: ft.Page):

        # self.page.dark_theme = ft.theme.Theme(color_scheme_seed="green")
        # self.page.dark_theme = ft.theme.Theme(ft.colors.GREEN)
        # self.page.ligth_theme = ft.theme.Theme(ft.colors.GREEN)
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.theme = ft.Theme(color_scheme_seed="#EEEEEE")
        # self.page.bgcolor = ft.colors.AMBER
        # self.page.window_bgcolor = ft.colors.WHITE

        self.page.locale_configuration = ft.LocaleConfiguration(
            supported_locales=[
                ft.Locale("pt", "PT"),
            ],
            current_locale=ft.Locale("pt", "PT"),
        )

        # page.theme = ft.theme.Theme(color_scheme_seed="#008B00")
        self.dbs = DataDBSingleton(DB_FILE=DB_FILE)
        # page.window_width = 380
        self.page.window.width = 360
        # page.window_height = 500  # 650
        self.page.window.height = 660

        self.navegador = Navegador(page)

        # Conectar um manipulador de eventos ao page.on_route_change
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go("/")

    # ----------------------------------------------------------------------
    ##
    # Rotas para views e appbar
    ##
    def route_change(self, route: ft.RouteChangeEvent):
        # print(f"\n======= def route_change(route: ft.RouteChangeEvent): =======\n")
        # print(f"\nENTRADA:\n{self.page.views = }\n")

        rota: str = route.route

        if rota == "/":
            # Limpa a lista de views
            self.page.views.clear()
            # Adicionar view "/" na lista de views
            self.page.views.append(
                ft.View(
                    route="/",
                    bgcolor=ft.colors.WHITE,
                    # appbar=ft.AppBar(title=ft.Text("CALINT"), bgcolor="#008B00"),
                    appbar=ft.AppBar(title=ft.Text("CALINT")),
                    drawer=self.navegador.drawer(),
                    # logo = ft.Image(src='imagens/Viana_Prancheta.png'),
                    # controls=[ft.Image(src='imagens/Viana_Prancheta.png')]
                    controls=[ft.Image(src="Viana_Prancheta.png")],
                    # controls=ft.Column(
                    #     controls=[ft.Image(src='imagens/Viana_Prancheta.png')],
                    #     scroll=ft.ScrollMode.ALWAYS,
                    #     expand=True,
                    # )
                )
            )

        ######################################
        # Rotas para datas
        ##
        elif rota == "/datas":
            esta_em_pageviews = False
            for i in range(len(self.page.views)):
                if self.page.views[i].route == "/datas":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                self.page.views.append(DataView(self.page, self.dbs))

        elif rota == "/selecionar_data":
            self.page.views.append(SelecionarDataView(self.page, self.dbs))

        elif rota == "/data_add_evento":
            # print("INDO PARA data_add_evento")
            self.page.views.append(DataAddEventoView(self.page, self.dbs))

        elif rota == "/data_reload":
            list_size = len(self.page.views)
            for i in range(list_size):
                if self.page.views[i].route == "/datas":
                    for _ in range(list_size - i):
                        self.page.views.pop()
                    break

            self.page.views.append(DataView(self.page, self.dbs))

        ######################################
        # Rotas para categoria datas
        ##
        elif rota == "/categoria_data":
            esta_em_pageviews = False
            for i in range(len(self.page.views)):
                if self.page.views[i].route == "/categoria_data":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                self.page.views.append(CategoriaDataView(self.page, self.dbs))

        elif rota == "/categoria_data_create":
            self.page.views.append(CategoriaDataCreateView(self.page, self.dbs))

        elif (
            rota.split("__-__")[0] == "/categoria_data_edit"
            and self.page.views[-1].route != "/categoria_data_edit"
        ):
            self.page.views.append(
                CategoriaDataEditView(int(rota.split("__-__")[1]), self.page, self.dbs)
            )

        elif rota == "/categoria_data_reload":
            list_size = len(self.page.views)
            for i in range(list_size):
                if self.page.views[i].route == "/categoria_data":
                    for _ in range(list_size - i):
                        self.page.views.pop()
                    break

            self.page.views.append(CategoriaDataView(self.page, self.dbs))

        elif rota == "/categoria_data_delete_reload":
            self.page.views.pop()
            self.page.views.append(CategoriaDataView(self.page, self.dbs))
            self.page.route = "/categoria_data"

        ######################################
        # Rotas para eventos
        ##
        elif rota == "/eventos":
            esta_em_pageviews = False
            for i in range(len(self.page.views)):
                if self.page.views[i].route == "/eventos":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                self.page.views.append(EventoView(self.page, self.dbs))

        elif rota == "/evento_create":
            self.page.views.append(EventoCreateView(self.page, self.dbs))

        elif (
            rota.split("__-__")[0] == "/evento_edit"
            and self.page.views[-1].route != "/evento_edit"
        ):
            # print(f"\n\n {rota = } \n\n")
            self.page.views.append(
                EventoEditView(int(rota.split("__-__")[1]), self.page, self.dbs)
            )

        elif rota == "/evento_reload":
            list_size = len(self.page.views)
            for i in range(list_size):
                if self.page.views[i].route == "/eventos":
                    for _ in range(list_size - i):
                        self.page.views.pop()
                    break
            self.page.views.append(EventoView(self.page, self.dbs))

        elif rota == "/evento_delete_reload":
            self.page.views.pop()
            self.page.views.append(EventoView(self.page, self.dbs))
            self.page.route = "/eventos"

        ######################################
        # Rotas para categorias de evento
        ##
        elif rota == "/categoria_evento":
            esta_em_pageviews = False
            for i in range(len(self.page.views)):
                if self.page.views[i].route == "/categoria_evento":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                self.page.views.append(CategoriaEventoView(self.page, self.dbs))

        elif rota == "/categoria_evento_create":
            self.page.views.append(CategoriaEventoCreateView(self.page, self.dbs))

        elif (
            rota.split("__-__")[0] == "/categoria_evento_edit"
            and self.page.views[-1].route != "/categoria_evento_edit"
        ):
            self.page.views.append(
                CategoriaEventoEditView(
                    int(rota.split("__-__")[1]), self.page, self.dbs
                )
            )

        elif rota == "/categoria_evento_reload":
            list_size = len(self.page.views)
            for i in range(list_size):
                if self.page.views[i].route == "/categoria_evento":
                    for _ in range(list_size - i):
                        self.page.views.pop()
                    break

            self.page.views.append(CategoriaEventoView(self.page, self.dbs))

        elif rota == "/categoria_evento_delete_reload":
            self.page.views.pop()
            self.page.views.append(CategoriaEventoView(self.page, self.dbs))
            self.page.route = "/categoria_evento"

        ######################################
        # Rotas para categorias de evento
        ##
        elif rota == "/ano_letivo":
            esta_em_pageviews = False
            for i in range(len(self.page.views)):
                if self.page.views[i].route == "/ano_letivo":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                self.page.views.append(AnoLetivoView(self.page, self.dbs))

        ######################################
        # Rotas para calendário
        ##
        elif rota == "/calendario":
            esta_em_pageviews = False
            for i in range(len(self.page.views)):
                if self.page.views[i].route == "/calendario":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                calendario_view = CalendarioView(self.page, self.dbs)
                self.page.views.append(calendario_view)
                
                self.page.add(
                    calendario_view
                )
                calendario_view.reposicionar_auto()
                # calendario_view.scroll_to(key="janeiro2025")

        self.page.update()

    def view_pop(self, e):
        # print(f"\n============def view_pop(e): ============\n")
        # print(f"\n{self.page.views.pop() = }")
        self.page.views.pop()
        top_view = self.page.views[-1]
        # print(f"\n{top_view = }")
        # print(f"\n{type(top_view.route) = }")
        self.page.go(top_view.route)

    # self.page.on_route_change = route_change
    # self.page.on_view_pop = view_pop
    # self.page.go(self.page.route)
    # page.go("/")


# ------------------------------------


def main(page: ft.Page):
    page.bgcolor = ft.colors.AMBER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="#FFFFFF")
    App(page)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
