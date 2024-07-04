# import flet as ft
# from src.modelo.data import Data
# from src.data.data_db import DataDB
# from src.data.database_singleton import DataDBSingleton
# from src.views.data_views.data_crud_view import DataCRUDView


# class DataCreateView(DataCRUDView):

#     def __init__(self, page: ft.Page, dbs: DataDBSingleton):
#         super().__init__(page, dbs)
#         self.route = "/data_create"
#         self.appbar = ft.AppBar(
#             # title=ft.Text(value="Cadastrar evento"), bgcolor="#008B00"
#             title=ft.Text(value="Cadastrar evento")
#         )

#         self.page: ft.Page = page
#         self.data_db = DataDB(dbs)

#     def registrar(self, e):
#         data = Data(
#             id=0,
#             data=self.ttf_data.value,
#             data_categoria=self.categoria_data_selecionada(),
#             eventos=self.eventos_selecionados(),
#         )
#         self.data_db.insert_data(data)
#         self.page.go("/data_reload")

#     def atualizar_page(self):
#         self.page.update()


# if __name__ == "__main__":
#     ...
