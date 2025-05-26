import flet as ft

# from src.modelo.evento import Evento
from src.modelo.evento_categoria import EventoCategoria
from src.data.evento_categoria_db import EventoCategoriaDB
from src.data.database_singleton import DataDBSingleton


class EventoCRUDView(ft.View):

    def __init__(self, dbs: DataDBSingleton):
        super().__init__()
        self.bgcolor = ft.Colors.WHITE
        self.eventoCategoriaDB = EventoCategoriaDB(dbs)

        self.ttf_evento = ft.TextField(
            label="Evento",
            hint_text="Evento",
        )

        self.ttf_descricao = ft.TextField(
            label="descricao",
            hint_text="descricao",
        )

        self.dpd_categoria_evento = ft.Dropdown(
            label="Categoria",
            hint_text="Categoria do evento",
        )

        self.btn_registrar = ft.ElevatedButton(text="Salvar", on_click=self.registrar)
        # self.btn_registrar = ft.ElevatedButton(text="Salvar", on_click=...)

        self.btn_limpar_form = ft.ElevatedButton(
            text="Limpar", on_click=self.limpar_form
        )
        # self.btn_limpar_form = ft.ElevatedButton(text="Limpar", on_click=...)

        self.formulario_evento_create = ft.Column(
            controls=[
                self.ttf_evento,
                self.ttf_descricao,
                self.dpd_categoria_evento,
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
            self.formulario_evento_create,
        ]

        self.listar_categoria_evento()

    def limpar_form(self, e: ft.ControlEvent):
        self.ttf_evento.value = None
        self.ttf_descricao.value = None
        self.atualizar_page()

    def atualizar_page(self):
        pass

    def validar(self) -> bool:
        # print(f"{self.dpd_categoria_evento.value = }")
        # print(f"{self.dpd_categoria_evento.value == "" = }")

        is_valido: bool = True
        if self.ttf_evento.value == "":
            is_valido = False
            self.ttf_evento.error_text = "Informe a evento."
        if self.dpd_categoria_evento.value is None:
            is_valido = False
            self.dpd_categoria_evento.error_text = "Informe a evento."
        return is_valido

    def listar_categoria_evento(self):
        for categoriaEvento in self.eventoCategoriaDB.select_evento_categoria_todos():
            dpd = ft.dropdown.Option(
                data=categoriaEvento,
                text=categoriaEvento.categoria,
            )
            self.dpd_categoria_evento.options.append(dpd)

    def evento_selecionado(self) -> EventoCategoria:
        for opcao in self.dpd_categoria_evento.options:
            if opcao.text == self.dpd_categoria_evento.value:
                return opcao.data
        return None

    def registrar(self, e):
        pass


# if __name__ == "__main__":
#     ...
