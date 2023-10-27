
class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer")
    def som(self):
        print(f"{self.nome} está emitindo som")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def som(self):
        print(f"{self.nome} foi miar")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def som(self):
        print(f"{self.nome} foi latir")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def som(self):
        print(f"{self.nome} foi mugir")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"{self.nome} foi ronronar")