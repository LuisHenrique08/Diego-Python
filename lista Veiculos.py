from abc import ABC, abstractmethod

# Classe abstrata Veiculo
class Veiculo(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def calcular_custo_viagem(self, distancia):
        pass

# Subclasse Carro
class Carro(Veiculo):
    def calcular_custo_viagem(self, distancia):
        return distancia * 0.5

# Subclasse Bicicleta
class Bicicleta(Veiculo):
    def calcular_custo_viagem(self, distancia):
        return distancia * 0.1

# Subclasse Caminhao
class Caminhao(Veiculo):
    def calcular_custo_viagem(self, distancia):
        return distancia * 1.0

# Criando os veículos
carro = Carro("Carro")
bicicleta = Bicicleta("Bicicleta")
caminhao = Caminhao("Caminhão")

# Lista de veículos
veiculos = [carro, bicicleta, caminhao]

# Distância da viagem
distancia_total = 200  # km

# Calculando custos
custos = []
custo_total = 0

for veiculo in veiculos:
    custo = veiculo.calcular_custo_viagem(distancia_total)
    custos.append((veiculo.nome, custo))
    custo_total += custo

# Exibindo resultados
print("Custos da viagem de 200km para cada veículo:")
for nome, custo in custos:
    print(f"{nome}: R${custo:.2f}")

print(f"\nCusto total da viagem para todos os veículos: R${custo_total:.2f}")