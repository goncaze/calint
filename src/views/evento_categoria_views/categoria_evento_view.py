import flet as ft
from src.modelo.evento_categoria import EventoCategoria
from src.data.database_singleton import DataDBSingleton
from src.data.evento_categoria_db import EventoCategoriaDB


class CategoriaEventoView(ft.View):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.route = "/categoria_evento"
        self.bgcolor = ft.colors.WHITE
        self.appbar = ft.AppBar(title=ft.Text("Categorias de evento"))
        self.page = page
        self.evento_categoria_db = EventoCategoriaDB(dbs)

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=lambda _: self.page.go("/categoria_evento_create"),
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

        for item in self.carregar_categorias():
            lw_lista.controls.append(item)

        return lw_lista

    def carregar_categorias(self):
        lista_containers: list[ft.Container] = []

        for eventoCategoria in self.evento_categoria_db.select_evento_categoria_todos():
            txt_categoria = ft.Text(
                spans=[
                    ft.TextSpan(
                        text=eventoCategoria.categoria,
                        data=eventoCategoria,
                    )
                ],
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE,
            )

            txt_descricao = ft.Text(
                value=eventoCategoria.descricao,
            )

            txt_cor = ft.Text(
                value=eventoCategoria.cor,
            )

            lista_containers.append(
                self.add_categoria_Linha(txt_categoria, txt_descricao, txt_cor)
            )

        return lista_containers

    def add_categoria_Linha(
        self, txt_categoria: ft.Text, txt_descricao: ft.Text, txt_cor: ft.Text
    ) -> ft.Container:

        linha1 = ft.Row(
            controls=[
                txt_categoria,
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.EDIT_DOCUMENT,
                            icon_color=ft.colors.CYAN_100,  # "#2ba84a",
                            tooltip="Editar",
                            on_click=self.icb_editar,
                            data=txt_categoria.spans[0].data,  # Objeto dataCategoria
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=self.deletar,
                            data=txt_categoria.spans[0].data,  # Objeto dataCategoria
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
                    value="Cor:",
                ),
                ft.Container(
                    bgcolor=txt_cor.value,  # "#a233c4", #
                    width=50,
                    height=15,
                ),
            ],
            spacing=5,
        )

        coluna = ft.Column(controls=[linha1, linha2, linha3], spacing=1)

        container_categorias = ft.Container(
            content=coluna, margin=ft.margin.only(right=15, left=15)
        )

        return container_categorias

    def deletar(self, e: ft.ControlEvent):
        eventoCategoria: EventoCategoria = e.control.data
        self.evento_categoria_db.delete_evento_categoria(eventoCategoria.id)

        self.page.go("/categoria_evento_delete_reload")

    def icb_editar(self, e: ft.ControlEvent):
        eventoCategoria: EventoCategoria = e.control.data
        rota = "/categoria_evento_edit__-__" + str(eventoCategoria.id)
        self.page.go(rota)

    # def ver_categorias_data(db: DataDB):
    #     """Listagem de categorias"""
    #     print("\n\n Categorias disponíves: \n")
    #     for eventoCategoria in db.select_evento_categoria_todos():
    #         print(eventoCategoria)
