# Baralho = coleçao de cartas (lista de cartas)
from Carta import Carta
from PilhaEncadeada import *
import random



class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Baralho:
    def __init__(self):
        self.baralho = Pilha()
        naipe = ["Ouro", "Espada", "Paus", "Copas"]
        cor =   ["vermelho", "preto", "preto", "vermelho"]
        numeracao = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

        for idx in range(len(naipe)):
            for id in numeracao:
                self.baralho.empilha( Carta(id, naipe[idx], cor[idx] ))

    def __len__(self):
        return self.baralho.tamanho()

    def temCarta(self):
        if self.baralho.estaVazia() == True:
            return True
        else:
            return False
    
    def retirarCarta(self)->Carta:
        try:
            return self.baralho.desempilha()
        except IndexError :
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')

    def embaralhar(self):
        baralhoTemporario = list()
        for i in range(self.baralho.tamanho()):
            carta = self.baralho.desempilha()
            baralhoTemporario.append(carta)
        
        random.shuffle(baralhoTemporario)

        for carta in baralhoTemporario:
            self.baralho.empilha(carta)

    def __str__(self):
        # saida = ''
        # for carta in self.baralho:
        #     saida += carta.__str__() + '\n' 
        # return saida
        return self.baralho.__str__()
