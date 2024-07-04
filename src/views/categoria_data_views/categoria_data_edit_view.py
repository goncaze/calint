import flet as ft
from src.modelo.data_categoria import DataCategoria
from src.data.data_categoria_db import DataCategoriaDB
from src.data.database_singleton import DataDBSingleton
from src.views.categoria_data_views.categoria_data_crud_view import (
    CategoriaDataCRUDView,
)


class CategoriaDataEditView(CategoriaDataCRUDView):

    def __init__(self, id_data_categoria: int, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.route = "/categoria_data_edit"
        self.appbar = ft.AppBar(
            # title=ft.Text(value="Editar categoria data"), bgcolor="#008B00"
            title=ft.Text(value="Editar categoria data")
        )
        self.data_categoria_db: DataCategoriaDB = DataCategoriaDB(dbs)

        self.dataCategoria: DataCategoria = (
            self.data_categoria_db.select_data_categoria(id_data_categoria)
        )
        self.page: ft.Page = page

        self.ttf_categoria.value = self.dataCategoria.categoria
        self.ttf_descricao.value = self.dataCategoria.descricao

    def registrar(self, e):
        if self.validar():
            self.data_categoria_db.update_data_categoria(
                self.dataCategoria.id,
                self.ttf_categoria.value,
                self.ttf_descricao.value,
            )
            self.page.go("/categoria_data_reload")
        else:
            self.atualizar_page()

    def atualizar_page(self):
        self.page.update()


if __name__ == "__main__":
    ...
