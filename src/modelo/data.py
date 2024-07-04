from src.modelo.data_categoria import DataCategoria
from src.modelo.evento import Evento
from datetime import datetime


class Data:
    def __init__(
        self,
        id: int = 0,
        data: str = "",
        data_categoria: DataCategoria = None, # type: ignore
        eventos: list[Evento] = [],
    ) -> None:

        self._data = data  # datetime.strptime(data, "%d/%m/%Y")
        self._data_categoria = data_categoria
        self._eventos = eventos
        self._id = id

    @property
    def data(self) -> str:
        return self._data

    @property
    def data_str(self) -> str:
        return self._data  # .strftime("%d/%m/%Y")

    @data.setter
    def data(self, nova_data: str):
        self._data = nova_data  # datetime.strptime(nova_data, "%d/%m/%Y")

    @property
    def data_categoria(self) -> DataCategoria:
        return self._data_categoria

    @data_categoria.setter
    def data_categoria(self, novo_data_categoria: DataCategoria):
        self._data_categoria = novo_data_categoria

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
            eventos += f"{evento.evento_categoria.categoria} | "
            # eventos += f"\t <>  Descrição: {evento.descricao} \n"

        return f"""
            ID = {self._id}
            Data = {self._data} 
            Data categoria = {self._data_categoria.categoria}
            
            Eventos: {eventos}
            --------
            """

    def __repr__(self):
        repr = f"Data(id = {self._id},"
        repr += f"data = {self._data},"  # {self._data.strftime('%d/%m/%Y')},"
        repr += f"data_categoria = {self._data_categoria.categoria})"
        return repr
