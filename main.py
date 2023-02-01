class Produto:
    def __init__(self, nome, preço, tipo):
        self.nome = nome
        self.preço = preço
        self.tipo = tipo

    def exibir(self, indice = 0):
        print(f'{indice} -- Nome: {self.nome} - Preço: {self.preço} - Tipo: {self.tipo}')
    

produto_um = Produto('Pizza', 5.0, 'Portuguesa')
produto_dois = Produto('Lasanha', 20, 'Frango')

produtos = [produto_um, produto_dois]
for produto in produtos:
    indice = produtos.index(produto)
    produto.exibir(indice)

indice_selecionado = int(input('Selecione o produto: '))
if indice_selecionado > len(produtos):
    print('Produto inexistente')
else:
    produto = produtos[indice_selecionado] 
quantidade = int(input('Informe a quantidade: '))
print(f'O valor total é R$ {quantidade * produto.preço}')


