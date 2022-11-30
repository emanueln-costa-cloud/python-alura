import random

print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual nivel de dificuldade? ")
print("(1) Facil (2) Medio (3) Dificil")
print("ola")

nivel = int(input("Define o nivel: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 100: ")
    print("Voce digitou", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior do que o numero secreto.")
        elif(menor):
            print("Voce errou! O seu chute foi menor do que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute) #Ex: 40 - 20 = 20
        pontos = pontos - pontos_perdidos
    
print("Numero secreto era:", numero_secreto)   
print("Fim do jogo")