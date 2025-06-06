import random
from typing import Dict, List, Tuple

class Aluno:
    ESTADOS = ('ativo', 'transferido', 'desistente')
    
    def __init__(self):
        self.alunos = {}
        self.nomes_aleatorios = [
            'Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 
            'Igor', 'Julia', 'Kaio', 'Larissa', 'Marcos', 'Natalia', 'Otavio', 'Patricia', 
            'Quirino', 'Rafaela', 'Sergio', 'Tatiana', 'Ubirajara', 'Vanessa', 'Wagner'
        ]
        self._gerar_alunos()
    
    def _gerar_alunos(self):
        for i in range(1, 24):
            nome = self.nomes_aleatorios[i-1]
            
            # Definindo alguns estados diferentes diretamente na criação
            if i == 3 or i == 15:
                estado = 'transferido'
            elif i == 7 or i == 12:
                estado = 'desistente'
            else:
                estado = 'ativo'
            
            self.alunos[i] = {
                'nome': nome,
                'estado': estado
            }
    
    def alterar_estado(self, numero: int, novo_estado: str):
        if novo_estado.lower() not in self.ESTADOS:
            raise ValueError(f"Estado inválido. Use um dos seguintes: {self.ESTADOS}")
        
        if numero not in self.alunos:
            raise ValueError("Número de aluno inválido")
        
        self.alunos[numero]['estado'] = novo_estado.lower()
    
    def listar_alunos(self):
        for numero, info in self.alunos.items():
            print(f"Nome: {info['nome']}, Estado: {info['estado']}")


class NotasAlunos:
    def __init__(self):
        self.notas: Dict[int, List[float]] = {}
        self._gerar_notas_aleatorias()
    
    def _gerar_notas_aleatorias(self):
        for i in range(1, 24):
            # Gera entre 3 e 5 notas aleatórias por aluno (entre 0 e 10)
            self.notas[i] = [round(random.uniform(0, 10), 1) for _ in range(random.randint(3, 5))]
    
    def adicionar_nota(self, numero: int, nota: float):
        if numero not in self.notas:
            raise ValueError("Número de aluno inválido")
        self.notas[numero].append(nota)
    
    def remover_nota(self, numero: int, indice: int):
        if numero not in self.notas:
            raise ValueError("Número de aluno inválido")
        if indice < 0 or indice >= len(self.notas[numero]):
            raise ValueError("Índice de nota inválido")
        self.notas[numero].pop(indice)
    
    def listar_notas(self):
        for numero, notas in self.notas.items():
            print(f"Notas: {notas}")


class NumerosChamada:
    def __init__(self):
        self.numeros: Tuple[int, ...] = tuple(range(1, 24))
    
    def listar_numeros(self):
        print("Números de chamada:", self.numeros)


# Demonstração do código
print("=== Lista de Alunos com Estados Pré-Definidos ===")
alunos = Aluno()
alunos.listar_alunos()

print("\n=== Notas dos Alunos ===")
notas = NotasAlunos()
notas.listar_notas()

print("\n=== Números de Chamada ===")
chamada = NumerosChamada()
chamada.listar_numeros()