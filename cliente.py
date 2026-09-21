class Cliente:
 
    # Construtor + Atributos
 
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
 
        # Métodos - ações
 
    def gettelefone(self):
        return self.__telefone
    
    def settelefone(self, telefone):
        self.__telefone=telefone
    
    def imprimirficha(self):
        print(f"|---Nome: {self.nome}---|")
        print(f"|--Telefone: {self.telefone}--|")
        print(f"|--Endereço: {self.endereco}--|")
 
        # Criar um objeto
 
        novoCliente = Cliente("João", "1234-8765", "Rua Legalzinha")
 
        # Acessar atributos
 
        print(novoCliente.nome)
 
        # Chamar método
 
        novoCliente.imprimir()
 