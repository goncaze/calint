import flet as ft
from src.modelo.evento_categoria import EventoCategoria
from src.data.database_singleton import DataDBSingleton
from src.data.evento_categoria_db import EventoCategoriaDB
from src.views.evento_categoria_views.categoria_evento_crud_view import (
    CategoriaEventoCRUDView,
)


class CategoriaEventoEditView(CategoriaEventoCRUDView):

    def __init__(self, id_evento_categoria: int, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.route = "/categoria_evento_edit"
        self.page: ft.Page = page
        self.eventoCategoriaDB: EventoCategoriaDB = EventoCategoriaDB(dbs)
        self.appbar = ft.AppBar(
            title=ft.Text(value="Editar categoria evento")
        )

        self.eventoCategoria: EventoCategoria = (
            self.eventoCategoriaDB.select_evento_categoria(id_evento_categoria)
        )

        self.ttf_categoria.value = self.eventoCategoria.categoria
        self.ttf_descricao.value = self.eventoCategoria.descricao
        self.ttf_cor.value = self.eventoCategoria.cor

    def registrar(self, e):
        if self.validar():
            self.eventoCategoriaDB.update_evento_categoria(
                self.eventoCategoria.id,
                self.ttf_categoria.value,
                self.ttf_descricao.value,
                self.ttf_cor.value
            )
            self.page.go("/categoria_evento_reload")
        else:
            self.atualizar_page()

    def atualizar_page(self):
        self.page.update()


if __name__ == "__main__":
    ...

