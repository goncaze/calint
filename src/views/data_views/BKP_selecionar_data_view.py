# import flet as ft
# from src.modelo.data import Data
# from src.data.data_db import DataDB
# from src.data.database_singleton import DataDBSingleton
# from src.modelo.data_categoria import DataCategoria
# from src.data.data_categoria_db import DataCategoriaDB
# from src.data.evento_db import EventoDB
# from src.modelo.evento import Evento
# from src.views.data_views.dropdown_evento import DropDownEvento


# class SelecionarDataView(ft.View):

#     def __init__(self, page: ft.Page, dbs: DataDBSingleton):

#         super().__init__()
#         self.data: Data = None
#         self.data_db = DataDB(dbs)
#         self.dataCategoriaDB = DataCategoriaDB(dbs)
#         self.eventoDB = EventoDB(dbs)
#         self.page = page

#         self.ttf_data = ft.TextField(
#             label="Data",
#             hint_text="Data",
#             expand=True,
#             disabled=True,
#         )

#         # --------------------------------------------------
#         ###
#         # DatePick
#         ###
#         def change_date(e):
#             self.ttf_data.value = self.date_picker.value.strftime("%d/%m/%Y")
#             self.buscar_dados_data(self.ttf_data.value)
#             self.ttf_data.update()

#         def date_picker_dismissed(e):
#             self.page.go(route="/data_reload")

#         self.date_picker = ft.DatePicker(
#             on_change=change_date,
#             on_dismiss=date_picker_dismissed,
#             help_text="Selecione uma data",
#             open=True,
#         )

#         # self.page.overlay.append(self.date_picker)
#         # self.page.open(self.date_picker)

#         # ----------------------------------------------------

#         self.dpd_categoria_data = ft.Dropdown(
#             label="Categoria",
#             hint_text="Categoria da data",
#         )

#         self.dpd_eventos = DropDownEvento(
#             ft.Dropdown(
#                 hint_text="Selecione evento",
#                 on_change=self.incluir_novo_dpd_evento,
#                 options=self.listar_eventos_options(),
#             ),
#             self.delete_dpd_evento,
#         )

#         self.coluna_eventos = ft.Column()

#         self.coluna_de_eventos_titulo = ft.Column(
#             controls=[
#                 ft.Text(
#                     spans=[ft.TextSpan(text="Eventos", style=ft.TextStyle(size=20))],
#                     weight=ft.FontWeight.BOLD,
#                     color=ft.colors.BLUE,
#                 ),
#                 self.coluna_eventos,
#             ],
#             visible=False,
#         )

#         self.btn_ir_a_eventos = ft.ElevatedButton(
#             text="Próximo", on_click=self.de_categoria_para_eventos
#         )

#         self.btn_registrar = ft.ElevatedButton(
#             text="Salvar", on_click=self.registrar, visible=False
#         )

#         self.btn_cancelar = ft.ElevatedButton(text="Cancelar", on_click=self.cancelar)

#         self.formulario_anotar_data = ft.Column(
#             controls=[
#                 ft.Row(controls=[self.ttf_data]),
#                 self.dpd_categoria_data,
#                 self.coluna_de_eventos_titulo,
#                 ft.Container(margin=ft.margin.all(5)),
#                 ft.Row(
#                     controls=[
#                         self.btn_cancelar,
#                         self.btn_ir_a_eventos,
#                         self.btn_registrar,
#                     ],
#                     alignment=ft.MainAxisAlignment.END,
#                 ),
#             ]
#         )

#         self.controls = [
#             ft.Column(
#                 controls=[self.formulario_anotar_data],
#                 scroll=ft.ScrollMode.ALWAYS,
#                 expand=True,
#             )
#         ]

#         self.listar_categoria_data()


#         # self.page.overlay.append(self.date_picker)
#         self.page.open(self.date_picker)



#     @property
#     def view(self) -> ft.View:
#         return self.view

#     @view.setter
#     def view(self, nova_view) -> None:
#         self.view = nova_view

#     def cancelar(self, e: ft.ControlEvent):
#         self.page.go(route="/data_reload")

#     def de_categoria_para_eventos(self, e):
#         if self.validar_categoria():
#             self.coluna_de_eventos_titulo.visible = True
#             self.coluna_de_eventos_titulo.update()
#             self.dpd_categoria_data.disabled = True
#             self.dpd_categoria_data.update()
#             self.btn_ir_a_eventos.visible = False
#             self.btn_ir_a_eventos.update()
#             self.btn_registrar.visible = True
#             self.btn_registrar.update()

#     def ver_categoria_e_eventos(self):
#         self.coluna_de_eventos_titulo.visible = True
#         self.coluna_de_eventos_titulo.update()
#         self.btn_ir_a_eventos.visible = False
#         self.btn_ir_a_eventos.update()
#         self.btn_registrar.visible = True
#         self.btn_registrar.update()

#     def validar_categoria(self) -> bool:
#         if self.categoria_data_selecionada() is None:
#             self.dpd_categoria_data.error_text = "Informe a categoria."
#             self.dpd_categoria_data.update()
#             return False
#         self.dpd_categoria_data.error_text = ""
#         self.dpd_categoria_data.update()
#         return True

#     def listar_categoria_data(self):
#         for categoriaData in self.dataCategoriaDB.select_data_categoria_todos():
#             dpd = ft.dropdown.Option(
#                 data=categoriaData,
#                 text=categoriaData.categoria,
#             )
#             self.dpd_categoria_data.options.append(dpd)

#     def listar_eventos_options(self) -> list:
#         lista = []
#         for evento in self.eventoDB.select_evento_todos():
#             lista.append(
#                 ft.dropdown.Option(
#                     data=evento,
#                     text=evento.evento,
#                 )
#             )
#         return lista

#     def categoria_data_selecionada(self) -> DataCategoria:
#         for opcao in self.dpd_categoria_data.options:
#             if opcao.text == self.dpd_categoria_data.value:
#                 return opcao.data
#         return None

#     def eventos_selecionados(self) -> list[Evento]:
#         lista_eventos: list[Evento] = []

#         for obj_dropdown_envento in self.coluna_eventos.controls:
#             for opcao in obj_dropdown_envento.dpd_evento.options:
#                 if opcao.text == obj_dropdown_envento.dpd_evento.value:
#                     lista_eventos.append(opcao.data)

#         return lista_eventos

#     def novo_dpd_evento(self) -> DropDownEvento:
#         novo_dpd_evento = DropDownEvento(
#             ft.Dropdown(
#                 hint_text="Selecione evento",
#                 on_change=self.incluir_novo_dpd_evento,
#                 options=self.listar_eventos_options(),
#             ),
#             self.delete_dpd_evento,
#         )
#         return novo_dpd_evento

#     def incluir_novo_dpd_evento(self, e):
#         self.coluna_eventos.controls.append(self.novo_dpd_evento())
#         self.page.update()

#     def restaurar_dpd_evento(self, dpd_evento: DropDownEvento):
#         self.coluna_eventos.controls.append(dpd_evento)
#         self.page.update()

#     def delete_dpd_evento(self, dpd_evento: DropDownEvento):
#         self.coluna_eventos.controls.remove(dpd_evento)
#         self.coluna_eventos.update()

#     def registrar(self, e):
#         print(f"\n\ndef registrar(self, e):\n")
#         if self.data:
#             print(f"\n\n\tTRUE if self.data:\n")
#             self.data.data_categoria = self.categoria_data_selecionada()
#             self.data.eventos = self.eventos_selecionados()
#             self.data_db.update_data(self.data)
#         else:
#             print(f"\n\n\tFALSE if self.data:\n")
#             self.data = Data(
#                 data=self.ttf_data.value,
#                 data_categoria=self.categoria_data_selecionada(),
#                 eventos=self.eventos_selecionados(),
#             )
#             self.data_db.insert_data(self.data)
#         self.page.go("/data_reload")

#     def atualizar_page(self):
#         pass

#     def buscar_dados_data(self, data_str: str):
#         self.data = self.data_db.select_uma_data(Data(data=data_str))
#         if self.data:
#             self.dpd_categoria_data.value = self.data.data_categoria.categoria
#             self.dpd_categoria_data.update()
#             for evento in self.data.eventos:
#                 # =========
#                 dpd_evento = ft.Dropdown(
#                     hint_text="Selecione evento",
#                     on_change=self.incluir_novo_dpd_evento,
#                     options=self.listar_eventos_options(),
#                 )

#                 dpd_evento.value = evento.evento

#                 self.restaurar_dpd_evento(
#                     DropDownEvento(
#                         dpd_evento,
#                         self.delete_dpd_evento,
#                     )
#                 )
#             self.ver_categoria_e_eventos()

#         dpd_evento = ft.Dropdown(
#             hint_text="Selecione evento",
#             on_change=self.incluir_novo_dpd_evento,
#             options=self.listar_eventos_options(),
#         )

#         self.restaurar_dpd_evento(
#             DropDownEvento(
#                 dpd_evento,
#                 self.delete_dpd_evento,
#             )
#         )
