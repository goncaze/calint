import flet as ft


class CategoriaDataCRUDView(ft.View):

    def __init__(self):
        super().__init__()

        self.ttf_categoria = ft.TextField(
            label="Categoria",
            hint_text="Categoria",
        )

        self.ttf_descricao = ft.TextField(
            label="descricao",
            hint_text="descricao",
        )

        self.btn_registrar = ft.ElevatedButton(text="Salvar", on_click=self.registrar)

        self.btn_limpar_form = ft.ElevatedButton(
            text="Limpar", on_click=self.btn_limpar_form
        )

        self.formulario_categoria_data_create = ft.Column(
            controls=[
                self.ttf_categoria,
                self.ttf_descricao,
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
            self.formulario_categoria_data_create,
        ]

    @property
    def view(self) -> ft.View:
        return self._view

    @view.setter
    def view(self, nova_view) -> None:
        self._view = nova_view

    def btn_limpar_form(self, e: ft.ControlEvent):
        self.ttf_categoria.value = None
        self.ttf_descricao.value = None
        self.atualizar_page()

    def atualizar_page(self):
        pass

    def validar(self) -> tuple:
        is_valido: bool = True
        if self.ttf_categoria.value == "":
            is_valido = False
            self.ttf_categoria.error_text = "Informe a categoria."
        return is_valido

    def registrar(self, e):
        pass
        # self._metodo_salvar()
        # dataCategoria = DataCategoria(
        #     self.ttf_categoria.value,
        #     self.ttf_descricao.value
        # )
        # self._db.insert_data_categoria(dataCategoria)
        # self._page.go("/categoria_data_reload")


if __name__ == "__main__":
    ...
