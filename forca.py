import random

def jogar():
    print("******************************")
    print("Bem-vindo(a) ao jogo da forca!")
    print("******************************")

    arquivo = open("frutas.txt", "r")
    frutas = []

    for linha in arquivo:
        frutas.append(linha.strip())

    arquivo.close()
    lista_frutas = random.randrange(0, len(frutas))
    palavra_secreta = frutas[lista_frutas]
    tamanho_palavra = len(palavra_secreta)
    tentativa = 1
    letra_posicao = []
    enforcou = False
    acertou = False

    for i in range(tamanho_palavra):
        letra_posicao.append("_")
    
    print("Essa é a palavra a ser adivinhada, você tem {} chances.: {}".format(tamanho_palavra, letra_posicao))

    while (not enforcou and not acertou):    
        if "_" in letra_posicao and tentativa <= tamanho_palavra:
            print("Tentativa número: {}".format(tentativa))
            chute = input("Digite uma letra: ").strip().lower()
            pos = 0 

            for letra in palavra_secreta:
                if(letra == chute):
                    letra_posicao[pos] = chute
                pos = pos + 1    
    
            tentativa = tentativa + 1
            print("Resultado: {}".format(letra_posicao))

        elif "_" in letra_posicao and tentativa > tamanho_palavra:
            enforcou = True
            print("ENFORCOU. Fim de jogo!")
            print("A palavra secreta era: {}".format(palavra_secreta))      

        #Se acertou, mostra a palavra e finaliza o jogo    
        else:
            acertou = True
            print("Você acertou!")
            print("A Palavra secreta é: {}".format(letra_posicao))

if(__name__ == "__main__"):
    jogar()

    #TO DO: identificar se o jogador já não tem mais chances e, caso afirmativo, encerrar o jogo