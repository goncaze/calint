import flet as ft
from src.modelo.evento import Evento
from src.data.database_singleton import DataDBSingleton
from src.data.evento_db import EventoDB
from src.views.evento_views.evento_crud_view import EventoCRUDView


class EventoCreateView(EventoCRUDView):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__(dbs)
        self.route = "/evento_create"
        self.appbar = ft.AppBar(title=ft.Text(value="Cadastrar evento"))

        self.page: ft.Page = page
        self.eventoDB = EventoDB(dbs)

    def registrar(self, e):
        if self.validar():
            evento = Evento(
                id=0,
                evento_categoria=self.evento_selecionado(),
                evento=self.ttf_evento.value,
                descricao=self.ttf_descricao.value,
            )
            self.eventoDB.insert_evento(evento)
            self.page.go("/evento_reload")
        else:
            self.atualizar_page()

    def atualizar_page(self):
        self.page.update()


if __name__ == "__main__":
    ...
