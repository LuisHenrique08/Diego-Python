# Lista original de números
numeros = [10, 20, 30, 40, 50]

# Função para calcular a soma dos números
def calcular_soma(lista):
    return sum(lista)

# Função para encontrar o maior número
def encontrar_maior(lista):
    return max(lista)

# Função para calcular a média dos números
def calcular_media(lista):
    return sum(lista) / len(lista)

# Exibir a lista original
print("Lista original:", numeros)

# Calcular e exibir a soma
soma = calcular_soma(numeros)
print("Soma dos elementos:", soma)

# Encontrar e exibir o maior número
maior = encontrar_maior(numeros)
print("Maior número:", maior)

# Calcular e exibir a média
media = calcular_media(numeros)
print("Média dos números:", media)

# Adicionar o número 60 à lista
numeros.append(60)
print("\nApós adicionar o número 60:")
print("Nova lista:", numeros)

