import sys
import math

words = []
nbMots = int(input("Entrer le nombre de mots à comparer"))
count = 0
tabLetterCounter = []

while count < nbMots:
    words.append(input("Entrer vos mots"))
    count += 1

wordCounter = 0
while wordCounter < len(words):

    boucleAllWord = 1
    while boucleAllWord <= len(words):

        if words[wordCounter] == words[(wordCounter + boucleAllWord) % len(words)]:
            print('', end='')
            # print("ignored + " + words[wordCounter] + " " + words[(wordCounter + boucleAllWord) % len(words)])

        else:
            letterCounter = 0
            while words[wordCounter][letterCounter] == words[(wordCounter + boucleAllWord) % len(words)][letterCounter]:
                # print(words[wordCounter][letterCounter], end='')
                letterCounter += 1

            tabLetterCounter.append(letterCounter)
            letterCounter = 0
        boucleAllWord += 1
    # VERIF NB LETTER
    print(words[wordCounter][0: max(tabLetterCounter) + 1])
    tabLetterCounter = []

    boucleAllWord = 0
    wordCounter += 1
