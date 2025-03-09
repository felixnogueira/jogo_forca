import game as g
import fileHandler as fh

def showMenu():
    print("="*30)
    print("MENU PRINCIPAL")
    print("="*30)
    print(" " * 7 + "JOGO DA FORCA")
    print("="*30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR")
    print("="*30)
    
fileName = "score.txt"
if fh.fileExists(fileName):
    print("Arquivo {} encontrado!".format(fileName))
else:
    print("Arquivo {} não encontrado!".format(fileName))
    fh.createFile(fileName)

while True:
    showMenu()
    option = int(input("Escolha uma opção (1/2/3): "))
    if option == 1:
        print("Iniciando jogo...")
        g.playGame()
    elif option == 2:
        print("Exibindo score...")
        data = fh.listFile("score.txt")
        if not data: 
            print("Nenhum score encontrado!")
        else:
            i = 1
            for playerName in data:
                playerName = playerName.split(";")
                print(f"{i} -> {playerName[0]}, Pontuação: {playerName[1]}")
                i += 1
    elif option == 3:
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
