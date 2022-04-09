from Baralho import Baralho
from Carta import Carta
from PilhaEncadeada import *

class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Jogador:
    def __init__(self, nome):
        self.__nome = nome 
        self.pontos = 0
        self.cartasDoJogador = Pilha()
        self.montanteReserva = list()

    def __str__(self):
        return "Nome do jogador: " + self.__nome + "\n" + "Cartas: \n" + self.cartasDoJogador.__str__()

    def printCartas(self):
       self.cartasDoJogador.imprime()

    def lenCartas(self):
        return self.cartasDoJogador.__len__()

    @property
    def nome(self):
        return self.__nome

    def desempilha(self):
        self.cartasDoJogador.desempilha()
    
    def empilha(self, valor):
        self.cartasDoJogador.empilha(valor)

    def mostrarMontanteReserva(self):
        print("[")
        saida = ''
        for carta in self.montanteReserva:
            saida += carta.__str__() + ', '
        print(']')
    