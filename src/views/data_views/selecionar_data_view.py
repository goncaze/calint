# import flet as ft
# from src.modelo.data import Data
# from src.data.data_db import DataDB
# from src.data.database_singleton import DataDBSingleton
# from src.data.evento_db import EventoDB
# from src.modelo.evento import Evento


# class SelecionarDataView(ft.View):

#     def __init__(self, page: ft.Page, dbs: DataDBSingleton):

#         super().__init__()
#         self.data: Data = None
#         self.page :ft.Page = page
#         self.data_db :DataDB = DataDB(dbs)
#         self.evento_db :EventoDB = EventoDB(dbs)
#         self.appbar :ft.AppBar = ft.AppBar(title=ft.Text(value="Eventos por data"))

#         self.ttf_data = ft.TextField(label="Data", value="", expand=True)

#         self.dtpkr_data = ft.DatePicker(on_change = self.change_date)

#         self.icb_data = ft.IconButton(
#             icon=ft.Icons.CALENDAR_MONTH,
#             on_click=lambda _: self.page.open(self.dtpkr_data),
#         )

#         self.ttb_salvar = ft.TextButton(text="Salvar", on_click=self.salvar)

#         self.linha_ttb = ft.Row(
#             controls=[
#                 self.ttb_salvar,
#             ],
#             alignment=ft.MainAxisAlignment.END
#         )

#         ###
#         # atributo coluna para litar eventos da data selecionada
#         #
#         self.cln_listagem = ft.Column(
#             scroll=ft.ScrollMode.ALWAYS,
#             expand=True,
#         )

#         self.floating_action_button = ft.FloatingActionButton(
#             icon=ft.Icons.ADD,
#             on_click=lambda _: self.page.go("/data_add_evento"),
#         )

#         self.controls = [
#             ft.SafeArea(
#                 # content = ft.Text(value="Selecionar data!")
#                 content = ft.Column(
#                     controls = [
#                         ft.Row(
#                             controls=[
#                                 self.ttf_data,
#                                 self.icb_data,
#                             ],
#                         ),
#                         self.cln_listagem,
#                         self.linha_ttb,
#                     ]
#                 )
#             )
#         ]


#     def listar_eventos(self) -> ft.ListView:
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


#     def carregar_dados(self) -> list[ft.Card]:
#         lista_cards: list[ft.Card] = []

#         self.data = self.data_db.select_uma_data(self.data)

#         if self.data:
#             for evento in self.data.eventos:
#                 txt_evento = ft.Text(
#                     value=evento.evento,
#                     color=ft.Colors.GREY_900,
#                 )

#                 lista_cards.append(
#                     self.add_dados_Linha(txt_evento)
#                 )

#         return lista_cards


#     def add_dados_Linha(
#         self,
#         txt_evento: ft.Text,
#     ) -> ft.Card:

#         # coluna = ft.Column(spacing=1)
#         # coluna.controls.append(linha_categoria)

#         # coluna.controls.append(
#         #     ft.Container(
#         #         content=ft.Row(
#         #             controls=[
#         #                 txt_data,
#         #             ],
#         #             expand=True,
#         #             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#         #         ),
#         #         bgcolor="#00ac41",
#         #         padding=ft.padding.only(left=10, right=10),
#         #         margin=ft.margin.only(top=0, bottom=10, right=0, left=0),
#         #         height=30,
#         #         border_radius=ft.border_radius.all(15),
#         #         gradient=ft.LinearGradient(colors=["#00ac41", "#cbff7f"]),
#         #     )
#         # )

#         # if len(lista_txt_eventos) > 0:
#         #     coluna.controls.append(
#         #         ft.Container(
#         #             content=ft.Text(
#         #                 weight=ft.FontWeight.BOLD,
#         #                 value="Eventos:",
#         #                 color=ft.Colors.BLUE_GREY_900,
#         #                 # color=ft.Colors.AMBER,
#         #             ),
#         #             margin=ft.margin.only(left=10, right=10),
#         #         )
#         #     )

#         #     for txt_evento in lista_txt_eventos:
#         #         coluna.controls.append(
#         #             ft.Container(
#         #                 content=txt_evento,
#         #                 margin=ft.margin.only(left=10, right=10),
#         #             )
#         #         )

#         # SUBSTITUIR POR CARD
#         # container_dados_data = ft.Container(
#         card_dados_data = ft.Card(
#             content=txt_evento,
#             margin=ft.margin.only(right=20),
#             color=ft.Colors.AMBER_200,
#         )

#         return card_dados_data


#     def change_date(self, e: ft.ControlEvent):
#         # print("\n\n\t\t def change_date(self, e: ft.ControlEvent): \n\n")
#         self.ttf_data.value = self.dtpkr_data.value.strftime('%d-%m-%Y')
#         self.data = Data(data=self.dtpkr_data.value.strftime('%Y-%m-%d'))
#         # print(f"{self.data = }\n\n")
#         self.cln_listagem.controls=[self.listar_eventos()]
#         self.ttf_data.update()
#         self.cln_listagem.update()


#     def validar(self) -> bool:
#         is_valido: bool = True
#         if self.ttf_data.value == "":
#             is_valido = False
#             self.ttf_data.error_text = "Selecionar Data"

#         return is_valido


#     def salvar(self, e):
#         if self.validar():
#             ...
