#coding: utf-8

import random

print("*********************************")
print("Bem-vindo ao jogo da adivinhação!")
print("*********************************")

numero_secreto = random.randint(1,100)
tentativa = 50
rodada = 0
pontos = 1000


for rodada in range(rodada, tentativa):
    chute_str = input("Digite o seu número: ")

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número maior que 0 e menor que 100!")
        continue

    if(acertou):
        print("Você acertou e marcou {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O número digitado é maior que o número secreto")
        elif(menor):
            print("Você errou! O número digitado é menor que o número secreto")
    rodada += 1
    print("Rodada {} de {}".format(rodada, tentativa))
    dif_pontos = numero_secreto - chute
    pontos = pontos - abs(dif_pontos)

if(not acertou):
    print("Que pena, acabaram suas tentativas!")

    

    
    

