def jogar():
    print("******************************")
    print("Bem-vindo(a) ao jogo da forca!")
    print("******************************")

    palavra_secreta = "banana"
    tamanho_palavra = len(palavra_secreta)
    letra_posicao = []

    for i in range(tamanho_palavra):
        letra_posicao.append("_")
    
    print("Essa é a palavra a ser adivinhada: {}".format(letra_posicao))

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Digite um letra: ").strip().lower()
        pos = 0
        
        for letra in palavra_secreta:
            if(letra == chute):
                letra_posicao[pos] = chute
            pos = pos + 1
            
        print(letra_posicao)

        ## Implantar o enforcou ou acertou

if(__name__ == "__main__"):
    jogar()

    