# from typing import Any, List
import flet as ft
from datetime import datetime


class dash_dias_letivos(ft.PieChart):
    DIAS_LETIVOS = 200

    def __init__(self):
        self.data_hoje = datetime.now()
        super().__init__()

        self.sections = (
            [
                ft.PieChartSection(
                    40,
                    title="40%",
                    # title_style=normal_title_style,
                    color=ft.colors.BLUE,
                    # radius=normal_radius,
                ),
                ft.PieChartSection(
                    30,
                    title="30%",
                    # title_style=normal_title_style,
                    color=ft.colors.YELLOW,
                    # radius=normal_radius,
                ),
            ],
        )
        sections_space = (0,)
        center_space_radius = (40,)
        on_chart_event = (on_chart_event,)
        expand = (True,)


if __name__ == "__main__":
    print(f"{ datetime.now() = }")
