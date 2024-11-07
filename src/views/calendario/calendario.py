import flet as ft
from src.views.calendario.mes_card import MesCard
from src.data.database_singleton import DataDBSingleton
from src.data.data_db import DataDB


class CalendarioView(ft.View):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.page = page
        self.appbar = ft.AppBar(title=ft.Text("Calendário acadêmico"))
        self.dbs = dbs
        self.data_db = DataDB(self.dbs)
        self.todas_datas = self.data_db.select_data_todas()
        self.todas_dt_literal = self.extrair_dt_literal()
        
        self.lv_mes_horizontal = ft.ListView(
            spacing=10, 
            padding=20,         
            horizontal = True,   
        ) 
        
        for mes in range(1,13):
            mes_card = MesCard(self.page, self.dbs, 2024, mes, self.todas_datas, self.todas_dt_literal)
            # print(f"{mes_card.width = }")
            self.lv_mes_horizontal.controls.append( 
                ft.Container(
                    content=ft.Column(
                        controls=[
                            mes_card,
                            ft.Container(
                                content=mes_card.coluna_de_eventos,
                                bgcolor="#F7F7F7", 
                                expand=True, 
                                # content=ft.Text(value="Legendas"),  
                                width=mes_card.width,
                                margin=0,      
                                padding=ft.padding.all(20)                      
                            ),                                 
                        ]
                    )
                )                
            ) 


        self.controls.append(    
            ft.SafeArea(content = self.lv_mes_horizontal, expand=True)
        )

    def extrair_dt_literal(self)->list[str]:
        lista_data: list[str] = []
        [lista_data.append(data.data) for data in self.todas_datas]
        return lista_data
            