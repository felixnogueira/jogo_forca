import artwork as art
import fileHandler as fh
from random import choice


def playGame():
    listOfWords = list()
    file = fh.openReadFile("palavras.txt")
    for line in file:
        word = line.strip()
        listOfWords.append(word)
    chosenWord = choice(listOfWords)

    for x in range(50):
        print()

    typed = []
    hits = []
    misses = 0

    playerName = input("Digite seu nome: ")

    while True:

        guess = art.printSecretWord(chosenWord, hits)

        if guess == chosenWord:
            print("Você venceu!")
            break

        playerTry = input("Digite uma letra: ").lower().strip()
        if playerTry in typed:
            print("Você já tentou essa letra!")
            continue
        else:
            typed.append(playerTry)
            if playerTry in chosenWord:
                hits += playerTry
            else:
                misses += 1

        for x in range(50):
            print()
        
        score = art.printHangman(misses)

        if misses == 6:
            print("Enforcado!")
            print(f"A palavra secreta era: {chosenWord}.")
            break
        
    fh.insertScore("score.txt", playerName, score)
    
    
        
        

