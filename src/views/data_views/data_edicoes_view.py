# import flet as ft
# from src.modelo.data import Data
# from src.data.data_db import DataDB
# from src.data.database_singleton import DataDBSingleton


# class DataEdicoesView(ft.View):

#     def __init__(self, page: ft.Page, dbs: DataDBSingleton):
#         super().__init__()
#         self.route = "/data_edicoes"
#         # self.appbar = ft.AppBar(title=ft.Text("Data Edições"), bgcolor="#008B00")
#         self.appbar = ft.AppBar(title=ft.Text("Data Edições"))

#         self.page = page
#         self.data_db = DataDB(dbs)

#         # self.floating_action_button = ft.FloatingActionButton(
#         #     icon=ft.Icons.ADD,
#         #     on_click=lambda _: self.page.go("/data_create"),
#         # )

#         self.controls = [
#             ft.Column(
#                 controls=[self.listagem()],  # <<<<<<<<<<<<<<<<<<<<<<<<
#                 # controls=[???????],
#                 scroll=ft.ScrollMode.ALWAYS,
#                 expand=True,
#             )
#         ]

#     def listagem(self) -> ft.ListView:
#         # Uma visualização em formato de lista
#         lw_lista = ft.ListView(
#             # Os itens serão organizados verticalmente
#             horizontal=False,
#             # Um espaçamento para componentes do entorno
#             spacing=20,
#             # Espessura do divisor entre os itens da ListView
#             divider_thickness=2,
#         )

#         for item in self.carregar_dados():
#             lw_lista.controls.append(item)

#         return lw_lista

#     def carregar_dados(self) -> list[ft.Container]:
#         lista_containers: list[ft.Container] = []

#         for data in self.data_db.select_data_todas():
#             txt_data = ft.Text(
#                 spans=[
#                     ft.TextSpan(
#                         text=data.data,  # .strftime("%d/%m/%Y"),
#                         data=data,
#                     )
#                 ],
#                 weight=ft.FontWeight.BOLD,
#                 color=ft.Colors.BLUE,
#             )

#             txt_categoria = ft.Text(
#                 value=data.data_categoria.categoria,
#             )

#             lista_txt_eventos: list[ft.Text] = []
#             for evento in data.eventos:
#                 txt_evento = ft.Text(
#                     value=evento.evento,
#                 )
#                 lista_txt_eventos.append(txt_evento)

#             lista_containers.append(
#                 self.add_dados_Linha(txt_data, txt_categoria, lista_txt_eventos)
#             )

#         return lista_containers

#     def add_dados_Linha(
#         self,
#         txt_data: ft.Text,
#         txt_categoria: ft.Text,
#         lista_txt_eventos: list[ft.Text],
#     ) -> ft.Container:

#         coluna = ft.Column(spacing=1)

#         if txt_data is not None:
#             linha1 = ft.Row(
#                 controls=[
#                     txt_data,
#                     ft.Row(
#                         controls=[
#                             ft.IconButton(
#                                 icon=ft.Icons.EDIT_DOCUMENT,
#                                 icon_color=ft.Colors.CYAN_100,  # "#2ba84a",
#                                 tooltip="Editar",
#                                 on_click=self.icb_editar,
#                                 data=txt_data.spans[0].data,  # Objeto evento
#                                 padding=0,
#                             ),
#                             ft.IconButton(
#                                 icon=ft.Icons.DELETE,
#                                 on_click=self.deletar,
#                                 data=txt_data.spans[0].data,  # Objeto evento
#                                 padding=0,
#                             ),
#                         ],
#                         alignment=ft.MainAxisAlignment.END,
#                     ),
#                 ],
#                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#             )
#             coluna.controls.append(linha1)

#         if txt_categoria is not None:
#             linha2 = ft.Row(
#                 controls=[
#                     ft.Text(
#                         weight=ft.FontWeight.BOLD,
#                         value="Categoria:",
#                     ),
#                     txt_categoria,
#                 ],
#                 spacing=5,
#             )
#             coluna.controls.append(linha2)

#         if len(lista_txt_eventos) > 0:
#             coluna.controls.append(
#                 ft.Text(
#                     weight=ft.FontWeight.BOLD,
#                     value="Eventos:",
#                 ),
#             )
#             for txt_evento in lista_txt_eventos:
#                 linha_evento = ft.Row(
#                     controls=[
#                         # ft.Text(
#                         #     weight=ft.FontWeight.BOLD,
#                         #     value="Evento:",
#                         # ),
#                         txt_evento,
#                     ],
#                     spacing=5,
#                 )
#                 coluna.controls.append(linha_evento)

#         # coluna = ft.Column(controls=[linha1, linha2], spacing=1)

#         container_categorias = ft.Container(
#             content=coluna, margin=ft.margin.only(right=15, left=15)
#         )

#         return container_categorias

#     def deletar(self, e: ft.ControlEvent):
#         data: Data = e.control.data
#         self.data_db.delete_data(data)
#         self.page.go("/data_delete_reload")

#     # def icb_editar(self, e: ft.ControlEvent):
#     #     print("\n\n\t def icb_editar(self, e: ft.ControlEvent): \n\n")
#     #     data: Data = e.control.data
#     #     rota = "/data_edit__-__" + str(data.id)
#     #     self.page.go(rota)

#     def icb_editar(self, e: ft.ControlEvent):
#         print("\n\n\t def icb_editar(self, e: ft.ControlEvent): \n\n")
#         data: Data = e.control.data
#         rota = "/data_edicoes__-__" + str(data.id)
#         self.page.go(rota)

#     # def ver_categorias_data(db:DataDB):
#     #     """ Listagem de categorias"""
#     #     print("\n\n Categorias disponíves: \n")
#     #     for eventoCategoria in db.select_evento_categoria_todos():
#     #         print(eventoCategoria)


# if __name__ == "__main__":
#     ...
