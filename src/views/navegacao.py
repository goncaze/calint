import flet as ft


class Navegador:

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self._appBar: ft.AppBar = ft.AppBar(title="CALINT ", bgcolor="#aa3A0786")
        self.page.theme = ft.Theme(
            navigation_drawer_theme=ft.NavigationDrawerTheme(
                label_text_style={
                    # Estilo para o estado padrão (não selecionado)
                    ft.ControlState.DEFAULT: ft.TextStyle(
                        color=ft.Colors.WHITE, size=16, weight=ft.FontWeight.NORMAL
                    ),
                    # # Estilo para o estado selecionado (opcional)
                    # ft.ControlState.SELECTED: ft.TextStyle(
                    #     color=ft.Colors.BLUE_700, size=18, weight=ft.FontWeight.BOLD
                    # ),
                    # # Estilo para o estado de foco (opcional)
                    # ft.ControlState.FOCUSED: ft.TextStyle(
                    #     color=ft.Colors.GREEN_700,
                    #     decoration=ft.TextDecoration.UNDERLINE,
                    # ),
                },
                # Outras propriedades do tema do drawer, se necessário
                # indicator_color=ft.colors.PURPLE_200,
                # bgcolor=ft.colors.BLUE_GREY_900
            )
        )

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
            bgcolor=ft.Colors.GREEN_900,
            indicator_color=None,
            selected_index=-1,
            controls=[
                ft.Container(height=52),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.EVENT_NOTE_OUTLINED, color=ft.Colors.WHITE),
                    label="Calendário",
                    selected_icon=ft.Icons.MAIL,
                ),
                # ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    label="Datas",
                    icon=ft.Icon(
                        ft.Icons.CALENDAR_TODAY_OUTLINED, color=ft.Colors.WHITE
                    ),
                    selected_icon=ft.Icon(ft.Icons.CALENDAR_MONTH_OUTLINED),
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.EVENT_OUTLINED, color=ft.Colors.WHITE),
                    label="Eventos",
                    selected_icon=ft.Icons.EVENT,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.EVENT_NOTE_OUTLINED, color=ft.Colors.WHITE),
                    label="Categoria Eventos",
                    selected_icon=ft.Icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.EVENT_NOTE_OUTLINED, color=ft.Colors.WHITE),
                    label="Ano letivo",
                    selected_icon=ft.Icons.MAIL,
                ),
            ],
            on_change=self.page_go,
        )

        return drawer

    def page_go(self, e):

        match e.control.selected_index:
            case 0:
                self.page.go("/calendario")
            case 1:
                self.page.go("/data_add_evento")
            case 2:
                self.page.go("/eventos")
            case 3:
                self.page.go("/categoria_evento")
            case 4:
                self.page.go("/ano_letivo")

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
