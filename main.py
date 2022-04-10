from PilhaEncadeada import Pilha
from Jogador import Jogador
from Baralho import Baralho
import random

print("teste")
print('''
      -------------------- Bem vindo ao jogo Batalha --------------------

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
    
    contadorDeRodadas = 0
    baralho = Baralho()
    montanteDeEmpate = Pilha()

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

    #Loop para numerar a jogada da vez.
    while(contadorDeRodadas != 26):
        print()
        print(f"------------------- Jogada #{contadorDeRodadas + 1}: --------------------\n")

        cartaNaMaoDoJogador1 = jogador1.cartasDoJogador.desempilha() #Retira a carta da coleção do jogador e atribui a mao.
        cartaNaMaoDoJogador2 = jogador2.cartasDoJogador.desempilha()
        
        numeroDaCartaDoJogador1 = cartaNaMaoDoJogador1.converterParaNumero() #Atribuindo a uma variavel o número da carta
        numeroDaCartaDoJogador2 = cartaNaMaoDoJogador2.converterParaNumero()


        # Comparando os numeros das cartas
        if(numeroDaCartaDoJogador1 > numeroDaCartaDoJogador2):
            jogador1.pontos += 1
            jogador1.montanteReserva.empilha(cartaNaMaoDoJogador2) #Carta recebida em caso de vitoria vai para outro montante

            print(f"Carta na mão do jogador {jogador1.nome}: {cartaNaMaoDoJogador1}")
            print(f"Carta na mão do jogador {jogador2.nome}: {cartaNaMaoDoJogador2}")

            print()
            print(f"Ponto para o jogador {jogador1.nome}")
            
            print()
            print(f"Carta adquirida: \n{cartaNaMaoDoJogador2}")

            #NAO ESTA FUNCIONANDO
            #No caso de empate, cada jogador tira mais uma carta para definir o vencedor da rodada.
            # if(not montanteDeEmpate.estaVazia()):
            #     for carta in range(montanteDeEmpate.tamanho()):
            #         print(carta, sep="\n")
            
            if (not montanteDeEmpate.estaVazia()):
                print(montanteDeEmpate)

            for carta in range(montanteDeEmpate.tamanho()):
                jogador1.montanteReserva.empilha(carta)
            

        elif(numeroDaCartaDoJogador1 < numeroDaCartaDoJogador2):
            jogador2.pontos += 1
            jogador2.montanteReserva.empilha(cartaNaMaoDoJogador1) #Carta recebida em caso de vitoria vai para outro montante

            print(f"Carta na mão do jogador {jogador1.nome}: {cartaNaMaoDoJogador1}")
            print(f"Carta na mão do jogador {jogador2.nome}: {cartaNaMaoDoJogador2}")
            
            print()
            print(f"Ponto para o jogador {jogador2.nome}")

            print()
            print(f"Carta adquirida: \n{cartaNaMaoDoJogador1}")

            #NAO ESTA FUNCIONANDO
            #No caso de emprate, cada jogador tira mais uma carta para definir o vencedor da rodada.
            # if(not montanteDeEmpate.estaVazia()):
            #     for carta in range(montanteDeEmpate.tamanho()):
            #         print(carta, sep="\n")
            if(not montanteDeEmpate.estaVazia()):
                print(montanteDeEmpate)

            for carta in range(montanteDeEmpate.tamanho()):
                jogador2.montanteReserva.empilha(carta)

        elif(numeroDaCartaDoJogador1 == numeroDaCartaDoJogador2):
            print(f"Carta na mão do jogador {jogador1.nome}: {cartaNaMaoDoJogador1}")
            print(f"Carta na mão do jogador {jogador2.nome}: {cartaNaMaoDoJogador2}\n")
            print("EMPATE")
            montanteDeEmpate.empilha(cartaNaMaoDoJogador1)
            montanteDeEmpate.empilha(cartaNaMaoDoJogador2)

            print(montanteDeEmpate)
        
            


        print(f"--------- PLACAR DA RODADA ---------")
        print(f"{jogador1.nome} {jogador1.pontos} x {jogador2.pontos} {jogador2.nome}")

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

        # print("PRESSIONE ENTER PARA CONTINUAR")
        # input()

    #Verifica se o usuário gostaria de jogar novamente.
    print()
    print("Deseja jogar novamente? (s/n)")
    jogarNovamente = input()
    

    if (jogarNovamente.upper() == 'N'):
        break
