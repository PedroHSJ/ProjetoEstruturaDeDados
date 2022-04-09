from PilhaEncadeada import Pilha
from Jogador import Jogador
from Baralho import Baralho
import random

print('''
               ----Bem vindo ao jogo Batalha---  
Regras do jogo:
1. Divide-se as cartas do baralho, igualmente, para dois jogadores. 
2. A menor carta é o Ás e a maior do baralho é o Rei. 
3. Não importa o naipe. 
4. Cada jogador inicia com seu próprio conjunto de cartas empilhadas, viradas para baixo. 
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
    nomeDoJogador1 = input()
    jogador1 = Jogador(nomeDoJogador1)
    print()

    print("Digite o nome do jogador 2")
    nomeDoJogador2 = input()
    jogador2 = Jogador(nomeDoJogador2)
    print()

    
    #Distribuindo as cartas
    tamanho_do_baralho = baralho.__len__() 
    numero_de_rodadas = (tamanho_do_baralho - 1) / 2 #
    n = 0
    #*******transformar em método "contarRodadas"
    while(n <= numero_de_rodadas):
        n += 1
        jogador1.cartasDoJogador.empilha(baralho.retirarCarta())
        jogador2.cartasDoJogador.empilha(baralho.retirarCarta())

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
        
            


        print(f"--------- PLACAR DA RODADA ---------")
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

        print("PRESSIONE ENTER PARA CONTINUAR")
        input()

    #Verifica se o usuário gostaria de jogar novamente.
    print()
    print("Deseja jogar novamente? (s/n)")
    jogarNovamente = input()
    

    if (jogarNovamente.upper() == 'N'):
        break
