class EventoCategoria:
    def __init__(
        self,
        categoria: str,
        descricao: str = "Não cadastrada",
        id: int = 0,
        cor: str = "",
    ) -> None:

        self._categoria = categoria
        self._descricao = descricao
        self._id = id
        self._cor = cor

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, novo_id: int) -> int:
        self._id = novo_id

    @property
    def cor(self) -> int:
        return self._cor
    
    @cor.setter
    def cor(self, nova_cor: int) -> int:
        self._cor = nova_cor

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
              cor = {self._cor}
              """

    def __repr__(self):
        repr = f"EventoCategoria(id = {self._id},"
        repr += f"categoria = {self._categoria},"
        repr += f"descricao = {self._descricao},"
        repr += f"cor = {self._cor}"
        return repr
