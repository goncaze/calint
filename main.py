import flet as ft

from src.data.database_singleton import DataDBSingleton
from pathlib import Path

from src.views.data_views.data_view import DataView
from src.views.data_views.selecionar_data_view import SelecionarDataView

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


ROOT_DIR = Path(__file__).parent
DB_NAME = "calendario_db.sqlite3"
DB_FILE: Path = ROOT_DIR / DB_NAME


def main(page: ft.Page):

    # page.dark_theme = ft.theme.Theme(color_scheme_seed="green")
    # page.dark_theme = ft.theme.Theme(ft.colors.GREEN)
    # page.ligth_theme = ft.theme.Theme(ft.colors.GREEN)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.GREEN,
        # primary_text_theme=ft.TextTheme(),
        )

    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[
            ft.Locale("pt", "PT"),
        ],
        current_locale=ft.Locale("pt", "PT"),
    )

    # page.theme = ft.theme.Theme(color_scheme_seed="#008B00")
    dbs = DataDBSingleton(DB_FILE=DB_FILE)    
    # page.window_width = 380
    page.window.width = 360
    # page.window_height = 500  # 650
    page.window.height = 680

    navegador = Navegador(page)

    # ----------------------------------------------------------------------
    ##
    # Rotas para views e appbar
    ##
    def route_change(route: ft.RouteChangeEvent):
        print(f"\n======= def route_change(route: ft.RouteChangeEvent): =======\n")
        print(f"\nENTRADA:\n{page.views = }\n")

        rota: str = route.route

        if rota == "/":
            # Limpa a lista de views
            page.views.clear()
            # Adicionar view "/" na lista de views
            page.views.append(
                ft.View(
                    route="/",
                    # appbar=ft.AppBar(title=ft.Text("CALINT"), bgcolor="#008B00"),
                    appbar=ft.AppBar(title=ft.Text("CALINT")),
                    drawer=navegador.drawer(),
                    # logo = ft.Image(src='imagens/Viana_Prancheta.png'),
                    # controls=[ft.Image(src='imagens/Viana_Prancheta.png')]
                    controls=[ft.Image(src='Viana_Prancheta.png')]
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
            for i in range(len(page.views)):
                if page.views[i].route == "/datas":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                page.views.append(DataView(page, dbs))

        elif rota == "/selecionar_data":
            page.views.append(SelecionarDataView(page, dbs))

        elif rota == "/data_reload":
            list_size = len(page.views)
            for i in range(list_size):
                if page.views[i].route == "/datas":
                    for _ in range(list_size - i):
                        page.views.pop()
                    break

            page.views.append(DataView(page, dbs))

        ######################################
        # Rotas para categoria datas
        ##
        elif rota == "/categoria_data":
            esta_em_pageviews = False
            for i in range(len(page.views)):
                if page.views[i].route == "/categoria_data":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                page.views.append(CategoriaDataView(page, dbs))

        elif rota == "/categoria_data_create":
            page.views.append(CategoriaDataCreateView(page, dbs))

        elif (
            rota.split("__-__")[0] == "/categoria_data_edit"
            and page.views[-1].route != "/categoria_data_edit"
        ):
            page.views.append(
                CategoriaDataEditView(int(rota.split("__-__")[1]), page, dbs)
            )

        elif rota == "/categoria_data_reload":
            list_size = len(page.views)
            for i in range(list_size):
                if page.views[i].route == "/categoria_data":
                    for _ in range(list_size - i):
                        page.views.pop()
                    break

            page.views.append(CategoriaDataView(page, dbs))

        elif rota == "/categoria_data_delete_reload":
            page.views.pop()
            page.views.append(CategoriaDataView(page, dbs))
            page.route = "/categoria_data"

        ######################################
        # Rotas para eventos
        ##
        elif rota == "/eventos":
            esta_em_pageviews = False
            for i in range(len(page.views)):
                if page.views[i].route == "/eventos":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                page.views.append(EventoView(page, dbs))

        elif rota == "/evento_create":
            page.views.append(EventoCreateView(page, dbs))

        elif (
            rota.split("__-__")[0] == "/evento_edit"
            and page.views[-1].route != "/evento_edit"
        ):
            print(f"\n\n {rota = } \n\n")
            page.views.append(EventoEditView(int(rota.split("__-__")[1]), page, dbs))

        elif rota == "/evento_reload":
            list_size = len(page.views)
            for i in range(list_size):
                if page.views[i].route == "/eventos":
                    for _ in range(list_size - i):
                        page.views.pop()
                    break
            page.views.append(EventoView(page, dbs))

        elif rota == "/evento_delete_reload":
            page.views.pop()
            page.views.append(EventoView(page, dbs))
            page.route = "/eventos"

        ######################################
        # Rotas para categorias de evento
        ##
        elif rota == "/categoria_evento":
            esta_em_pageviews = False
            for i in range(len(page.views)):
                if page.views[i].route == "/categoria_evento":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                page.views.append(CategoriaEventoView(page, dbs))

        elif rota == "/categoria_evento_create":
            page.views.append(CategoriaEventoCreateView(page, dbs))

        elif (
            rota.split("__-__")[0] == "/categoria_evento_edit"
            and page.views[-1].route != "/categoria_evento_edit"
        ):
            page.views.append(
                CategoriaEventoEditView(int(rota.split("__-__")[1]), page, dbs)
            )

        elif rota == "/categoria_evento_reload":
            list_size = len(page.views)
            for i in range(list_size):
                if page.views[i].route == "/categoria_evento":
                    for _ in range(list_size - i):
                        page.views.pop()
                    break

            page.views.append(CategoriaEventoView(page, dbs))

        elif rota == "/categoria_evento_delete_reload":
            page.views.pop()
            page.views.append(CategoriaEventoView(page, dbs))
            page.route = "/categoria_evento"
        
        ######################################
        # Rotas para categorias de evento
        ##
        elif rota == "/ano_letivo":
            esta_em_pageviews = False
            for i in range(len(page.views)):
                if page.views[i].route == "/ano_letivo":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                page.views.append(AnoLetivoView(page, dbs))

        ######################################
        # Rotas para calendário
        ##
        elif rota == "/calendario":
            esta_em_pageviews = False
            for i in range(len(page.views)):
                if page.views[i].route == "/calendario":
                    esta_em_pageviews = True
                    break

            if not esta_em_pageviews:
                page.views.append(CalendarioView(page, dbs))
            
            

        page.update()

    def view_pop(e):
        # print(f"\n============def view_pop(e): ============\n")
        # print(f"\n{page.views.pop() = }")
        page.views.pop()
        top_view = page.views[-1]
        # print(f"\n{top_view = }")
        # print(f"\n{type(top_view.route) = }")
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    # page.go("/")


# ------------------------------------


if __name__ == "__main__":
    ft.app(target=main, assets_dir='assets')
