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
            # title=ft.Text(value="Editar categoria evento"), bgcolor="#008B00"
            title=ft.Text(value="Editar categoria evento")
        )

        self.eventoCategoria: EventoCategoria = (
            self.eventoCategoriaDB.select_evento_categoria(id_evento_categoria)
        )

        self.ttf_categoria.value = self.eventoCategoria.categoria
        self.ttf_descricao.value = self.eventoCategoria.descricao
        self.ttf_cor.value = self.eventoCategoria.cor

    def registrar(self, e):
        print("\n\ndef registrar(self, e):")
        if self.validar():
            print("\n\t if self.validar:")
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


# class CategoriaDataEditView(ft.View):

#     def __init__(self, id_evento_categoria: int, page: ft.Page, db: DataDB):
#        super().__init__()
#        self.route = "/categoria_data_edit"
#        self.appbar = ft.AppBar(
#            title=ft.Text(value="Editar categoria data"),
#            bgcolor="#3A0786"
#        )

#        self.eventoCategoria: DataCategoria = db.select_data_categoria(id_evento_categoria)
#        self.page: ft.Page = page
#        self._db: DataDB = db

#        self.ttf_categoria = ft.TextField(
#             label="Categoria",
#             hint_text="Categoria",
#             value = self.eventoCategoria.categoria
#        )

#        self.ttf_descricao = ft.TextField(
#             label="descricao",
#             hint_text="descricao",
#             value = self.eventoCategoria.descricao,
#        )

#        self.btn_atualizar = ft.ElevatedButton(
#            text="Salvar",
#            on_click=self.atualizar
#        )

#        self.btn_limpar_form = ft.ElevatedButton(
#            text="Limpar",
#            on_click=self._btn_limpar_form
#         )

#        self.formulario_categoria_data_edit = ft.Column(
#            controls=[
#                self.ttf_categoria,
#                self.ttf_descricao,
#                ft.Container(margin=ft.margin.all(5)),
#                ft.Row(
#                    controls=[
#                        self.btn_limpar_form,
#                        self.btn_atualizar,
#                    ],
#                    alignment=ft.MainAxisAlignment.END,
#                ),
#            ]
#        )

#        self.controls = [
#            ft.Container(
#                margin=ft.margin.only(top=10)
#             ),
#            self.formulario_categoria_data_edit,
#        ]


#     @property
#     def view(self)->ft.View:
#         return self._view

#     @view.setter
#     def view(self, nova_view)->None:
#         self._view = nova_view


#     def _btn_limpar_form(self, e:ft.ControlEvent):
#         self.ttf_categoria.value = None
#         self.ttf_descricao.value = None
#         self.page.update()

#     def validar(self) -> tuple:
#         is_valido: bool = True
#         qtde_campos_vazios = 0

#         if self.ttf_categoria.value == "":
#             is_valido = False
#             self.ttf_categoria.error_text = "Informe a categoria."
#             qtde_campos_vazios += 1

#         if self.ttf_descricao.value == "":
#             is_valido = False
#             self.ttf_descricao.error_text = "Informe a descricao."
#             qtde_campos_vazios += 1

#         return is_valido, qtde_campos_vazios


#     def atualizar(self, e):
#         self._db.update_data_categoria(
#             self.eventoCategoria.id,
#             self.ttf_categoria.value,
#             self.ttf_descricao.value
#         )
#         self.page.go("/categoria_data_reload")
#         print('self.page.go("/categoria_data_reload")')


# if __name__ == "__main__":
#     ...
