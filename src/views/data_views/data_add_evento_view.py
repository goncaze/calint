import flet as ft
from src.modelo.data import Data
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton
from src.modelo.data_categoria import DataCategoria
from src.data.data_categoria_db import DataCategoriaDB
from src.data.evento_db import EventoDB
from src.modelo.evento import Evento
from src.views.data_views.dropdown_evento import DropDownEvento


class DataAddEventoView(ft.View):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):

        super().__init__()
        self.data: Data = Data()
        self.data_db = DataDB(dbs)
        self.eventoDB = EventoDB(dbs)
        self.page = page
        self.appbar = ft.AppBar(title=ft.Text(value="Data e seus eventos"))

        self.ttf_data = ft.TextField(
            label="Data",
            hint_text="Data",
            expand=True,
            read_only=True,
            # disabled=True,            
        )
        
        self.dtpkr_data = ft.DatePicker(on_change = self.change_date)

        self.icb_data = ft.IconButton(      
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_data),
        )

        # self.dpd_eventos = DropDownEvento(
        #     ft.Dropdown(
        #         hint_text="Selecione evento",
        #         on_change=self.incluir_novo_dpd_evento,
        #         options=self.listar_opcoes_eventos(),
        #     ),
        #     self.delete_dpd_evento,
        # )

        self.coluna_eventos = ft.Column()

        self.coluna_de_eventos_titulo = ft.Container(
            content = ft.Column(                
                controls=[
                    ft.Text(
                        spans=[ft.TextSpan(text="Eventos", style=ft.TextStyle(size=20))],
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLUE,
                    ),
                    self.coluna_eventos,
                ],                
            ),
            margin=10,
        )


        self.btn_atualizar_eventos_data = ft.ElevatedButton(
            text="Salvar", 
            on_click=self.atualizar_eventos_data, 
            visible=True,
            icon=ft.icons.SAVE_SHARP,
        )

        self.btn_cancelar = ft.ElevatedButton(text="Cancelar", on_click=self.cancelar)

        self.formulario_anotar_data = ft.Column(
            controls=[
                ft.Row(controls=[self.ttf_data]),
                # self.dpd_categoria_data,
                self.coluna_de_eventos_titulo,
                ft.Container(margin=ft.margin.all(5)),
                ft.Row(
                    controls=[
                        self.btn_cancelar,
                        # self.btn_ir_a_eventos,
                        self.btn_atualizar_eventos_data,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        )

        self.mensagem_dlg = ft.Text()

        self.dlg_apos_atualizar = ft.AlertDialog(
            modal=True,
            title=ft.Text("Aviso"),
            content=self.mensagem_dlg,
            actions=[
                ft.TextButton("Ok", on_click=self.handle_close_dlg),
                # ft.TextButton("No", on_click=self.handle_close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.add(
                ft.Text("Modal dialog dismissed"),
            ),
        )


        self.controls = [
            ft.SafeArea(
                content = ft.Column(                    
                    # controls=[self.formulario_anotar_data],
                    controls=[
                        ft.Row(controls=[self.ttf_data, self.icb_data]),
                        self.coluna_de_eventos_titulo,
                        ft.Row(
                            controls=[self.btn_atualizar_eventos_data,],
                            alignment=ft.MainAxisAlignment.END,
                        )
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    expand=True,
                )
            )
        ]

        # self.buscar_dados_data()

    def handle_close_dlg(self, e):
        self.page.close(self.dlg_apos_atualizar)

    def limpar_geral(self):
        self.ttf_data.value = ""
        self.limpar_coluna_eventos()

    def change_date(self, e: ft.ControlEvent):
        # print("\n\n\t\t def change_date(self, e: ft.ControlEvent): \n\n")
        self.ttf_data.value = self.dtpkr_data.value.strftime('%d-%m-%Y')
        self.data = Data(data=self.dtpkr_data.value.strftime('%Y-%m-%d'))
        # print(f"{self.data = }\n\n")
        # self.cln_listagem.controls=[self.listar_eventos()]
        self.limpar_coluna_eventos()
        self.buscar_dados_data()
        self.ttf_data.update()
        # self.cln_listagem.update()


    def cancelar(self, e: ft.ControlEvent):
        self.page.go(route="/data_reload")



    def listar_opcoes_eventos(self) -> list:
        lista = []
        for evento in self.eventoDB.select_evento_todos():
            lista.append(
                ft.dropdown.Option(
                    data=evento,
                    text=evento.evento,
                )
            )
        return lista



    def eventos_selecionados(self) -> list[Evento]:
        lista_eventos: list[Evento] = []

        for obj_dropdown_envento in self.coluna_eventos.controls:
            for opcao in obj_dropdown_envento.dpd_evento.options:
                if opcao.text == obj_dropdown_envento.dpd_evento.value:
                    lista_eventos.append(opcao.data)

        return lista_eventos
    


    def novo_dpd_evento(self) -> DropDownEvento:
        novo_dpd_evento = DropDownEvento(
            ft.Dropdown(
                hint_text="Selecione evento",
                on_change=self.incluir_novo_dpd_evento,
                options=self.listar_opcoes_eventos(),
                expand=True,
            ),
            self.delete_dpd_evento,
        )
        return novo_dpd_evento



    def incluir_novo_dpd_evento(self, e):
        self.coluna_eventos.controls.append(self.novo_dpd_evento())
        self.page.update()

    def restaurar_dpd_evento(self, dpd_evento: DropDownEvento):
        self.coluna_eventos.controls.append(dpd_evento)
        self.page.update()

    def delete_dpd_evento(self, dpd_evento: DropDownEvento):
        self.coluna_eventos.controls.remove(dpd_evento)
        self.coluna_eventos.update()

    def limpar_coluna_eventos(self):
        self.coluna_eventos.controls.clear()

    def atualizar_eventos_data(self, e):
        print(f"\n\ndef atualizar_eventos_data(self, e):\n")
        if self.data.data != "":
            print(f"\n\n\tTRUE if self.data:\n")
            # self.data.data_categoria = self.categoria_data_selecionada()
            self.data.eventos = self.eventos_selecionados()
            self.data_db.update_data_evento(self.data)
            self.data = Data()
            self.limpar_geral()
            self.mensagem_dlg.value = "Os dados foram atualizados!"
            self.page.open(self.dlg_apos_atualizar)            
        else:
            self.mensagem_dlg.value = "Primeiro, selecione uma data!"
            self.page.open(self.dlg_apos_atualizar)

    def atualizar_page(self):
        pass

    def buscar_dados_data(self):
        self.data = self.data_db.select_uma_data(self.data)
        if self.data:
            for evento in self.data.eventos:
                # =========
                dpd_evento = ft.Dropdown(
                    hint_text="Selecione evento",
                    on_change=self.incluir_novo_dpd_evento,
                    options=self.listar_opcoes_eventos(),
                    expand=True,
                )

                dpd_evento.value = evento.evento

                self.restaurar_dpd_evento(
                    DropDownEvento(
                        dpd_evento,
                        self.delete_dpd_evento,
                    )
                )
            # self.ver_categoria_e_eventos()

        dpd_evento = ft.Dropdown(
            hint_text="Selecione evento",
            on_change=self.incluir_novo_dpd_evento,
            options=self.listar_opcoes_eventos(),
            expand=True,
        )

        self.restaurar_dpd_evento(
            DropDownEvento(
                dpd_evento,
                self.delete_dpd_evento,
            )
        )
