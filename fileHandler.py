def fileExists(fileName):
    try:
        a = open(fileName, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def openReadFile(fileName):
    try:
        a = open(fileName, "r")
    except FileNotFoundError:
        print("Não foi possível abrir o arquivo para leitura")
    else:
        print(f"Arquivo {fileName} aberto com sucesso!\n")
        return a

def createFile(fileName):
    try:
        a = open(fileName, "wt+")
        a.close()
    except:
        print("Não foi possível criar o arquivo")
    else:
        print(f"Arquivo {fileName} criado com sucesso!\n")

def listFile(fileName):
    try:
        a = open(fileName, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        data = a.readlines()
    finally:
        a.close()
        return data

def insertScore(fileName, playerName, playerScore):
    try:
        a = open(fileName, "at")
    except:
        print("Erro ao abrir o arquivo")
    else:
        a.write("{};{}\n".format(playerName, playerScore))
    finally:
        a.close()
        
