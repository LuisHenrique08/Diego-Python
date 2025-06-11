import random

class Animal:
    def emitir_som(self):
        raise NotImplementedError("Método deve ser implementado nas subclasses")

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"
    
    def __str__(self):
        return "Cachorro"

class Gato(Animal):
    
    
    def emitir_som(self):  # Versão correta
        return "Miar"
    
    def __str__(self):
        return "Gato"

class Cavalo(Animal):
    def emitir_som(self):
        return "Relincho"
    
    def __str__(self):
        return "Cavalo"

# Função para demonstrar polimorfismo
def fazer_barulho(animal):
    print(f"{animal} faz: {animal.emitir_som()}")

# Criando instâncias dos animais
cachorro = Cachorro()
gato = Gato()
Cavalo = Cavalo()

# Lista de animais
animais = [cachorro, gato, Cavalo]

# Demonstração do polimorfismo
for animal in animais:
    fazer_barulho(animal)

# Exemplo adicional: selecionando um animal aleatório
