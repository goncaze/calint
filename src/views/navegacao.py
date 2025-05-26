import flet as ft


class Navegador:

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self._appBar: ft.AppBar = ft.AppBar(title="CALINT ", bgcolor="#aa3A0786")

    @property
    def appBar(self) -> ft.AppBar:
        return self._appBar

    @appBar.setter
    def appBar(self, titulo, bgcolor) -> ft.AppBar:
        self._appBar = ft.AppBar(title=ft.Text(titulo), bgcolor=bgcolor)

        return self._appBar

    def drawer(self) -> ft.NavigationDrawer:
        drawer = ft.NavigationDrawer(
            open=False,
            controls=[
                # ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Datas",
                    icon=ft.Icons.CALENDAR_TODAY_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.CALENDAR_MONTH_OUTLINED),
                ),
                ft.Divider(thickness=2),
                # ft.NavigationDrawerDestination(
                #     icon_content=ft.Icon(ft.Icons.CALENDAR_TODAY_OUTLINED),
                #     label="Categoria Datas",
                #     selected_icon=ft.Icons.MAIL,
                # ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.EVENT_OUTLINED,
                    label="Eventos",
                    selected_icon=ft.Icons.EVENT,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.EVENT_NOTE_OUTLINED,
                    label="Categoria Eventos",
                    selected_icon=ft.Icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.EVENT_NOTE_OUTLINED,
                    label="Ano letivo",
                    selected_icon=ft.Icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.EVENT_NOTE_OUTLINED,
                    label="Calendário",
                    selected_icon=ft.Icons.MAIL,
                ),
            ],
            on_change=self.page_go,
        )

        return drawer

    def page_go(self, e):

        match e.control.selected_index:
            case 0:
                # self.page.go("/datas")
                self.page.go("/data_add_evento")
            # case 1:
            #     self.page.go("/categoria_data")
            case 1:
                self.page.go("/eventos")
            case 2:
                self.page.go("/categoria_evento")
            case 3:
                self.page.go("/ano_letivo")
            case 4:
                self.page.go("/calendario")

    def aux_page_go(self, url: str):

        match url:
            case "/datas":
                self.page.go("/datas")
            case "/categoria_data":
                self.page.go("/categoria_data")
            case "/eventos":
                self.page.go("/eventos")
            case "/categoria_evento":
                self.page.go("/categoria_evento")
