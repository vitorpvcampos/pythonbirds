class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    vitor = Pessoa(nome='Vitor')
    mariozam = Pessoa(vitor, nome='Mariozam')
    print(Pessoa.cumprimentar(mariozam))
    print(id(mariozam))
    print(mariozam.cumprimentar())
    print(mariozam.nome)
    print(mariozam.idade)
    for filho in mariozam.filhos:
        print(filho.nome)
    mariozam.sobrenome = 'Ferreira'
    print(mariozam.sobrenome)
    del mariozam.filhos
    print(mariozam.__dict__)
    print(vitor.__dict__)
    print(Pessoa.olhos)
    print(vitor.olhos)
