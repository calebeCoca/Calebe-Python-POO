# 🎁 Projeto Lanche

Este projeto foi desenvolvido durante as aulas do curso de **Técnico em Desenvolvimento de Software** do **SENAC**, com o objetivo de colocar em prática os conhecimentos adquiridos ao longo do curso, trabalhando com Python e Programação Orientada a Objetos (POO).

## ➡️ Como rodar nosso projeto

Siga o passo a passo abaixo para baixar e executar o projeto em seu computador.

### 1. Instale o Python

Baixe e instale a versão mais recente do Python pelo site oficial:

https://www.python.org/downloads/

### 2. Clone o repositório

Abra o terminal do seu computador e execute o seguinte comando:

```bash
git clone https://github.com/calebeCoca/Calebe-Python-POO.git
```

### 3. Abra o projeto no VS Code

* Acesse a pasta onde o projeto foi baixado.
* Abra o terminal dentro dessa pasta.
* Execute o comando:

```bash
code .
```

Isso abrirá o projeto no Visual Studio Code.

### 4. Execute o projeto

* Localize e abra o arquivo `main.js`.
* Clique no botão **Executar** do VS Code para iniciar o programa.

## 📚 Entendendo as classes

Nesta seção, vamos apresentar as classes utilizadas no projeto e explicar suas funcionalidades, atributos e métodos, facilitando a compreensão da estrutura do código.

```python
#criar um objeto - representar um elemento - dar valores
novoPedido = Pedido(1, "14/09/2026", "21:10", "Rafael",
                    ["X-Salada", "X-Bacon"], "Pix")
 
 Oque eu posso fazer com o objeto 
#acessar um atributo
print(novoPedido.num)
print(novoPedido.status)
#alterar os dados de um atributo
novoPedido.cliente="Rafael Martins"
print(novoPedido.cliente)
 
#chamando os metodos
novoPedido.imprimir()
novoPedido.atualizar_pedido("Em preparação")
 
#acessar o id - private
#novoPedido.__Num=2
#print(novoPedido.__num) #acessar
#novoPedido.imprimir()
 
print(novoPedido.getnum())
novoPedido.setnum(2)
print(novoPedido.getnum())
 
novoPedido.setitem("X-Calabresa")
novoPedido.imprimir()


novoCliente = Cliente(endereco="Rua dahora 157",nome="Garoto bacanudo", telefone="987654321") 
novoCliente.imprimirficha()

novoPedido = Pedido(1, "14/09/26", "21:20", novoCliente, 
                    ["X-salada", "X-bacon"], "pix ")
novoPedido.imprimir()

#criar produto
xbacon = Produto(cod="P01", desc="X-bacon", categoria="Lanche", preco=19.90)
xbacon.imprimirproduto()