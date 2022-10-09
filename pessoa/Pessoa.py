class Pessoa:
    def __init__(self, nome, sobrenome, idade, data_nascimento):
        self._nome = nome
        self.sobrenome = sobrenome
        self._idade = idade
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        valor = valor.split(' ', 1)
        self._nome = valor[0]
        self.sobrenome = valor[1]

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError
        self._idade = valor

    def fazer_aniversario(self):
        self.idade += 1
