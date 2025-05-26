import flet as ft


class App:

    def __init__(self, page: ft.Page):
        self.page = page
        page.dark_theme = ft.theme.Theme(color_scheme_seed="orange")
        # self.page.theme_mode = "#F96400"
        # self.page.theme = ft.Theme(
        #     # color_scheme=ft.Colors.ORANGE,
        #     primary_color=ft.Colors.ORANGE,
        # )
        # self.page.theme = ft.Theme(primary_color=ft.Colors.ORANGE)
        # Código para FLET 0.22.1
        # self.page.window_width = 340
        # self.page.window_height = 610
        # Código para FLET 0.23.2
        self.page.window.width = 340
        self.page.window.height = 610
        # Conectar um manipulador de eventos ao page.on_route_change
        ttf_teste = ft.TextField(
            value="Teste",
            prefix_icon=ft.Icons.EMAIL,
            # icon_color=ft.Colors.BLUE,
            # color="#F96400",
            prefix=ft.Icon(ft.Icons.EMAIL, color=ft.Colors.ORANGE),
            # prefix_icon=ft.Icon(name=ft.Icons.SEARCH, color=ft.Colors.ORANGE, size=30),
            # prefix_style=ft.Colors.ORANGE,
            label="Standard",
            # prefix_icon=ft.Icons.SEARCH,  # Definindo o ícone sem a cor
            # border_color=ft.Colors.BLUE,  # Cor da borda para testar
            # prefix_style=ft.TextStyle(color=ft.Colors.BLUE),
        )

        self.page.add(
            ttf_teste
            # ft.Container(
            #     # width=200,
            #     # height=200,
            #     # border=ft.border.all(1, ft.Colors.BLACK),
            #     content=ttf_teste,
            #     # theme=ft.Theme(color_scheme=ft.Colorscheme(primary=ft.Colors.YELLOW)),
            # )
        )

        # tb1 = ft.TextField(label="Standard")
        # tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
        # tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
        # tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
        # tb5 = ft.TextField(label="With an icon", icon=ft.Icons.EMOJI_EMOTIONS)
        # b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
        # page.add(tb1, tb2, tb3, tb4, tb5, b, t)


def main(page: ft.Page):
    App(page)


if __name__ == "__main__":
    ft.app(target=main)
