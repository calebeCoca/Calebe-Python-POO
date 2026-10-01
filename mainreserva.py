from Produto import Produto
import os
from cliente import Cliente


listaClientes = []
listaprodutos = []
def menuCliente():
    while True:
        print("----  Clientes 👤 ----\n"+
            "1 - 📄 Cadastrar\n"+
            "2 - 🔎 Listar\n"+
            "3 - 📝 Alterar\n"+
            "4 - ❌ Excluir\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        elif opcao=="1":
            print("|---- 🙋Novo cliente ----|\n")

            nome=input("| 🔤Nome do cliente: \n")
            telefone=input("| 📞Telefone: \n")
            endereco=input("| 🏠Endereço: \n")

            novocli = Cliente(nome=nome,telefone=telefone,endereco=endereco)
            listaClientes.append(novocli)
            input("| 🟩🧑   Salvo com sucesso!!\n !Aperte a tecla enter para voltar!")

        elif opcao =="2":
                for novocli in listaClientes:
                    novocli.imprimir()
def menuProduto():
    while True:
        print("----  Produtos 📦 ----\n"+
            "1 - 📄 Cadastrar\n"+
            "2 - 🔎 Listar\n"+
            "3 - 📝 Alterar\n"+
            "4 - ❌ Excluir\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        elif opcao=="1":
            novoprod = Produto(input("|   🔢Código: "), input("|   🍟Categoria: "), input("|    🔡Descrição: "), input("|   💵Preço: "))
            listaprodutos.append(novoprod)
            input("| 🟩🛍️   Cadastrado com sucesso!!\n !Aperte a tecla enter para voltar!")
        elif opcao=="2":
            for novoprod in listaprodutos:
                novoprod.imprimir()

##main
if __name__ == "__main__":
    while True:
        os.system("cls")
        print("---- Sistema Lanchonete 🥪 ----\n"
            "1 - 👤 Clientes\n"+
            "2 - 📦 Produtos\n"+
            "3 - 🛒 Novo Pedido\n"+
            "0 - ⬅️ Sair\n")
        opcao = input("Digite a opção escolhida:")

        if opcao=="0":
            break
        elif opcao=="1":
            menuCliente()
        elif opcao=="2":
            menuProduto()
    print("\n bye!\n ( ﾟдﾟ)✌️   ")