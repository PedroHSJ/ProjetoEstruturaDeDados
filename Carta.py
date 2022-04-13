class Carta:

    def __init__(self, numero, naipe, cor):
        self.__numero = numero
        self.__naipe = naipe

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__numero
        
<<<<<<< HEAD
    def converterParaNumero(self):
        if (self.numero == "As"):
            return 1
        elif (self.numero == "2"):
            return 2
        elif (self.numero == "3"):
            return 3 
        elif (self.numero == "4"):
            return 4
        elif (self.numero == "5"):
            return 5
        elif (self.numero == "6"):
            return 6
        elif (self.numero == "7"):
            return 7
        elif (self.numero == "8"):
            return 8
        elif (self.numero == "9"):
            return 9
        elif (self.numero == "10"):
            return 10
        elif (self.numero == "Valete"):
            return 11
        elif (self.numero == "Dama"):
            return 12
        elif (self.numero == "Rei"):
            return 13
=======
         
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d

    
    def __str__(self): # todas as informacoes da carta
        return f'{self.__numero} de {self.__naipe}'
<<<<<<< HEAD
=======

    def __gt__(self, outraCarta):
        return self.numero > outraCarta.numero
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d
    
    def __eq__(self, outraCarta):
        return self.numero == outraCarta.numero