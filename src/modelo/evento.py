from src.modelo.evento_categoria import EventoCategoria


class Evento:

    def __init__(
        self,        
        evento_categoria: EventoCategoria,
        evento: str,
        descricao: str = "Não cadastrada",
        id: int = 0,
    ) -> None:

        self._id = id
        self._evento_categoria: EventoCategoria = evento_categoria
        self._evento: str = evento
        self._descricao: str = descricao

    @property
    def evento(self) -> str:
        return self._evento

    @evento.setter
    def evento(self, novo_evento: str):
        self._evento = novo_evento

    @property
    def evento_categoria(self) -> EventoCategoria:
        return self._evento_categoria

    @evento_categoria.setter
    def evento_categoria(self, nova_categoria: EventoCategoria):
        self._evento_categoria = nova_categoria

    @property
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self.descricao = nova_descricao

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, novo_id: int) -> int:
        self._id = novo_id
            

    def __str__(self):
        return f"""
              id = {self._id}
              evento_categoria = {self._evento_categoria.categoria}
              evento = {self._evento}
              descricao = {self._descricao}
              """

    def __repr__(self):
        return f"""
            EventoCategoria(id = {self._id},            
                            evento_categoria = {self._evento_categoria.categoria},
                            evento = {self._evento},
                            descricao = {self._descricao})        
        """
        
        
        
        
        
