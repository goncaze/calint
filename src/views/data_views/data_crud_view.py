# import flet as ft
# from src.data.data_db import DataDB
# from src.data.database_singleton import DataDBSingleton
# from src.modelo.data_categoria import DataCategoria
# from src.data.data_categoria_db import DataCategoriaDB
# from src.data.evento_db import EventoDB
# from src.modelo.evento import Evento


# class DataCRUDView(ft.View):

#     def __init__(self, page: ft.Page, dbs: DataDBSingleton):

#         super().__init__()

#         self.data_db = DataDB(dbs)
#         self.dataCategoriaDB = DataCategoriaDB(dbs)
#         self.eventoDB = EventoDB(dbs)
#         self.page = page

#         self.ttf_data = ft.TextField(label="Data", hint_text="Data", read_only=True)

#         # --------------------------------------------------
#         ###
#         # DatePick
#         ###
#         def change_date(e):
#             self.ttf_data.value = self.date_picker.value.strftime("%d/%m/%Y")
#             self.ttf_data.update()

#         def date_picker_dismissed(e):
#             print(f"\n\n Date picker dismissed, value is {self.date_picker.value} \n")

#         self.date_picker = ft.DatePicker(
#             on_change=change_date,
#             on_dismiss=date_picker_dismissed,
#             help_text="Selecione uma data",
#         )

#         self.page.overlay.append(self.date_picker)

#         self.data_iconButton = ft.IconButton(
#             icon=ft.Icons.CALENDAR_MONTH,
#             on_click=lambda _: self.date_picker.pick_date(),
#             # data=0,
#         )

#         # ----------------------------------------------------

#         self.dpd_categoria_data = ft.Dropdown(
#             label="Categoria",
#             hint_text="Categoria da data",
#         )

#         self.dpd_eventos = ft.Dropdown(
#             # label="Evento",
#             hint_text="Selecione evento",
#             on_change=self.incluir_dpd_eventos,
#         )

#         self.delete_iconButton = ft.IconButton(
#             icon=ft.Icons.DELETE,
#             on_click=...,  # lambda _: self.date_picker.pick_date(),
#             # data=0,
#         )

#         self.formulario_eventos = ft.Column(controls=[self.dpd_eventos])

#         self.btn_registrar = ft.ElevatedButton(text="Salvar", on_click=self.registrar)

#         self.btn_limpar_form = ft.ElevatedButton(
#             text="Limpar", on_click=self.limpar_form
#         )

#         self.formulario_data_create = ft.Column(
#             controls=[
#                 ft.Row(controls=[self.ttf_data, self.data_iconButton]),
#                 self.dpd_categoria_data,
#                 ft.Text(
#                     spans=[ft.TextSpan(text="Eventos", style=ft.TextStyle(size=20))],
#                     weight=ft.FontWeight.BOLD,
#                     color=ft.Colors.BLUE,
#                 ),
#                 self.formulario_eventos,
#                 ft.Container(margin=ft.margin.all(5)),
#                 ft.Row(
#                     controls=[
#                         self.btn_limpar_form,
#                         self.btn_registrar,
#                     ],
#                     alignment=ft.MainAxisAlignment.END,
#                 ),
#             ]
#         )

#         self.controls = [
#             ft.Column(
#                 controls=[self.formulario_data_create],
#                 scroll=ft.ScrollMode.ALWAYS,
#                 expand=True,
#             )
#         ]

#         self.listar_categoria_data()
#         self.listar_eventos()

#     @property
#     def view(self) -> ft.View:
#         return self.view

#     @view.setter
#     def view(self, nova_view) -> None:
#         self.view = nova_view

#     def limpar_form(self, e: ft.ControlEvent):
#         self.ttf_data.value = None
#         self.ttf_descricao.value = None
#         self.atualizar_page()

#     def validar(self) -> tuple:
#         is_valido: bool = True
#         qtde_campos_vazios = 0

#         if self.ttf_data.value == "":
#             is_valido = False
#             self.ttf_data.error_text = "Informe a evento."
#             qtde_campos_vazios += 1

#         if self.ttf_descricao.value == "":
#             is_valido = False
#             self.ttf_descricao.error_text = "Informe a descricao."
#             qtde_campos_vazios += 1

#         return is_valido, qtde_campos_vazios

#     def listar_categoria_data(self):
#         for categoriaData in self.dataCategoriaDB.select_data_categoria_todos():
#             dpd = ft.dropdown.Option(
#                 data=categoriaData,
#                 text=categoriaData.categoria,
#             )
#             self.dpd_categoria_data.options.append(dpd)

#     def listar_eventos(self):
#         for evento in self.eventoDB.select_evento_todos():
#             dpd = ft.dropdown.Option(
#                 data=evento,
#                 text=evento.evento,
#             )
#             self.dpd_eventos.options.append(dpd)

#     def categoria_data_selecionada(self) -> DataCategoria:
#         for opcao in self.dpd_categoria_data.options:
#             if opcao.text == self.dpd_categoria_data.value:
#                 return opcao.data
#         return None

#     def eventos_selecionados(self) -> list[Evento]:
#         lista_eventos: list[Evento] = []

#         for dpd_mais_evts in self.formulario_eventos.controls:
#             for opcao in dpd_mais_evts.options:
#                 if opcao.text == dpd_mais_evts.value:
#                     lista_eventos.append(opcao.data)

#         return lista_eventos

#     def novo_dpd_eventos(self):
#         novo_dpd_eventos = ft.Dropdown(
#             # label="Evento",
#             hint_text="Selecione evento",
#             on_change=self.incluir_dpd_eventos,
#         )

#         for evento in self.eventoDB.select_evento_todos():
#             dpd = ft.dropdown.Option(
#                 data=evento,
#                 text=evento.evento,
#             )
#             novo_dpd_eventos.options.append(dpd)
#         return novo_dpd_eventos

#     def incluir_dpd_eventos(self, e):
#         self.formulario_eventos.controls.append(self.novo_dpd_eventos())
#         self.page.update()

#     def registrar(self, e):
#         pass

#     def atualizar_page(self):
#         pass


# if __name__ == "__main__":
#     ...
