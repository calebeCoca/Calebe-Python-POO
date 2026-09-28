from pedidoreserva import Pedido
from cliente import Cliente
from Produto import Produto
 
 
#criar um objeto - representar um elemento - dar valores
novoPedido = Pedido(1, "14/09/2026", "21:10", "Rafael",
                    ["X-Salada", "X-Bacon"], "Pix")
 
##### Oque eu posso fazer com o objeto #####
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