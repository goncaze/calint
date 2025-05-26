# import flet as ft
# from src.data.data_db import DataDB
# from src.data.database_singleton import DataDBSingleton


# class DataView(ft.View):

#     def __init__(self, page: ft.Page, dbs: DataDBSingleton):
#         super().__init__()
#         self.route = "/datas"
#         self.appbar = ft.AppBar(
#             title=ft.Text("Datas"), bgcolor="#005400", color=ft.Colors.WHITE
#         )
#         self.bgcolor = ft.Colors.WHITE
#         # self.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

#         self.page = page
#         self.data_db = DataDB(dbs)

#         self.floating_action_button = ft.FloatingActionButton(
#             icon=ft.Icons.ADD,
#             on_click=lambda _: self.page.go("/selecionar_data"),
#         )

#         self.controls = [
#             ft.Column(
#                 controls=[self.listar_datas()],
#                 scroll=ft.ScrollMode.ALWAYS,
#                 expand=True,
#             )
#         ]

#     def listar_datas(self) -> ft.ListView:
#         # Uma visualização em formato de lista
#         lw_lista = ft.ListView(
#             # Os itens serão organizados verticalmente
#             horizontal=False,
#             # Um espaçamento para componentes do entorno
#             spacing=20,
#             # Espessura do divisor entre os itens da ListView
#             # divider_thickness=1,
#         )

#         for item in self.carregar_dados():
#             lw_lista.controls.append(item)

#         lw_lista.controls.append(ft.Container(height=50))
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
#                 color=ft.Colors.GREY_100,
#             )

#             # txt_categoria = ft.Text(
#             #     value=data.data_categoria.categoria,
#             #     color="#000068",
#             # )

#             lista_txt_eventos: list[ft.Text] = []
#             for evento in data.eventos:
#                 txt_evento = ft.Text(
#                     value=evento.evento,
#                     color=ft.Colors.GREY_900,
#                 )
#                 lista_txt_eventos.append(txt_evento)

#             lista_containers.append(
#                 # self.add_dados_Linha(txt_data, txt_categoria, lista_txt_eventos)
#                 self.add_dados_Linha(txt_data, lista_txt_eventos)

#             )

#         return lista_containers

#     def add_dados_Linha(
#         self,
#         txt_data: ft.Text,
#         # txt_categoria: ft.Text,
#         lista_txt_eventos: list[ft.Text],
#     ) -> ft.Container:

#         coluna = ft.Column(spacing=1)
#         # coluna.controls.append(linha_categoria)

#         coluna.controls.append(
#             ft.Container(
#                 content=ft.Row(
#                     controls=[
#                         txt_data,
#                     ],
#                     expand=True,
#                     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                 ),
#                 bgcolor="#00ac41",
#                 padding=ft.padding.only(left=10, right=10),
#                 margin=ft.margin.only(top=0, bottom=10, right=0, left=0),
#                 height=30,
#                 border_radius=ft.border_radius.all(15),
#                 gradient=ft.LinearGradient(colors=["#00ac41", "#cbff7f"]),
#             )
#         )

#         if len(lista_txt_eventos) > 0:
#             coluna.controls.append(
#                 ft.Container(
#                     content=ft.Text(
#                         weight=ft.FontWeight.BOLD,
#                         value="Eventos:",
#                         color=ft.Colors.BLUE_GREY_900,
#                         # color=ft.Colors.AMBER,
#                     ),
#                     margin=ft.margin.only(left=10, right=10),
#                 )
#             )

#             for txt_evento in lista_txt_eventos:
#                 coluna.controls.append(
#                     ft.Container(
#                         content=txt_evento,
#                         margin=ft.margin.only(left=10, right=10),
#                     )
#                 )

#         # SUBSTITUIR POR CARD
#         # container_dados_data = ft.Container(
#         card_dados_data = ft.Card(
#             content=coluna,
#             margin=ft.margin.only(right=20),
#             color=ft.Colors.AMBER_200,
#         )

#         return card_dados_data
