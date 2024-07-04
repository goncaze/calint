import os
from modelo.data_categoria import DataCategoria
from src.modelo.data import Data
from src.data.database import DataDB
import src.teste.teste_data_categoria as teste_data_categoria


def ver_datas(db:DataDB):
    """ Listagem de datas """
    print("\n\n Datas registradas: \n")
    for datas in db.select_data_todas():
        print(datas)


def registrar_data(db:DataDB):
    """ Novo cadastro de data """
    nova_data = input("\n Informe a data no padrão dd/mm/YYYY: ")
    teste_data_categoria.ver_categorias_data(db)
    id_categoria_data = input("Selecione o id da categoria de data: ")
    id_categoria_data = int(id_categoria_data)
    dataCategoria: DataCategoria = db.select_data_categoria(id=id_categoria_data)
    data = Data(nova_data, dataCategoria)
    db.insert_data(data)


def deletar_data_categoria(db:DataDB):
    """ Excluir da base uma categoria de data """
    ver_datas(db)    
    print("\n\n")
    id = input("Informe o id da categoria que será excluída: ")
    db.delete_data_categoria(id)


def atualizar_data_categoria(db:DataDB):
    ver_datas(db)    
    print("\n\n")
    id = input("Informe o id da categoria que será atualiazada: ")
    categoria = input("Atualizar atual categoria para: ")
    descricao = input("Atualizar atual descrição para: ")
    db.update_data_categoria(id, categoria, descricao)

menu = [
    "[1] - Ver datas",
    "[2] - Inserir categoria de data",
    "[3] - Alterar categoria de data",
    "[4] - Exluir categoria de data",
    "[0] - Voltar"
]


def apresentar_menu():
    for opc in menu:
        print(opc)


def operacoes_data(db:DataDB):

    while(True):
        os.system("cls")
        print("---------------------------------------")
        print("TESTE OPERAÇÕES PARA CATEGORIAS DE DATA")
        print("---------------------------------------\n\n")
        apresentar_menu()

        opc = input("\n Informe opção: ")

        match opc:
            case '0':
                os.system("cls")
                print("\n Voltando... \n")
                break
            case '1':
                os.system("cls")
                ver_datas(db)
                input("\n Tecle <ENTER> para continuar")
            case '2':
                os.system("cls")
                registrar_data(db)
                input("\n Tecle <ENTER> para continuar")
            case '3':
                os.system("cls")
                atualizar_data_categoria(db)
                input("\n Tecle <ENTER> para continuar")
            case '4':
                os.system("cls")
                deletar_data_categoria(db)
                input("\n Tecle <ENTER> para continuar")                                
