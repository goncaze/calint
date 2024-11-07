import flet as ft
from src.modelo.data import Data
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton
from src.data.evento_db import EventoDB
from src.modelo.evento import Evento


class SelecionarDataView(ft.View):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):

        super().__init__()
        self.data: Data = None
        self.page :ft.Page = page
        self.data_db :DataDB = DataDB(dbs)        
        self.evento_db :EventoDB = EventoDB(dbs)
        self.appbar :ft.AppBar = ft.AppBar(title=ft.Text(value="Eventos por data"))

        self.ttf_data = ft.TextField(label="Data", value="", expand=True)

        self.dtpkr_data = ft.DatePicker(on_change = self.change_date)

        self.icb_data = ft.IconButton(      
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_data),
        )

        self.ttb_salvar = ft.TextButton(text="Salvar", on_click=self.salvar)

        self.linha_ttb = ft.Row(
            controls=[
                self.ttb_salvar,
            ],
            alignment=ft.MainAxisAlignment.END
        )

        self.controls = [
            ft.SafeArea(
                # content = ft.Text(value="Selecionar data!")
                content = ft.Column(
                    controls = [
                        ft.Row(
                            controls=[
                                self.ttf_data,
                                self.icb_data,
                            ],
                        ),
                        self.linha_ttb,
                    ]   
                )
            )
        ]
        print("\n\n\n\t\t\t SELECIONAR DATA AQUI \n\n\n")
        # self.update()

    def change_date(self, e: ft.ControlEvent):
        self.ttf_data.value = self.dtpkr_data.value.strftime('%d-%m-%Y')
        self.ttf_data.update()


    def validar(self) -> bool:
        is_valido: bool = True
        if self.ttf_data.value == "":
            is_valido = False
            self.ttf_data.error_text = "Selecionar Data"

        return is_valido



    def salvar(self, e):
        if self.validar():    
            ...
 