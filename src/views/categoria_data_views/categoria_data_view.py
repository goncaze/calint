import flet as ft
from src.modelo.data_categoria import DataCategoria
from src.data.database_singleton import DataDBSingleton
from src.data.data_categoria_db import DataCategoriaDB


class CategoriaDataView(ft.View):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.route = "/categoria_data"
        # self.appbar = ft.AppBar(title=ft.Text("Categorias de data"), bgcolor="#008B00")
        self.appbar = ft.AppBar(title=ft.Text("Categorias de data"))

        self.page = page
        self.data_categoria_db = DataCategoriaDB(dbs)

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            on_click=lambda _: self.page.go("/categoria_data_create"),
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

        for dataCategoria in self.data_categoria_db.select_data_categoria_todos():
            txt_categoria = ft.Text(
                spans=[
                    ft.TextSpan(
                        text=dataCategoria.categoria,
                        data=dataCategoria,
                    )
                ],
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE,
            )

            txt_descricao = ft.Text(
                value=dataCategoria.descricao,
            )

            lista_containers.append(
                self._add_categoria_Linha(txt_categoria, txt_descricao)
            )

        return lista_containers

    def _add_categoria_Linha(
        self, txt_categoria: ft.Text, txt_descricao: ft.Text
    ) -> ft.Container:

        linha1 = ft.Row(
            controls=[
                txt_categoria,
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.EDIT_DOCUMENT,
                            icon_color=ft.Colors.CYAN_100,  # "#2ba84a",
                            tooltip="Editar",
                            on_click=self._icb_editar,
                            data=txt_categoria.spans[0].data,  # Objeto dataCategoria
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            on_click=self._deletar,
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

        coluna = ft.Column(controls=[linha1, linha2], spacing=1)

        container_categorias = ft.Container(
            content=coluna, margin=ft.margin.only(right=15, left=15)
        )
        return container_categorias

    def _deletar(self, e: ft.ControlEvent):
        dataCategoria: DataCategoria = e.control.data
        self.data_categoria_db.delete_data_categoria(dataCategoria.id)
        self.page.go("/categoria_data_delete_reload")

    def _icb_editar(self, e: ft.ControlEvent):
        dataCategoria: DataCategoria = e.control.data
        rota = "/categoria_data_edit__-__" + str(dataCategoria.id)
        self.page.go(rota)

    def ver_categorias_data(self):
        """Listagem de categorias"""
        print("\n\n Categorias disponíves: \n")
        for categoria in self.data_categoria_db.select_data_categoria_todos():
            print(categoria)
