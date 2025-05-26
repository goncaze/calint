import flet as ft


class DropDownEvento(ft.Container):

    def __init__(self, dpd_evento: ft.Dropdown, dpd_evento_delete):

        super().__init__()
        self.dpd_evento = dpd_evento
        self.dpd_evento_delete = dpd_evento_delete
        self.disabled = False

        self.linha = ft.Row(
            controls=[
                self.dpd_evento,
                ft.IconButton(icon=ft.Icons.DELETE, on_click=self.deletar_a_si_mesmo),
            ]
        )
        self.content = self.linha

    def deletar_a_si_mesmo(self, e):
        self.dpd_evento_delete(self)
