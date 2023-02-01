class Produto:
    def __init__(self, nome, preço, tipo):
        self.nome = nome
        self.preço = preço
        self.tipo = tipo

    def exibir(self):
        print(f'Nome: {self.nome} - Preço: {self.preço} - Tipo: {self.tipo}')
    

produto = Produto('Pizza', 5.0, 'Portuguesa')
produto.exibir()
quantidade = int(input('Informe a quantidade: '))
print(f'O valor total é R$ {quantidade * produto.preço}')


