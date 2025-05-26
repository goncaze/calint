import flet as ft


class VisaoLista(ft.View):
    def __init__(self):
        super().__init__()
        self.scroll = ft.ScrollMode.ALWAYS

        self.lv = ft.ListView(
            controls=[
                ft.Card(
                    key=str(i),
                    content=ft.Container(
                        width=500,
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    title=ft.Text(f"Elemento {i}"),
                                ),
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.SETTINGS),
                                    title=ft.Text("One-line selected list tile"),
                                    selected=True,
                                ),
                            ],
                            spacing=0,
                        ),
                        padding=ft.padding.symmetric(vertical=10),
                    ),
                )
                for i in range(100)
            ],
        )

        self.controls = [self.lv]


class App:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.scroll = ft.ScrollMode.ALWAYS
        self.page.auto_scroll = True
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go("/")

        self.obj_lv = VisaoLista()

        self.page.add(
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        self.obj_lv,
                    ],
                    expand=True,
                )
            )
        )

        self.obj_lv.scroll_to(key="35")

    def route_change(self, route: ft.RouteChangeEvent):
        rota: str = route.route

        if rota == "/":
            self.page.views.clear()
            # self.page.views.append(VisaoLista())
            self.page.views.append(self.obj_lv)

        self.page.update()

    def view_pop(self, e):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


def main(page: ft.Page):
    # page.scroll = ft.ScrollMode.ALWAYS
    App(page)


if __name__ == "__main__":
    ft.app(target=main)
