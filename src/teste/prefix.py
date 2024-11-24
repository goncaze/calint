import flet as ft


class App:

    def __init__(self, page: ft.Page):
        self.page = page
        page.dark_theme = ft.theme.Theme(color_scheme_seed="orange")
        # self.page.theme_mode = "#F96400"
        # self.page.theme = ft.Theme(
        #     # color_scheme=ft.colors.ORANGE,
        #     primary_color=ft.colors.ORANGE,
        # )
        # self.page.theme = ft.Theme(primary_color=ft.colors.ORANGE)
        # Código para FLET 0.22.1
        # self.page.window_width = 340
        # self.page.window_height = 610
        # Código para FLET 0.23.2
        self.page.window.width = 340
        self.page.window.height = 610
        # Conectar um manipulador de eventos ao page.on_route_change
        ttf_teste = ft.TextField(
            value="Teste",
            prefix_icon=ft.icons.EMAIL,
            # icon_color=ft.colors.BLUE,
            # color="#F96400",
            prefix=ft.Icon(ft.icons.EMAIL, color=ft.colors.ORANGE),
            # prefix_icon=ft.Icon(name=ft.icons.SEARCH, color=ft.colors.ORANGE, size=30),
            # prefix_style=ft.colors.ORANGE,
            label="Standard",
            # prefix_icon=ft.icons.SEARCH,  # Definindo o ícone sem a cor
            # border_color=ft.colors.BLUE,  # Cor da borda para testar
            # prefix_style=ft.TextStyle(color=ft.colors.BLUE),
        )

        self.page.add(
            ttf_teste
            # ft.Container(
            #     # width=200,
            #     # height=200,
            #     # border=ft.border.all(1, ft.colors.BLACK),
            #     content=ttf_teste,
            #     # theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.YELLOW)),
            # )
        )

        # tb1 = ft.TextField(label="Standard")
        # tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
        # tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
        # tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
        # tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)
        # b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
        # page.add(tb1, tb2, tb3, tb4, tb5, b, t)


def main(page: ft.Page):
    App(page)


if __name__ == "__main__":
    ft.app(target=main)
