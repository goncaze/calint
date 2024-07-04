class DataCategoria:

    def __init__(
        self,
        categoria: str = "",
        descricao: str = "Não cadastrada",
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
    def descricao(self) -> str:
        return self._descricao

    @categoria.setter
    def categoria(self, nova_categoria):
        self._categoria = nova_categoria

    @descricao.setter
    def descricao(self, nova_descricao: str):
        self._descricao = nova_descricao

    def __str__(self):
        return f""" \
              id = {self._id} \t categoria = {self._categoria} \t descrição = {self._descricao}
              """

    def __repr__(self):
        repr = f"DataCategoria(id = {self._id}, "
        repr += f"categoria = {self._categoria}, "
        repr += f"descricao = {self._descricao}"
        repr += ")"
        return repr

    # DIA_LETIVO = "Dia Letivo"
    # PONTO_FACULTATIVO = "Ponto Facultativo"
    # FERIAS = "Férias"
    # FERIADO = "Feriado"
    # RECESSO = "Recesso"
