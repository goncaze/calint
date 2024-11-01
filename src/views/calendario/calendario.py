import flet as ft
from src.views.calendario.mes_card import MesCard


class CalendarioView(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
        
        self.lv_mes_horizontal = ft.ListView(
            spacing=10, 
            padding=20,         
            horizontal = True,   
        ) 
        
        for i in range(1,13):
            mes_Card = MesCard(self.page, 2024, i)
            print(f"{mes_Card.width = }")
            self.lv_mes_horizontal.controls.append( 
                ft.Container(
                    content=ft.Column(
                        controls=[
                            mes_Card,
                            ft.Container(
                                bgcolor=ft.colors.TEAL_200, 
                                expand=True, 
                                content=ft.Text(value="Legendas"),  
                                width=mes_Card.width,
                                margin=0,                            
                            ),                                 
                        ]
                    )
                )                
            ) 


        self.controls.append(    
            ft.SafeArea(content = self.lv_mes_horizontal, expand=True)
        )