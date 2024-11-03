import flet as ft
from src.data.database_singleton import DataDBSingleton
from src.views.ano_letivo_views.formulario_ano import FormularioAno


class AnoLetivoView(ft.View):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):

        super().__init__()
        self.route = "/ano_letivo"
        self.appbar = ft.AppBar(title=ft.Text("Reiniciar ano letivo"))        
        self.dbs :DataDBSingleton = dbs
        self.page :ft.Page = page

        self.formulario_ano :FormularioAno = FormularioAno(self.page, self.dbs)

        self.controls = [
            self.formulario_ano,
        ]    