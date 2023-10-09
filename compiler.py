import os
import time
import sys

class Color:
    violet = "\033[35m"
    red = "\u001b[31m"
    cyan = "\u001b[36m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    fucsia = "\u001b[35;1m"
    gray = "\033[90m"
    reset = "\u001b[0m"


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def intro(cascata):
    clear()
    if (cascata):
        time.sleep(0.1)
    print(Color.green + "   _____                             _ ")
    if (cascata):
        time.sleep(0.1)
    print("  |  _  |___ ___ ___ _ _ _ ___ ___ _| |")
    if (cascata):
        time.sleep(0.1)
    print("  |   __| .'|_ -|_ -| | | | . |  _| . |")
    if (cascata):
        time.sleep(0.1)
    print("  |__|  |__,|___|___|_____|___|_| |___|\n")
    if (cascata):
        time.sleep(0.1)
    print("     _____               _ _         ")
    if (cascata):
        time.sleep(0.1)
    print("    |     |___ _____ ___|_| |___ ___ ")
    if (cascata):
        time.sleep(0.1)
    print("    |   --| . |     | . | | | -_|  _|")
    if (cascata):
        time.sleep(0.1)
    print("    |_____|___|_|_|_|  _|_|_|___|_|  ")
    if (cascata):
        time.sleep(0.1)
    print("                    |_|            \n")
    if (cascata):
        time.sleep(0.1)
    testo1 = Color.violet + "\n      by alfanowski    " + Color.reset + "version: 3.0 \n\n\n"
    if (cascata):
        for carattere in testo1:
            sys.stdout.write(carattere)
            sys.stdout.flush()
            time.sleep(0.05)
    else:
        print(testo1)
    if (cascata):
        time.sleep(0.2)
        testo2 = Color.gray + "\t      [Press Enter]\n" + Color.reset
        for carattere in testo2:
            sys.stdout.write(carattere)
            sys.stdout.flush()
            time.sleep(0.1)
        input()
    print(Color.red + "------------------------------------------\n" + Color.reset)


def getName():
    while True:
        intro(cascata = False)
        print(Color.yellow + "Write the name")
        nome = input(Color.red + " >> " + Color.reset)
        if all(char.isalpha() for char in nome) and len(nome) > 1:
            break
    return nome


def getSurname():
    while True:
        intro(cascata = False)
        print(Color.yellow + "Write the surname")
        cognome = input(Color.red + " >> " + Color.reset)
        if all(char.isalpha() for char in cognome) and len(nome) > 1:
            break
    return cognome


def getNascita():
    while True:
        intro(cascata = False)
        print(Color.yellow + "Write the birth year (DDMMYYYY)")
        nascita = str(input(Color.red + " >> " + Color.reset))
        if len(nascita) == 8 and nascita.isdigit():
            break
    return nascita


def correct(nome, cognome, giorno, mese, anno):
    while True:
        while True:
            intro(cascata = False)
            print(Color.cyan + "         NAME " + Color.violet + "--> " + Color.reset + nome.capitalize())
            print(Color.cyan + "      SURNAME " + Color.violet + "--> " + Color.reset + cognome.capitalize())
            print(Color.cyan + "   BIRTH DATE " + Color.violet + "--> " + Color.reset + giorno + "/" + mese + "/" + anno)
            print("\nAre you sure? (Y or N)")
            selezione = input(Color.red + " >> " + Color.reset)
            if selezione == 'y' or selezione == 'Y' or selezione == 'n' or selezione == 'N':
                break
        if selezione == 'y' or selezione == 'Y':
            return True
        else:
            return False
        

def nomeFile():
    while True:
        while True:
            intro(cascata = False)
            print(Color.yellow + "Give a name to the file to generate (without .txt)" + Color.reset)
            file = input(Color.red + " >> " + Color.reset)
            if len(file) > 0:
                break
        while True:
            intro(cascata = False)
            print(Color.cyan + "         FILE " + Color.violet + "--> " + Color.reset + file + Color.gray + ".txt" + Color.reset)
            print("\nAre you sure? (Y or N)")
            selezione = input(Color.red + " >> " + Color.reset)
            if selezione == 'y' or selezione == 'Y' or selezione == 'n' or selezione == 'N':
                break
        if selezione == 'y' or selezione == 'Y':
            return file + ".txt"


def generazione(file, combinazioni):
    count = 0
    with open(file, 'w') as f:
        for i in range(len(combinazioni)):
            for j in range(len(combinazioni)):
                if i != j:
                    f.write(combinazioni[i] + combinazioni[j] + "\n")
                    count += 1

        for i in range(len(combinazioni)):
            for j in range(len(combinazioni)):
                for k in range(len(combinazioni)):
                    if i != j and i != k and j != k:
                        f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + "\n")
                        count += 1

        for i in range(len(combinazioni)):
            for j in range(len(combinazioni)):
                for k in range(len(combinazioni)):
                    for o in range(len(combinazioni)):
                        if i != j and i != k and i != o and j != k and j != o and k != o:
                            f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + combinazioni[o] + "\n")
                            count += 1

        for i in range(len(combinazioni)):
            for j in range(len(combinazioni)):
                f.write(combinazioni[i] + combinazioni[j] + "\n")
                count += 1

        for i in range(len(combinazioni)):
            for j in range(len(combinazioni)):
                for k in range(len(combinazioni)):
                    f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + "\n")
                    count += 1

        for i in range(len(combinazioni)):
            for j in range(len(combinazioni)):
                for k in range(len(combinazioni)):
                    for o in range(len(combinazioni)):
                        f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + combinazioni[o] + "\n")
                        count += 1
    return count

    
def fine(file, paroleGenerate):
    intro(cascata = False)
    print("The file " + Color.green + file + Color.reset + " has been created!")
    print("\nLines: " + Color.cyan + paroleGenerate + Color.reset)
    input()
    clear()


# main

intro(cascata = True)

while True:
    nome = getName().lower()
    cognome = getSurname().lower()
    nascita = getNascita()
    giorno = str(nascita[:2])
    mese = str(nascita[2:4])
    anno = str(nascita[4:])
    if correct(nome, cognome, giorno, mese, anno):
        break

file = nomeFile()  
upperNome = nome.capitalize()
upperCognome = cognome.capitalize()
fullUpperNome = nome.swapcase()
fullUpperCognome = cognome.swapcase()
abbrevanno = anno[-2:]
combinazioni = [nome, cognome, fullUpperCognome, fullUpperNome, giorno, mese, anno, abbrevanno, upperNome, upperCognome]
combinazioni.extend(['.', ',', '?', '@', '#', '_', '-'])
combinazioni.extend(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
intro(cascata = False)
for i in range(6):
        sys.stdout.write('\r       Loading' + '.' * i)
        sys.stdout.flush()
        time.sleep(0.5)
paroleGenerate = str(generazione(file, combinazioni))
fine(file, paroleGenerate)
