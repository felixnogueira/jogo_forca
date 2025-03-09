def printSecretWord(word, hits):
    guess = ""
    for letter in word:
        if letter in hits:
            guess += letter
        else:
            guess += "\u2588"
    print(f"ADIVINHE: ({len(word)} letras): ")
    for letter in guess:
        print(f"{letter} ", end="")
    print()

    return guess

def printHangman(misses):
    score = 1000
    print("X==:==")
    print("X  :  ")
    if misses >= 1:
        print("X  O  ")
        score = 800
    else: print("X")

    line2 = ""
    if misses == 2:
        line2 = "  |  "
        score = 600
    elif misses == 3:
        line2 = " /| "
        score = 400
    elif misses >= 4:
        line2 = " /|\ "
        score = 200
    print(f"X{line2}")

    line3 = ""
    if misses == 5:
        line3 = " / "
        score = 100
    elif misses >= 6:
        line3 = " / \ "
        score = 0
    print(f"X{line3}")

    print(f"X\n=======")
    return score
    
        
