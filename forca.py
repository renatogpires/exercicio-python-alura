def jogar():
    print("******************************")
    print("Bem-vindo(a) ao jogo da forca!")
    print("******************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Digite um letra: ").strip().lower()
        pos = 0

        for letra in palavra_secreta:
            if(letra == chute):
                print("A letra \"{}\" está na posição: {}".format(chute, pos))
            pos = pos + 1
            
        print("\nSegue o jogo...\n")

if(__name__ == "__main__"):
    jogar()