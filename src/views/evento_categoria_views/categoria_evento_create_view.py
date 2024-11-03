import flet as ft
from src.modelo.evento_categoria import EventoCategoria
from src.data.evento_categoria_db import EventoCategoriaDB
from src.data.database_singleton import DataDBSingleton
from src.views.evento_categoria_views.categoria_evento_crud_view import (
    CategoriaEventoCRUDView,
)


class CategoriaEventoCreateView(CategoriaEventoCRUDView):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.route = "/categoria_evento_create"
        self.appbar = ft.AppBar(
            # title=ft.Text(value="Cadastrar categoria evento"), bgcolor="#008B00"
            title=ft.Text(value="Cadastrar categoria evento")
        )

        self.page: ft.Page = page
        self.eventoCategoriaDB: EventoCategoriaDB = EventoCategoriaDB(dbs)

    def registrar(self, e):
        if self.validar():
            eventoCategoria = EventoCategoria(
                categoria = self.ttf_categoria.value, 
                descricao = self.ttf_descricao.value, 
                cor = self.ttf_cor.value
            )
            self.eventoCategoriaDB.insert_evento_categoria(eventoCategoria)
            self.page.go("/categoria_evento_reload")
        else:
            self.atualizar_page()

    def atualizar_page(self):
        self.page.update()


if __name__ == "__main__":
    ...
