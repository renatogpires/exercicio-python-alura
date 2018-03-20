def jogar():
    print("******************************")
    print("Bem-vindo(a) ao jogo da forca!")
    print("******************************")

    #Define a palavra secreta
    palavra_secreta = "banana"
    
    #Define o tamanho da palavra que será preenchida pelos underscores
    tamanho_palavra = len(palavra_secreta)
    
    #Inicializa o número de tentativas
    tentativa = 1
    
    #Inicializa o vetor
    letra_posicao = []

    #Preenche o vetor com underscores baseados no tamanho da palavra secreta
    for i in range(tamanho_palavra):
        letra_posicao.append("_")
    
    print("Essa é a palavra a ser adivinhada, você tem 5 chances.: {}".format(letra_posicao))

    #Inicializa as variáveis de derrota e acerto
    enforcou = False
    acertou = False

    #Enquanto não enforca (5 chances) e não acerta, continua o jogo
    while (not enforcou and not acertou):
        
        #Se existem underscores na lista, é porquê o jogo não acabou
        if "_" in letra_posicao:
            print("Tentativa número: {}".format(tentativa))
            
            #Tratamento para espaços e letras maíusculas
            chute = input("Digite um letra: ").strip().lower()
            pos = 0
        
            #Se a letra do chute estiver na palavra secreta, coloca a mesma nas posições correspondentes
            for letra in palavra_secreta:
                if(letra == chute):
                    letra_posicao[pos] = chute
                pos = pos + 1

            #Verifica se há tentativas restantes para poder continuar o jogo
            if tentativa == 5:
                enforcou = True
                print("ENFORCOU. Fim de jogo!")
                print("A palavra secreta era: {}".format(palavra_secreta))
                
            tentativa =  tentativa + 1
            print("Resultado: {}".format(letra_posicao))

        #Se acertou, mostra a palavra e finaliza o jogo    
        else:
            acertou = True
            print("Você acertou!")
            print("A Palavra secreta é: {}".format(letra_posicao))

if(__name__ == "__main__"):
    jogar()

    