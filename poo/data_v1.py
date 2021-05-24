class Data:
    # Construtor em python
    # Python não permite mais de um construtor
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # __str__ transforma o objeto em string
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2019
print(d1)

d2 = Data(7, 11, 2020)
# d2.dia = 7
# d2.mes = 11
# d2.ano = 2020
print(d2)
