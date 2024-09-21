import flet as ft
from datetime import datetime
from datetime import timedelta
from src.data.database_singleton import DataDBSingleton
from src.modelo.data import Data
from src.modelo.data_categoria import DataCategoria
from src.modelo.evento import Evento
from src.modelo.evento_categoria import EventoCategoria
from src.data.data_db import DataDB
from src.data.database_singleton import DataDBSingleton
from src.data.data_categoria_db import DataCategoriaDB
from src.data.evento_db import EventoDB
from src.data.evento_categoria_db import EventoCategoriaDB


class FormularioAno(ft.Card):
    def __init__(self, page:ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.page :ft.Page = page
        self.dataDB :DataDB = DataDB(dbs)
        self.dataCategoriaDB :DataCategoriaDB = DataCategoriaDB(dbs)
        self.eventoDB :EventoDB = EventoDB(dbs)
        self.eventoCategoriaDB :EventoCategoriaDB = EventoCategoriaDB(dbs)

        self.data_categoria_Letivo :DataCategoria = DataCategoria("Letivo")
        self.data_categoria_ferias :DataCategoria = DataCategoria("Férias")

        self.ttf_inicio_letivo = ft.TextField(label="Início ano letivo", value="05/02/2024", expand=True)
        self.ttf_fim_letivo = ft.TextField(label="Fim ano letivo", value="10/12/2024", expand=True)
        self.ttf_inicio_ferias_1 = ft.TextField(label="Início férias coletivas 1", value="08/07/2024", expand=True)    
        self.ttf_fim_ferias_1 = ft.TextField(label="Fim férias coletivas 1", value="22/07/2024", expand=True)
        self.ttf_inicio_ferias_2 = ft.TextField(label="Início férias coletivas 2", value="01/01/2025", expand=True)    
        self.ttf_fim_ferias_2 = ft.TextField(label="Fim férias coletivas 2", value="31/01/2025", expand=True)

        self.dtpkr_i_letivo = ft.DatePicker(on_change = self.change_date_i_letivo,)
        self.dtpkr_f_letivo = ft.DatePicker(on_change = self.change_date_f_letivo,)
        self.dtpkr_i_ferias_1 = ft.DatePicker(on_change = self.change_date_i_ferias_1,)
        self.dtpkr_f_ferias_1 = ft.DatePicker(on_change = self.change_date_f_ferias_1,)
        self.dtpkr_i_ferias_2 = ft.DatePicker(on_change = self.change_date_i_ferias_2,)
        self.dtpkr_f_ferias_2 = ft.DatePicker(on_change = self.change_date_f_ferias_2,)

        self.icb_letivo_1 = ft.IconButton(      
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_i_letivo),
        )

        self.icb_letivo_2 = ft.IconButton(      
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_f_letivo),
        )        

        self.icb_i_ferias_1 = ft.IconButton(      
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_i_ferias_1),
        )                

        self.icb_f_ferias_1 = ft.IconButton(      
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_f_ferias_1),
        )                        

        self.icb_i_ferias_2 = ft.IconButton(      
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_i_ferias_2),
        )                

        self.icb_f_ferias_2 = ft.IconButton(      
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.dtpkr_f_ferias_2),
        )        


        self.ttb_salvar = ft.TextButton(text="Salvar", on_click=self.salvar)

        self.linha_ttb = ft.Row(
            controls=[
                self.ttb_salvar,
            ],
            alignment=ft.MainAxisAlignment.END
        )

        self.content = ft.Column(
            controls = [                
                ft.Row(
                    controls=[
                        self.ttf_inicio_letivo,
                        self.icb_letivo_1,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_fim_letivo,
                        self.icb_letivo_2,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_inicio_ferias_1,
                        self.icb_i_ferias_1,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_fim_ferias_1,
                        self.icb_f_ferias_1,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_inicio_ferias_2,
                        self.icb_i_ferias_2,
                    ],
                ),
                ft.Row(
                    controls=[
                        self.ttf_fim_ferias_2,
                        self.icb_f_ferias_2,
                    ],
                ),
                self.linha_ttb,
            ]
        )


    def change_date_i_letivo(self, e: ft.ControlEvent):
        self.ttf_inicio_letivo.value = self.dtpkr_i_letivo.value.strftime('%d/%m/%Y')
        self.ttf_inicio_letivo.update()

    def change_date_f_letivo(self, e: ft.ControlEvent):
        self.ttf_fim_letivo.value = self.dtpkr_f_letivo.value.strftime('%d/%m/%Y')
        self.ttf_fim_letivo.update()

    def change_date_i_ferias_1(self, e: ft.ControlEvent):
        self.ttf_inicio_ferias_1.value = self.dtpkr_i_ferias_1.value.strftime('%d/%m/%Y')
        self.ttf_inicio_ferias_1.update()

    def change_date_f_ferias_1(self, e: ft.ControlEvent):
        self.ttf_fim_ferias_1.value = self.dtpkr_f_ferias_1.value.strftime('%d/%m/%Y')
        self.ttf_fim_ferias_1.update()
        
    def change_date_i_ferias_2(self, e: ft.ControlEvent):
        self.ttf_inicio_ferias_2.value = self.dtpkr_i_ferias_2.value.strftime('%d/%m/%Y')
        self.ttf_inicio_ferias_2.update()

    def change_date_f_ferias_2(self, e: ft.ControlEvent):
        self.ttf_fim_ferias_2.value = self.dtpkr_f_ferias_2.value.strftime('%d/%m/%Y')        
        self.ttf_fim_ferias_2.update()


    # def limpar_formulario(self):
    #     self.ttf_titulo.value = ""
    #     self.ttf_genero.value = ""
    #     self.ttf_lancamento.value = ""
    #     self.update()


    def validar(self) -> bool:
        is_valido: bool = True
        if self.ttf_inicio_letivo.value == "":
            is_valido = False
            self.ttf_inicio_letivo.error_text = "Data do início do ano letivo"

        if self.ttf_fim_letivo.value == "":
            is_valido = False
            self.ttf_fim_letivo.error_text = "Data do fim do ano letivo"
        
        if self.ttf_inicio_ferias_1.value == "":
            is_valido = False
            self.ttf_inicio_ferias_1.error_text = "Data de início das férias 1"

        if self.ttf_inicio_ferias_2.value == "":
            is_valido = False
            self.ttf_inicio_ferias_2.error_text = "Data de início das férias 2"
        
        if self.ttf_fim_ferias_1.value == "":
            is_valido = False
            self.ttf_fim_ferias_1.error_text = "Data de fim das férias 1"

        if self.ttf_fim_ferias_2.value == "":
            is_valido = False
            self.ttf_fim_ferias_2.error_text = "Data de fim das férias 2"

        return is_valido



    def salvar(self, e):
        if self.validar():        
            data_i_letivo = Data(data=self.ttf_inicio_letivo.value)
            data_f_letivo = Data(data=self.ttf_fim_letivo.value)
            data_i_ferias_1 = Data(data=self.ttf_inicio_ferias_1.value)
            data_f_ferias_1 = Data(data=self.ttf_fim_ferias_1.value)
            data_i_ferias_2 = Data(data=self.ttf_inicio_ferias_2.value)
            data_f_ferias_2 = Data(data=self.ttf_fim_ferias_2.value)

            # Inserir categorias de datas no banco de dados
            data_categoria_Letivo :DataCategoria = DataCategoria("Letivo")
            data_categoria_ferias :DataCategoria = DataCategoria("Férias")

            self.dataCategoriaDB.insert_data_categoria(data_categoria_Letivo)
            data_categoria_Letivo = self.dataCategoriaDB.select_data_categoria(1)
            self.dataCategoriaDB.insert_data_categoria(data_categoria_ferias)
            data_categoria_ferias = self.dataCategoriaDB.select_data_categoria(2)

            # Inserir categoria de evento no banco de dados
            evento_categoria :EventoCategoria = EventoCategoria("Longo período")
            self.eventoCategoriaDB.insert_evento_categoria(evento_categoria)
            evento_categoria = self.eventoCategoriaDB.select_evento_categoria(1)

            # Inserir eventos no banco de dados
            evento_i_letivo :Evento = Evento(evento_categoria, "Início ano letivo")
            evento_f_letivo :Evento = Evento(evento_categoria, "Fim ano letivo")
            evento_i_ferias_1 :Evento = Evento(evento_categoria, "Início férias 1")
            evento_f_ferias_1 :Evento = Evento(evento_categoria, "Fim férias 1")
            evento_i_ferias_2 :Evento = Evento(evento_categoria, "Início férias 2")
            evento_f_ferias_2 :Evento = Evento(evento_categoria, "Fim férias 2")

            self.eventoDB.insert_evento(evento_i_letivo)
            evento_i_letivo = self.eventoDB.select_evento(1)
            self.eventoDB.insert_evento(evento_f_letivo)
            evento_f_letivo = self.eventoDB.select_evento(2)
            self.eventoDB.insert_evento(evento_i_ferias_1)
            evento_i_ferias_1 = self.eventoDB.select_evento(3)
            self.eventoDB.insert_evento(evento_f_ferias_1)
            evento_f_ferias_1 = self.eventoDB.select_evento(4)
            self.eventoDB.insert_evento(evento_i_ferias_2)
            evento_i_ferias_2 = self.eventoDB.select_evento(5)
            self.eventoDB.insert_evento(evento_f_ferias_2)
            evento_f_ferias_2 = self.eventoDB.select_evento(6)

            # Preparar datas
            data_i_letivo.data_categoria = data_categoria_Letivo
            data_i_letivo.eventos = [evento_i_letivo]

            data_f_letivo.data_categoria = data_categoria_Letivo
            data_f_letivo.eventos = [evento_f_letivo]

            data_i_ferias_1.data_categoria = data_categoria_ferias
            data_i_ferias_1.eventos = [evento_i_ferias_1]

            data_f_ferias_1.data_categoria = data_categoria_ferias
            data_f_ferias_1.eventos = [evento_f_ferias_1]

            data_i_ferias_2.data_categoria = data_categoria_ferias
            data_i_ferias_2.eventos = [evento_i_ferias_2]

            data_f_ferias_2.data_categoria = data_categoria_ferias
            data_f_ferias_2.eventos = [evento_f_ferias_2]


            # Inserir datas
            self.dataDB.insert_data(data_i_letivo)
            self.dataDB.insert_data(data_f_letivo)
            self.dataDB.insert_data(data_i_ferias_1)
            self.dataDB.insert_data(data_f_ferias_1)
            self.dataDB.insert_data(data_i_ferias_2)
            self.dataDB.insert_data(data_f_ferias_2)

            lista_dias_ferias_1 = self.preencher_db_ferias(
                data_i_ferias_1, 
                data_f_ferias_1, 
                data_categoria_ferias
            )
            
            self.preencher_db_dias_letivos(
                data_i_letivo, 
                data_categoria_Letivo, 
                lista_dias_ferias_1
            )

            self.page.go("/")                        
        else:
            self.update()

       
    def preencher_db_dias_letivos(
            self, 
            data_i_letivo :Data, 
            data_categoria_Letivo :DataCategoria,
            lista_dias_ferias_1 :list[str]
        ):
        dia = 0
        dias_letivos = 1
        while dias_letivos <= 200:
            dia += 1

            data = datetime.strftime(
                datetime.strptime(data_i_letivo.data,"%d/%m/%Y") + 
                timedelta(dia), "%d/%m/%Y"
            )

            data_dia_da_semana = datetime.date(datetime.strptime(data,"%d/%m/%Y"))

            if data_dia_da_semana.isoweekday() == 6 or data_dia_da_semana.isoweekday() == 7:
                print(f"Fim de semana = {data_dia_da_semana}")

            elif data not in lista_dias_ferias_1:
                novo_dia_letivo = Data(data=data, data_categoria=data_categoria_Letivo)
                self.dataDB.insert_data(novo_dia_letivo)

                print(f"{data = }")
                dias_letivos += 1
                
        

    def preencher_db_ferias(
            self, 
            data_i_ferias_1: Data, 
            data_f_ferias_1: Data, 
            data_categoria_ferias: DataCategoria
        ) -> list[str]:

        lista_dias_ferias_1 :list[str] = [data_i_ferias_1.data]
        dia = 0

        while True:
            dia += 1

            data = datetime.strftime(
                datetime.strptime(data_i_ferias_1.data,"%d/%m/%Y") + 
                timedelta(dia), "%d/%m/%Y"
            )            
            
            lista_dias_ferias_1.append(data)

            print(f"{data = }")

            if data == data_f_ferias_1.data:
                break
            else:
                # inserir dia de férias
                nova_data = Data(data=data, data_categoria=data_categoria_ferias)
                self.dataDB.insert_data(nova_data)
        
        return lista_dias_ferias_1