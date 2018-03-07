def jogar():
    print("******************************")
    print("Bem-vindo(a) ao jogo da forca!")
    print("******************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        print("Jogando")

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()

    # Fazer a captura da letra digitada pelo jogador
    # Tratar maiuscula e minuscula
    # Mostrar onde a letra digitada está (posição)