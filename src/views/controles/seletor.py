import flet as ft


class SeletorCor(ft.AlertDialog):
    def __init__(self):
        super().__init__()

        self.title = ft.Text(value="Seletor de cores")
        self.modal = True

        self.cor_selecionada: str = None
        self.lst_cores = [
            "white",
            "grey",
            "black",
            "brown",
            "yellow",
            "amber",
            "cyan",
            "blue",
            "indigo",
            "red",
            "#FF0000",
            "orange",
            "deeporange",
            "pink",
            "green",
            "teal",
            "purple",
            "deeppurple",
        ]

        self.containers_colors: list[ft.Container] = []
        for cor in self.lst_cores:
            self.containers_colors.append(
                ft.Container(
                    width=30,
                    height=30,
                    bgcolor=cor,
                    on_click=self.selecionar,
                    border_radius=30,
                )
            )

        self.content = ft.Row(
            wrap=True,
            controls=[*self.containers_colors],
        )

    def selecionar(self, e: ft.ControlEvent):
        for ctn in self.containers_colors:
            ctn.border = None

        self.update()
        self.data = e.control.bgcolor

        e.control.border = ft.border.all(
            width=5,
            color="white",
        )
        e.control.update()
