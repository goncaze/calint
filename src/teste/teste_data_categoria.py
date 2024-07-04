import os
from modelo.data_categoria import DataCategoria
from src.data.database import DataDB


# db = DataDB()

def ver_categorias_data(db:DataDB):
    """ Listagem de categorias"""
    print("\n\n Categorias disponíves: \n")
    for categoria in db.select_data_categoria_todos():
        print(categoria)


def registrar_categoria(db:DataDB):
    """ Novo cadastro de categoria para data """
    categoria = input("\n Informe a categoria: ")
    descricao = input("\n Informe a descrição: ")
    data_categoria = DataCategoria(categoria, descricao)
    db.insert_data_categoria(data_categoria)


def deletar_data_categoria(db:DataDB):
    """ Excluir da base uma categoria de data """
    ver_categorias_data(db)    
    print("\n\n")
    id = input("Informe o id da categoria que será excluída: ")
    db.delete_data_categoria(id)


def atualizar_data_categoria(db:DataDB):
    ver_categorias_data(db)    
    print("\n\n")
    id = input("Informe o id da categoria que será atualiazada: ")
    categoria = input("Atualizar atual categoria para: ")
    descricao = input("Atualizar atual descrição para: ")
    db.update_data_categoria(id, categoria, descricao)

menu = [
    "[1] - Ver categorias de data",
    "[2] - Inserir categoria de data",
    "[3] - Alterar categoria de data",
    "[4] - Exluir categoria de data",
    "[0] - Voltar"
]


def apresentar_menu():
    for opc in menu:
        print(opc)


def operacoes_data_categoria(db:DataDB):

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
                input("\n Tecle <ENTER> para continuar")  
                break
            case '1':
                os.system("cls")
                ver_categorias_data(db)
                input("\n Tecle <ENTER> para continuar")
            case '2':
                os.system("cls")
                registrar_categoria(db)
                input("\n Tecle <ENTER> para continuar")
            case '3':
                os.system("cls")
                atualizar_data_categoria(db)
                input("\n Tecle <ENTER> para continuar")
            case '4':
                os.system("cls")
                deletar_data_categoria(db)
                input("\n Tecle <ENTER> para continuar")                                
