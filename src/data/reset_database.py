from src.data.data_db import DataDB
from src.data.evento_categoria_db import EventoCategoriaDB
from src.data.evento_db import EventoDB
from src.data.database_singleton import DataDBSingleton

class ResetDatabase:

    def __init__(self, dbs: DataDBSingleton):
        self.data_db = DataDB(dbs)
        self.evento_categoria_db = EventoCategoriaDB(dbs) 
        self.evento_db = EventoDB(dbs)

    def resetar(self):
        self.data_db.excluir_tabela_evento_data()
        self.evento_db.excluir_tabela()
        self.evento_categoria_db.excluir_tabela()
        self.data_db.excluir_tabela_data()

        self.data_db.criar_tabela_data()
        self.evento_categoria_db.criar_tabela_evento_categoria()
        self.evento_db.criar_tabela_evento()        
        self.data_db.criar_tabela_evento_data()
