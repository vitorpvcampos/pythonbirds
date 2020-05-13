class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}.'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atrib_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe} Aperto de mão.'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    vitor = Mutante(nome='Vitor')
    mariozam = Homem(vitor, nome='Mariozam')
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
    print(Pessoa.metodo_estatico(), mariozam.metodo_estatico())
    print(Pessoa.nome_e_atrib_de_classe(), mariozam.nome_e_atrib_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(vitor, Pessoa))
    print(isinstance(vitor, Homem))
    print(mariozam.cumprimentar())
    print(vitor.cumprimentar())
