# import flet as ft
# from src.modelo.evento import Evento
# from src.modelo.data import Data
# from src.data.data_db import DataDB
# from src.data.database_singleton import DataDBSingleton
# from src.views.data_views.data_crud_view import DataCRUDView


# class DataEditView(DataCRUDView):

#     def __init__(self, id: int, page: ft.Page, dbs: DataDBSingleton):
#         # print("\n\n\tclass DataEditView(DataCRUDView):\n\n")
#         super().__init__(page, dbs)
#         self.route = "/data_edit"
#         # self.appbar = ft.AppBar(title=ft.Text(value="Editar data"), bgcolor="#008B00")
#         self.appbar = ft.AppBar(title=ft.Text(value="Editar data"))

#         self.dataDB = DataDB(dbs)
#         self.data: Data = self.dataDB.select_uma_data(Data(id))
#         self.page: ft.Page = page

#         self.ttf_data.value = self.data.data
#         # self.ttf_descricao.value = self.data.descricao
#         # self.dpd_eventos.value = self.data.evento_categoria.categoria
#         self.dpd_categoria_data.value = self.data.data_categoria.categoria
#         self.incluir_dpd_eventos_selecionados()

#     def incluir_dpd_eventos_selecionados(self):
#         lista_eventos: list[Evento] = self.data.eventos
#         if len(lista_eventos) > 1:
#             self.dpd_eventos.value = lista_eventos[0].evento
#             lista_eventos.pop(0)
#         for evento in lista_eventos:
#             dpd_eventos_selecionado = self.novo_dpd_eventos()
#             dpd_eventos_selecionado.value = evento.evento
#             self.formulario_eventos.controls.append(dpd_eventos_selecionado)

#         self.formulario_eventos.controls.append(self.novo_dpd_eventos())
#         self.page.update()

#     def registrar(self, e):

#         print("\n\n\t def registrar(self, e): \n\n")

#         self.data.data_categoria = self.categoria_data_selecionada()
#         self.data.eventos = self.eventos_selecionados()

#         self.dataDB.update_data(self.data)
#         self.page.go("/data_reload")

#     def atualizar_page(self):
#         self.page.update()
