import flet as ft


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.ALWAYS
    page.auto_scroll = False

    lv = ft.ListView(
        horizontal=False,
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
                                leading=ft.Icon(ft.icons.SETTINGS),
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

    page.add(
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Ir para item 50", on_click=lambda _: lv.scroll_to(key="50")
                ),
                ft.ElevatedButton(
                    text="Ir para item 80", on_click=lambda _: lv.scroll_to(key="80")
                ),
                ft.ElevatedButton(
                    text="Ir para item 90", on_click=lambda _: lv.scroll_to(key="90")
                ),
            ]
        ),
        lv,
    )


ft.app(main)
