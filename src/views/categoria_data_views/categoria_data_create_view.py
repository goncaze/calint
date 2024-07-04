import flet as ft
from src.modelo.data_categoria import DataCategoria

from src.data.data_categoria_db import DataCategoriaDB
from src.data.database_singleton import DataDBSingleton
from src.views.categoria_data_views.categoria_data_crud_view import (
    CategoriaDataCRUDView,
)


class CategoriaDataCreateView(CategoriaDataCRUDView):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.route = "/categoria_data_create"
        self.appbar = ft.AppBar(
            # title=ft.Text(value="Cadastrar categoria data"), bgcolor="#008B00"
            title=ft.Text(value="Cadastrar categoria data")
        )
        self.data_categoria_db = DataCategoriaDB(dbs)

        self._page: ft.Page = page

    def registrar(self, e):
        if self.validar():
            dataCategoria = DataCategoria(
                self.ttf_categoria.value, self.ttf_descricao.value
            )
            self.data_categoria_db.insert_data_categoria(dataCategoria)
            self._page.go("/categoria_data_reload")
        else:
            self.atualizar_page()

    def atualizar_page(self):
        self._page.update()


if __name__ == "__main__":
    ...
