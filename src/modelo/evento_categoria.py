class EventoCategoria:
    def __init__(
        self,
        categoria: str,
        descricao: str,
        id: int = 0,
    ) -> None:

        self._categoria = categoria
        self._descricao = descricao
        self._id = id

    @property
    def id(self) -> int:
        return self._id

    @property
    def categoria(self) -> str:
        return self._categoria

    @property
    def descricao(self):
        return self._descricao

    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    def __str__(self):
        return f"""
              id = {self._id}
              categoria = {self._categoria}
              descricao = {self._descricao}
              """

    def __repr__(self):
        repr = f"EventoCategoria(id = {self._id},"
        repr += f"categoria = {self._categoria},"
        repr += f"descricao = {self._descricao}"
        return repr
