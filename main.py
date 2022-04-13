<<<<<<< HEAD
from re import A
=======
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d
from PilhaEncadeada import Pilha
from Jogador import Jogador
from Baralho import Baralho
import random

print('''
<<<<<<< HEAD
      -------------------- Bem vindo ao jogo Batalha --------------------

=======
               ----Bem vindo ao jogo Batalha---  
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d
Regras do jogo:
1. Divide-se as cartas do baralho, igualmente, para dois jogadores. 
2. A menor carta é o Ás e a maior do baralho é o Rei. 
3. Não importa o naipe. 
4. Cada jogador inicia com seu próprio conjunto de cartas empilhadas, viradas para baixo. 
<<<<<<< HEAD
5. A batalha começa quando cada jogador retira uma carta do topo do seu baralho e a revela na mesa. 
   Então, aquele que apresentar a carta de MAIOR valor, vence a batalha e recebe a carta do outro jogador. 
6. As duas cartas são adicionadas à base do baralho.
7. No caso de cada jogador apresentar a mesma carta, elas ficam bloqueadas e outro par de cartas é puxado. 
8. Ganha o total de cartas acumuladas o jogador que desempatar a batalha.
9. O jogo termina após 26 rodadas e o jogador com mais pontos ganha a partida. 
''')

print("---------- Batalha ---------- \n")
jogar = True
#Loop principal
while (jogar):
    
    contadorDeRodadas = 0
    baralho = Baralho()
    montanteDeEmpate = Pilha()

    #Instanciando os dois jogadores
    print("Digite o nome do jogador(a) 1")
=======
5. A batalha começa quando cada jogador retira uma carta do topo do seu baralho e a revela na mesa. Então, aquele que apresentar a carta de maior valor, vence a batalha e recebe a carta do outro jogador. 
6. As duas cartas são adicionadas à base do baralho.
7. No caso de cada jogador apresentar a mesma carta, elas ficam bloqueadas e outro par de cartas é puxado. 
8. Ganha o total de cartas acumuladas o jogador que desempatar a batalha. 
''')

print("---------- Batalha ---------- \n")

#Loop principal
while (True):
    
    contadorDeJogadas = 0
    baralho = Baralho()
    montanteDeEmpate = list()

    #Instanciando os dois jogadores
    print("Digite o nome do jogador 1")
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d
    nomeDoJogador1 = input()
    jogador1 = Jogador(nomeDoJogador1)
    print()

<<<<<<< HEAD
    print("Digite o nome do jogador(a) 2")
=======
    print("Digite o nome do jogador 2")
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d
    nomeDoJogador2 = input()
    jogador2 = Jogador(nomeDoJogador2)
    print()

    
    #Distribuindo as cartas
    tamanho_do_baralho = baralho.__len__() 
<<<<<<< HEAD
    metadeDoBaralho = (tamanho_do_baralho - 1) / 2 
    n = 0

    while(n <= metadeDoBaralho):
=======
    numero_de_rodadas = (tamanho_do_baralho - 1) / 2 #
    n = 0
    #*******transformar em método "contarRodadas"
    while(n <= numero_de_rodadas):
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d
        n += 1
        jogador1.cartasDoJogador.empilha(baralho.retirarCarta())
        jogador2.cartasDoJogador.empilha(baralho.retirarCarta())

<<<<<<< HEAD
    #Loop para numerar a jogada da vez.
    while(contadorDeRodadas != 26):
        print()
        print(f"------------------- Rodada #{contadorDeRodadas + 1}: --------------------\n")

        cartaNaMaoDoJogador1 = jogador1.cartasDoJogador.desempilha() #Retira a carta da coleção do jogador e atribui a mao.
        cartaNaMaoDoJogador2 = jogador2.cartasDoJogador.desempilha()
        
        numeroDaCartaDoJogador1 = cartaNaMaoDoJogador1.converterParaNumero() #Atribuindo a uma variavel o número da carta
        numeroDaCartaDoJogador2 = cartaNaMaoDoJogador2.converterParaNumero()


        # Comparando os numeros das cartas
        if(numeroDaCartaDoJogador1 > numeroDaCartaDoJogador2):
            jogador1.pontos += 1
            jogador1.montanteReserva.empilha(cartaNaMaoDoJogador2) #Carta recebida em caso de vitoria vai para outro montante

            print(f"Carta na mão do jogador(a) {jogador1.nome.upper()}: {cartaNaMaoDoJogador1}")
            print(f"Carta na mão do jogador(a) {jogador2.nome.upper()}: {cartaNaMaoDoJogador2}")

            print()
            print(f"Ponto para o jogador(a) {jogador1.nome.upper()}")
            
            print()
            print(f"Carta adquirida: \n{cartaNaMaoDoJogador2}")

            
            #No caso de empate, cada jogador tira mais uma carta para definir o vencedor da rodada.
            if(not montanteDeEmpate.estaVazia()):
                print(montanteDeEmpate.imprime())
                  
                for n in range(montanteDeEmpate.tamanho()):
                    jogador1.montanteReserva.empilha(montanteDeEmpate.desempilha())
            

        elif(numeroDaCartaDoJogador1 < numeroDaCartaDoJogador2):
            jogador2.pontos += 1
            jogador2.montanteReserva.empilha(cartaNaMaoDoJogador1) #Carta recebida em caso de vitoria vai para outro montante

            print(f"Carta na mão do jogador(a) {jogador1.nome.upper()}: {cartaNaMaoDoJogador1}")
            print(f"Carta na mão do jogador(a) {jogador2.nome.upper()}: {cartaNaMaoDoJogador2}")
            
            print()
            print(f"Ponto para o jogador(a) {jogador2.nome.upper()}")

            print()
            print(f"Carta adquirida: \n{cartaNaMaoDoJogador1}")

            
            #No caso de emprate, cada jogador tira mais uma carta para definir o vencedor da rodada.
            if(not montanteDeEmpate.estaVazia()):
                print(montanteDeEmpate.imprime())
                  
                for n in range(montanteDeEmpate.tamanho()):
                    jogador2.montanteReserva.empilha(montanteDeEmpate.desempilha())

        elif(numeroDaCartaDoJogador1 == numeroDaCartaDoJogador2):
            print(f"Carta na mão do jogador(a) {jogador1.nome.upper()}: {cartaNaMaoDoJogador1}")
            print(f"Carta na mão do jogador(a) {jogador2.nome.upper()}: {cartaNaMaoDoJogador2}\n")
            print("EMPATE")
            montanteDeEmpate.empilha(cartaNaMaoDoJogador1)
            montanteDeEmpate.empilha(cartaNaMaoDoJogador2)

            print(montanteDeEmpate.imprime())
=======
    print(jogador1)
    print(jogador2)
    #Loop para numerar a jogada da vez.
    while(contadorDeJogadas <= 25):
        print()
        print(f"------------------- Jogada #{contadorDeJogadas + 1}: --------------------\n")

        cartaNaMaoDoJogador1 = jogador1.cartasDoJogador.desempilha() #Retira a carta da coleção do jogador e atribui a mao.
        cartaNaMaoDoJogador2 = jogador2.cartasDoJogador.desempilha()


        #Metodo de comparaçao presente na classe Carta
        if(cartaNaMaoDoJogador1.__gt__(cartaNaMaoDoJogador2)):
            jogador1.pontos += 1
            jogador1.montanteReserva.append(cartaNaMaoDoJogador2) #Carta recebida em caso de vitoria vai para outro montante

            print(f"Carta na mão do jogador {jogador1.nome}: {cartaNaMaoDoJogador1}")
            print(f"Carta na mão do jogador {jogador2.nome}: {cartaNaMaoDoJogador2}")

            print()
            print(f"Ponto para o jogador {jogador1.nome}")
            
            print()
            print(f"Carta adquirida: {cartaNaMaoDoJogador2}")

             
            #No caso de emprate, cada jogador tira mais uma carta para definir o vencedor da rodada.
            if(montanteDeEmpate != []):
                for carta in montanteDeEmpate:
                    print(carta.__str__(), sep="\n")
            
            jogador1.montanteReserva.append(montanteDeEmpate)
            montanteDeEmpate.clear()

        elif(cartaNaMaoDoJogador2.__gt__(cartaNaMaoDoJogador1)):
            jogador2.pontos += 1
            jogador2.montanteReserva.append(cartaNaMaoDoJogador1) #Carta recebida em caso de vitoria vai para outro montante

            print(f"Carta na mão do jogador {jogador1.nome}: {cartaNaMaoDoJogador1}")
            print(f"Carta na mão do jogador {jogador2.nome}: {cartaNaMaoDoJogador2}")
            
            print()
            print(f"Ponto para o jogador {jogador2.nome}")

            print()
            print(f"Carta adquirida: {cartaNaMaoDoJogador1}")


            #No caso de emprate, cada jogador tira mais uma carta para definir o vencedor da rodada.
            if(montanteDeEmpate != []):
                for carta in montanteDeEmpate:
                    print(carta.__str__(), sep="\n")
            
            jogador2.montanteReserva.append(montanteDeEmpate)
            montanteDeEmpate.clear()

        elif(cartaNaMaoDoJogador1.__eq__(cartaNaMaoDoJogador2)):
            montanteDeEmpate.append(cartaNaMaoDoJogador1)
            montanteDeEmpate.append(cartaNaMaoDoJogador2)

            for x in range(len(montanteDeEmpate)):
                print(montanteDeEmpate[x] , sep="\n")
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d
        
            


        print(f"--------- PLACAR DA RODADA ---------")
<<<<<<< HEAD
        print(f"{jogador1.nome.upper()} {jogador1.pontos} x {jogador2.pontos} {jogador2.nome.upper()}")

        contadorDeRodadas += 1

        #Verifica se o montante principal do jogador está vazio e adiciona ao montante principal as cartas do montante reserva
        if(jogador1.cartasDoJogador.estaVazia()):
            
            while(not jogador1.montanteReserva.estaVazia()):
                carta = jogador1.montanteReserva.desempilha()
                jogador1.cartasDoJogador.empilha(carta)
                
        #Verifica se o montante principal do jogador está vazio e adiciona ao montante principal as cartas do montante reserva
        if(jogador2.cartasDoJogador.estaVazia()):
            
            while(not jogador2.montanteReserva.estaVazia()):
                carta = jogador2.montanteReserva.desempilha()
                jogador2.cartasDoJogador.empilha(carta)
=======
        print(f"{jogador1.nome} {jogador1.pontos} x {jogador2.pontos} {jogador2.nome}")

        if(jogador1.cartasDoJogador.estaVazia()):
            for carta in jogador1.montanteReserva: 
                random.shuffle(jogador1.montanteReserva)
                jogador1.cartasDoJogador.empilha(carta)
                

        if(jogador2.cartasDoJogador.estaVazia()):
            for carta in jogador1.montanteReserva:
                random.shuffle(jogador2.montanteReserva)     
                jogador2.cartasDoJogador.empilha(carta)
        contadorDeJogadas += 1
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d

        print("PRESSIONE ENTER PARA CONTINUAR")
        input()

<<<<<<< HEAD
    if(jogador1.pontos > jogador2.pontos):
        print(f'JOGADOR(A) {jogador1.nome.upper()} VENCEU A PARTIDA!!!')
    elif(jogador2.pontos > jogador1.pontos):
        print(f'JOGADOR(A) {jogador2.nome.upper()} VENCEU A PARTIDA!!!')

    


    
    #Verifica se o usuário gostaria de jogar novamente.    
    print()
    print("Deseja jogar novamente? (s/n)")
    jogarNovamente = input()

    while (jogarNovamente.upper() != 'S' and jogarNovamente.upper() != 'N' ):
        print('Entrada inválida')
        print("Deseja jogar novamente? (s/n)")
        jogarNovamente = input()    

    if (jogarNovamente.upper() == 'S'):
            jogar = True    

    elif (jogarNovamente.upper() == 'N'):
            print('Programa encerrado')
            jogar = False
        


       

=======
    #Verifica se o usuário gostaria de jogar novamente.
    print()
    print("Deseja jogar novamente? (s/n)")
    jogarNovamente = input()
    

    if (jogarNovamente.upper() == 'N'):
        break
>>>>>>> 4ffe0944bfa6dc45099ad8140770e35abaf33d1d
