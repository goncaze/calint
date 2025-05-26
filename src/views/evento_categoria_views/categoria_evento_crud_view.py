import flet as ft
from src.modelo.evento_categoria import EventoCategoria
from src.views.controles.seletor import SeletorCor


class CategoriaEventoCRUDView(ft.View):

    def __init__(self):
        super().__init__()
        self.bgcolor = ft.Colors.WHITE
        self.ttf_categoria = ft.TextField(
            label="Categoria",
            hint_text="Categoria",
        )

        self.ttf_descricao = ft.TextField(
            label="Descricao",
            hint_text="Descricao",
        )

        self.ttf_cor = ft.TextField(
            label="Cor",
            hint_text="Cor",
            expand=True,
        )

        self.ttb_selecionar = ft.TextButton(
            text="Selecionar", on_click=self.selecionar_cor
        )
        self.seletor_de_cores = SeletorCor()
        self.seletor_de_cores.actions = [
            ft.TextButton(
                text="Fechar", on_click=lambda e: self.page.close(self.seletor_de_cores)
            ),
            self.ttb_selecionar,
        ]

        self.ttb_select_cor = ft.TextButton(
            text="alterar cor",
            icon=ft.Icons.COLOR_LENS,
            expand=True,
            on_click=lambda e: self.page.open(self.seletor_de_cores),
        )

        self.btn_registrar = ft.ElevatedButton(text="Salvar", on_click=self.registrar)

        self.btn_limpar_form = ft.ElevatedButton(
            text="Limpar", on_click=self.btn_limpar_form
        )

        self.formulario_categoria_create = ft.Column(
            controls=[
                self.ttf_categoria,
                self.ttf_descricao,
                ft.Row(controls=[self.ttf_cor, self.ttb_select_cor]),
                ft.Container(margin=ft.margin.all(5)),
                ft.Row(
                    controls=[
                        self.btn_limpar_form,
                        self.btn_registrar,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        )

        self.controls = [
            ft.Container(margin=ft.margin.only(top=10)),
            self.formulario_categoria_create,
        ]

    def selecionar_cor(self, e: ft.ControlEvent):
        self.ttf_cor.value = self.seletor_de_cores.data
        self.ttf_cor.update()
        self.page.close(self.seletor_de_cores)

    @property
    def view(self) -> ft.View:
        return self.view

    @view.setter
    def view(self, nova_view) -> None:
        self.view = nova_view

    def btn_limpar_form(self, e: ft.ControlEvent):
        self.ttf_categoria.value = None
        self.ttf_descricao.value = None
        self.ttf_cor.value = None
        self.atualizar_page()

    def atualizar_page(self):
        pass

    def validar(self) -> bool:
        is_valido: bool = True
        if self.ttf_categoria.value == "":
            is_valido = False
            self.ttf_categoria.error_text = "Informe a categoria."
        return is_valido

    def registrar(self, e):
        pass


if __name__ == "__main__":
    ...
