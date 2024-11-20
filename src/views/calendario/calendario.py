import flet as ft
from datetime import datetime
from src.views.calendario.mes_card import MesCard
from src.data.database_singleton import DataDBSingleton
from src.data.data_db import DataDB
import calendar


class CalendarioView(ft.View):

    def __init__(self, page: ft.Page, dbs: DataDBSingleton):
        super().__init__()
        self.page = page
        self.appbar = ft.AppBar(title=ft.Text("Calendário acadêmico"))
        self.dbs = dbs
        self.data_db = DataDB(self.dbs)
        self.todas_datas = self.data_db.select_data_todas()
        self.todas_dt_literal = self.extrair_dt_literal()
        self.hoje = datetime.now().date()

        self.lv_mes_horizontal = ft.ListView(
            spacing=10,
            padding=20,
            horizontal=True,
        )

        self.ano = self.hoje.year - 1
        for ano in range(self.hoje.year, self.hoje.year + 2):
            self.ano += 1
            for mes in range(1, 13):
                mes_card = MesCard(
                    self.page,
                    self.dbs,
                    ano,
                    mes,
                    self.todas_datas,
                    self.todas_dt_literal,
                )
                # self.aux_i_mes += 1
                # print("self.aux_i_mes")
                # print(f"{self.aux_i_mes = }")
                # print("key=str(mes + self.aux_i_mes)")
                # print(f"{mes + self.aux_i_mes = }")
                # print(f"{calendar.month_name[mes] + str(self.ano) = }")

                self.lv_mes_horizontal.controls.append(
                    ft.Container(
                        key=str(calendar.month_name[mes] + str(self.ano)), # + self.aux_i_mes),
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
                                    padding=ft.padding.all(20),
                                ),
                            ]
                        )
                    )
                )

        # for mes in range(1, 13):
        #     mes_card = MesCard(
        #         self.page, self.dbs, 2024, mes, self.todas_datas, self.todas_dt_literal
        #     )
        #     # print(f"{mes_card.width = }")
        #     self.lv_mes_horizontal.controls.append(
        #         ft.Container(
        #             content=ft.Column(
        #                 controls=[
        #                     mes_card,
        #                     ft.Container(
        #                         content=mes_card.coluna_de_eventos,
        #                         bgcolor="#F7F7F7",
        #                         expand=True,
        #                         # content=ft.Text(value="Legendas"),
        #                         width=mes_card.width,
        #                         margin=0,
        #                         padding=ft.padding.all(20),
        #                     ),
        #                 ]
        #             )
        #         )
        #     )

        self.controls.append(ft.SafeArea(content=self.lv_mes_horizontal, expand=True))
        # page.add(self.lv_mes_horizontal)
        # self.lv_mes_horizontal.scroll_to(key='março2024')

    def extrair_dt_literal(self) -> list[str]:
        lista_data: list[str] = []
        [lista_data.append(data.data) for data in self.todas_datas]
        return lista_data
