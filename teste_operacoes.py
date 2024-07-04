import os
from src.data.database import DataDB
from modelo.data_categoria import DataCategoria
from modelo.evento_categoria import EventoCategoria
from src.modelo.evento import Evento
from src.modelo.data import Data
import src.teste.teste_data_categoria as teste_data_categoria
import src.teste.teste_data as teste_data


from pathlib import Path
ROOT_DIR = Path(__file__).parent
DB_NAME = 'calendario_db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME


menu = [
    "[1] - Operações para data",
    "[2] - Operações para evento",
    "[3] - Operações para categoria de data",
    "[4] - Operações para categoria de de evento",
    "[0] - Encerrar App"
]


def apresentar_menu():
    for opc in menu:
        print(opc)

def controle(db: DataDB):
    while(True):
        os.system("cls")
        print("--------------------")
        print("TESTE PROJETO CALINT")
        print("--------------------\n\n")        
        apresentar_menu()

        opc = input("\n Informe opção: ")

        match opc:
            case '0':
                os.system("cls")
                print("\n Encerrando app... \n")
                input("\n Tecle <ENTER> para continuar")
                os.system("cls")
                break
            case '1':
                os.system("cls")
                teste_data.operacoes_data(db)
                input("\n Tecle <ENTER> para continuar")
            case '2':
                os.system("cls")
                print("\n Operações para data")
                input("\n Tecle <ENTER> para continuar")
            case '3':
                os.system("cls")
                teste_data_categoria.operacoes_data_categoria(db)

            case '4':
                os.system("cls")
                print("\n Operações para data")
                input("\n Tecle <ENTER> para continuar")


if __name__ == "__main__":
    db = DataDB(DB_FILE)

    controle(db)