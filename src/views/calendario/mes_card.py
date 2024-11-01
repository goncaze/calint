import flet as ft
import calendar
from src.views.calendario.cartao import Cartao



class MesCard(Cartao):

    def __init__(self, page: ft.Page, ano: int = 2024, mes: int = 10): 
        super().__init__()
        self.page = page
        self.page.expand = False
        self.width = 350

        self.ano = ano
        self.mes = mes
        self.titulo_mes = f"{calendar.month_name[mes].capitalize()} de {ano}"

        self.obj_calendar_d0 = calendar.Calendar(firstweekday=6)
        # obj_calendar_d1 = calendar.Calendar(firstweekday=1)
        calendar.setfirstweekday(calendar.SUNDAY)


        ###
        # As listas de containers representam as colunas dos dias da semana.
        # Cada unidade de container contém os dias da semana e o nome do dia.
        #
        self.lista_container_00 = [
            ft.Container(
                content=ft.Text(value="DOM", color="#46a151"), 
                alignment=ft.alignment.center,
                bgcolor = '#f3f3f3', #ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_01 = [
            ft.Container(
                content=ft.Text(value="SEG", color="#46a151"), 
                alignment=ft.alignment.center,
                bgcolor='#f3f3f3', #ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_02 = [
            ft.Container(
                content=ft.Text(value="TER", color="#46a151"), 
                alignment=ft.alignment.center,
                bgcolor='#f3f3f3', #ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_03 = [
            ft.Container(
                content=ft.Text(value="QUA", color="#46a151"), 
                alignment=ft.alignment.center,
                bgcolor='#f3f3f3', #ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_04 = [
            ft.Container(
                content=ft.Text(value="QUI", color="#46a151"), 
                alignment=ft.alignment.center,
                bgcolor='#f3f3f3', #ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_05 = [
            ft.Container(
                content=ft.Text(value="SEX", color="#46a151"), 
                alignment=ft.alignment.center,
                bgcolor='#f3f3f3', #ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]
        self.lista_container_06 = [
            ft.Container(
                content=ft.Text(value="SAB", color="#46a151"), 
                alignment=ft.alignment.center,
                bgcolor='#f3f3f3', #ft.colors.BLUE_100,
                border=ft.border.all(width=1, color=ft.colors.GREY_300),
            )
        ]

        ###
        # Essa lista dos containers serve para rodar um loop que irá gerar  
        # os containers contendo os dias do mês.
        #
        self.listas_containers: list[list] = [
            self.lista_container_00,
            self.lista_container_01,
            self.lista_container_02,
            self.lista_container_03,
            self.lista_container_04,
            self.lista_container_05,
            self.lista_container_06
        ]



        self.preencher_dias(ano=self.ano, mes=self.mes)


        ###
        # As colunas para cada dia da semana contendo os dias
        # do mês que estão nas listas de conteiners.
        #
        self.coluna_00 = ft.Column(self.lista_container_00, expand=True)
        self.coluna_01 = ft.Column(self.lista_container_01, expand=True)
        self.coluna_02 = ft.Column(self.lista_container_02, expand=True)
        self.coluna_03 = ft.Column(self.lista_container_03, expand=True)
        self.coluna_04 = ft.Column(self.lista_container_04, expand=True)
        self.coluna_05 = ft.Column(self.lista_container_05, expand=True)
        self.coluna_06 = ft.Column(self.lista_container_06, expand=True)


        ###
        # Uma Row para agrupar as colnas antes de incluir no Card.
        #
        self.linha: ft.Row = ft.Row(
            controls=[
                self.coluna_00,
                self.coluna_01,
                self.coluna_02,
                self.coluna_03,
                self.coluna_04,
                self.coluna_05,
                self.coluna_06
            ]
        )

        self.content = ft.Container(
            margin = 10,
            content = ft.Column(
                controls=[
                    ft.Row(                        
                        controls=[
                            ft.Container(
                                content = ft.Text(value=self.titulo_mes),
                                alignment=ft.alignment.center,
                                expand=True,
                            ),
                        ],
                    ),
                    ft.Row( 
                        vertical_alignment=ft.CrossAxisAlignment.START,                                         
                        controls=[                    
                            self.coluna_00,
                            self.coluna_01,
                            self.coluna_02,
                            self.coluna_03,
                            self.coluna_04,
                            self.coluna_05,
                            self.coluna_06
                        ]
                    ),   
                ]   
            )      
        )
        

    ##
    # Encapsula o dia do mês dentro de um container e o retorna como resultado.
    # Dias zero são encapsulados sem borda e valor.
    #
    def container(self, dia: int, mes: int, ano: int) -> ft.Container:
        if dia > 0:             
            container = ft.Container(                
                content=ft.Text(value=dia),
                bgcolor="#ea9999" if calendar.weekday(ano, mes, dia) in (5,6) else "",
                border=ft.border.all(width = 1, color=ft.colors.GREY_300),
                expand=True,
                alignment=ft.alignment.center,
            )
        else:
            container = ft.Container(                
                content=ft.Text(value=""),
                expand=True,
                alignment=ft.alignment.center,
            )

        return container
    
    ##
    # Para cada um dos sete dias da semana existe uma lista de containers 
    # contendo os dias da semana do mês. Por exemplo, self.lista_container_01 
    # contém todos os dias da segunda-feira de um determinado mês.
    #
    def preencher_dias(self, ano: int = 2024, mes: int = 10):
        self.i = 0

        for dia in self.obj_calendar_d0.itermonthdays(ano, mes):
            if self.i < 7:                
                self.listas_containers[self.i].append(self.container(dia, mes, ano))
                # print(f"{dia}", end="\t")
                self.i += 1                
            else:
                # print(f"\n{dia}", end="\t")
                self.i = 1
                self.listas_containers[0].append(self.container(dia, mes, ano))
  




        # self.content = ft.Text("TESTADO")

    #     self.icb_editar = ft.IconButton(
    #         icon=ft.icons.UPDATE,
    #         icon_color="blue",
    #         icon_size=25,
    #         tooltip="Update record",
    #         on_click=self.editar,
    #     )

    #     self.icb_excluir = ft.IconButton(
    #         icon=ft.icons.DELETE_FOREVER_ROUNDED,
    #         icon_color="pink600",
    #         icon_size=25,
    #         tooltip="Delete record",
    #         on_click=self.excluir,
    #     )

    #     self.linha_botoes = ft.Row(
    #         controls=[self.icb_editar, self.icb_excluir],
    #         alignment=ft.MainAxisAlignment.END,
    #     )

    #     # self.content.content.controls[1] = self.linha_botoes

    # def excluir(self, e):
    #     self.filme_db.delete_filme(self.data)
    #     self.page.go("/reload")

    # def editar(self, e):
    #     self.page.go(f"/formulario/{self.data.id}")
