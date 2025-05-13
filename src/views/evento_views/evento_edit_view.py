import flet as ft
from src.modelo.evento import Evento
from src.data.evento_db import EventoDB
from src.data.database_singleton import DataDBSingleton
from src.views.evento_views.evento_crud_view import EventoCRUDView


class EventoEditView(EventoCRUDView):

    def __init__(self, id: int, page: ft.Page, dbs: DataDBSingleton):
        super().__init__(dbs)
        self.route = "/evento_edit"
        self.appbar = ft.AppBar(title=ft.Text(value="Editar evento"))

        self.eventoDB = EventoDB(dbs)
        self.evento: Evento = self.eventoDB.select_evento(id)
        self.page: ft.Page = page

        self.ttf_evento.value = self.evento.evento
        self.ttf_descricao.value = self.evento.descricao
        self.dpd_categoria_evento.value = self.evento.evento_categoria.categoria

    def registrar(self, e):
        if self.validar():
            self.eventoDB.update_evento(
                self.evento.id,
                self.evento_selecionado(),
                self.ttf_evento.value,
                self.ttf_descricao.value,
            )
            self.page.go("/evento_reload")
        else:
            self.atualizar_page()

    def atualizar_page(self):
        self.page.update()


if __name__ == "__main__":
    ...
