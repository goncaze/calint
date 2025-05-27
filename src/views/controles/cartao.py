import flet as ft


class Cartao(ft.Card):

    def __init__(self):
        super().__init__()
        self.color = "#f3f3f3"  # ft.Colors.AMBER_100
        self.shadow_color = ft.Colors.GREEN
        self.surface_tint_color = ft.Colors.BLUE_400
        self.elevation = 8.0
        self.show_border_on_foreground = True
        # self.expand = True
        # self.height = 200
