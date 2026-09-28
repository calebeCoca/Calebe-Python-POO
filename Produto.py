class Produto:
 
    def __init__(self, cod, desc, categoria, preco):
        self.codigo=cod
        self.descricao=desc
        self.categoria=categoria
        self.preco=preco
 
 
    def imprimirproduto(self):
        print(f"\n|Produto Cód: {self.codigo}|"
              f"\n|Descrição: {self.descricao}|"
              f"\n|Tipo: {self.categoria}|" 
              f"\n|Preço: {self.preco}")