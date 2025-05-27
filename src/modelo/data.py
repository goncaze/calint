from src.modelo.evento import Evento
from datetime import datetime


class Data:
    def __init__(
        self,
        id: int = 0,
        data: str = "",
        eventos: list[Evento] = [],
        # cor: str = "#f3f3f3",
    ) -> None:

        self._data = data  # datetime.strptime(data, "%d/%m/%Y")
        self._eventos = eventos
        self._id = id
        # self._cor = cor

    @property
    def data(self) -> str:
        return self._data

    @property
    def data_str(self) -> str:
        return self._data  # .strftime("%d/%m/%Y")

    @data.setter
    def data(self, nova_data: str):
        self._data = nova_data  # datetime.strptime(nova_data, "%d/%m/%Y")

    # @property
    # def cor(self) -> str:
    #     return self._cor

    # @cor.setter
    # def cor(self, nova_cor: str) -> str:
    #     self._cor = nova_cor

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def eventos(self) -> list[Evento]:
        return self._eventos

    @eventos.setter
    def eventos(self, novos_eventos: list[Evento]):
        self._eventos = novos_eventos

    def data_longa(self):
        # data_longa = self.data.strftime("%A, %d de %B de %Y")
        obj_data = datetime.strptime(self.data, "%A, %d de %B de %Y")
        data_longa = datetime.strftime(obj_data, "%A, %d de %B de %Y")
        return data_longa

    def delta_today(self) -> int:
        obj_data = datetime.strptime(self.data, "%A, %d de %B de %Y")
        delta = datetime.today() - obj_data
        return delta.days

    def __str__(self):
        eventos = ""
        for evento in self._eventos:
            # eventos += f"{evento.evento_categoria.categoria} | "
            eventos += f"{evento.evento} | "

        # Data categoria = {self._data_categoria.categoria}
        return f"""
            ID = {self._id}
            Data = {self._data}                         
            Eventos: {eventos}
            --------
            """

    # repr += f"data_categoria = {self._data_categoria.categoria})"
    def __repr__(self):
        repr = f"Data(id = {self._id},"
        repr += f"data = {self._data})"  # {self._data.strftime('%d/%m/%Y')},"
        return repr
