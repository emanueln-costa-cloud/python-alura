
def jogar():
    print("*********************************")
    print("Bem vindo no jogo da Forca!")
    print("*********************************")
    
    palavra_secreta = "banana"
    
    enforcou = False
    acertou = False

    #enquanto nao enforcou(False)=True e nao acertou(False)=True
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()