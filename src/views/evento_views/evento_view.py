import flet as ft
from src.modelo.evento import Evento
from src.data.database_singleton import DataDBSingleton
from src.data.evento_db import EventoDB


class EventoView(ft.View):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.route = "/eventos"
        self.bgcolor = ft.Colors.WHITE
        self.appbar = ft.AppBar(title=ft.Text("Eventos"))
        self.page = page
        self.evento_db = EventoDB(dbs)

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            on_click=lambda _: self.page.go("/evento_create"),
        )

        self.controls = [
            ft.Column(
                controls=[self.listagem()],
                scroll=ft.ScrollMode.ALWAYS,
                expand=True,
            )
        ]

    def listagem(self) -> ft.ListView:
        # Uma visualização em formato de lista
        lw_lista = ft.ListView(
            # Os itens serão organizados verticalmente
            horizontal=False,
            # Um espaçamento para componentes do entorno
            spacing=20,
            # Espessura do divisor entre os itens da ListView
            divider_thickness=2,
        )

        for item in self.carregar_dados():
            lw_lista.controls.append(item)

        return lw_lista

    def carregar_dados(self) -> list[ft.Container]:
        lista_containers: list[ft.Container] = []

        for evento in self.evento_db.select_evento_todos():
            txt_evento = ft.Text(
                spans=[
                    ft.TextSpan(
                        text=evento.evento,
                        data=evento,
                    )
                ],
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE,
            )

            txt_descricao = ft.Text(
                value=evento.descricao,
            )

            txt_categoria = ft.Text(
                value=evento.evento_categoria.categoria,
            )

            lista_containers.append(
                self.add_dados_Linha(txt_evento, txt_descricao, txt_categoria)
            )

        return lista_containers

    def add_dados_Linha(
        self, txt_evento: ft.Text, txt_descricao: ft.Text, txt_categoria: ft.Text
    ) -> ft.Container:

        linha1 = ft.Row(
            controls=[
                txt_evento,
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.EDIT_DOCUMENT,
                            icon_color=ft.Colors.CYAN_100,  # "#2ba84a",
                            tooltip="Editar",
                            on_click=self.icb_editar,
                            data=txt_evento.spans[0].data,  # Objeto evento
                            padding=0,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            on_click=self.deletar,
                            data=txt_evento.spans[0].data,  # Objeto evento
                            padding=0,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        linha2 = ft.Row(
            controls=[
                ft.Text(
                    weight=ft.FontWeight.BOLD,
                    value="Descrição:",
                ),
                txt_descricao,
            ],
            spacing=5,
        )

        linha3 = ft.Row(
            controls=[
                ft.Text(
                    weight=ft.FontWeight.BOLD,
                    value="Categoria:",
                ),
                txt_categoria,
            ],
            spacing=5,
        )

        coluna = ft.Column(controls=[linha1, linha2, linha3], spacing=1)

        container_categorias = ft.Container(
            content=coluna, margin=ft.margin.only(right=15, left=15)
        )

        return container_categorias

    def deletar(self, e: ft.ControlEvent):
        evento: Evento = e.control.data
        self.evento_db.delete_evento(evento.id)
        self.page.go("/evento_delete_reload")

    def icb_editar(self, e: ft.ControlEvent):
        evento: Evento = e.control.data
        rota = "/evento_edit__-__" + str(evento.id)
        self.page.go(rota)
