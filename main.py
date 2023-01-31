class Produto:
    def __init__(self, nome, preço, tipo):
        self.nome = nome
        self.preço = preço
        self.tipo = tipo

produto = Produto('Pizza', 5.0, 'Portuguesa')




quantidade = int(input('Informe a quantidade: '))
print(quantidade)

