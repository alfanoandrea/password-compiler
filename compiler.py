import os
import time
import sys
import itertools
try:
    from tqdm import tqdm
except ImportError:
    import subprocess
    subprocess.run(["pip", "install", "tqdm"])
    from tqdm import tqdm


class Color:
    violet = "\033[35m"
    red = "\u001b[31m"
    cyan = "\u001b[36m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    fucsia = "\u001b[35m"
    gray = "\033[90m"
    italic = "\033[3m"
    reset = "\u001b[0m"


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def intro(dynamic):
    clear()
    logo = [
        Color.green,
        "    _____                             _ \n",
        "   |  _  |___ ___ ___ _ _ _ ___ ___ _| |\n",
        "   |   __| .'|_ -|_ -| | | | . |  _| . |\n",
        "   |__|  |__,|___|___|_____|___|_| |___|\n",
        "      _____               _ _         \n",
        "     |     |___ _____ ___|_| |___ ___ \n",
        "     |   --| . |     | . | | | -_|  _|\n",
        "     |_____|___|_|_|_|  _|_|_|___|_|  \n",
        "                     |_|            \n\n",
        Color.violet, Color.italic,
        f"       by alfanowski     {Color.reset}version: 3.1\n\n"
    ]
    for i in logo:
        for j in i:
            print(j, end='', flush=True)
            time.sleep(0.01) if dynamic else None
    time.sleep(0.4) if dynamic else None
    input(f"{Color.gray}                [PRESS ENTER]{Color.reset}\n\n") if dynamic else None
    print(f"{Color.red} ------------------------------------------\n{Color.reset}")


def getName():
    while True:
        intro(dynamic = False)
        nome = input(f"{Color.yellow} Write the name\n{Color.red}  >>  {Color.reset}")
        if all(char.isalpha() for char in nome) and len(nome) > 1:
            return nome


def getSurname():
    while True:
        intro(dynamic = False)
        cognome = input(f"{Color.yellow} Write the surname\n{Color.red}  >>  {Color.reset}")
        if all(char.isalpha() for char in cognome) and len(cognome) > 1:
            return cognome


def getNascita():
    while True:
        intro(dynamic = False)
        nascita = input(f"{Color.yellow} Write the birth year (DDMMYYYY)\n{Color.red}  >>  {Color.reset}")
        if len(nascita) == 8 and nascita.isdigit():
            return nascita


def current(nome, cognome, giorno, mese, anno):
    while True:
        intro(dynamic = False)
        print(f"{Color.cyan}          NAME {Color.violet}>>  {Color.reset}{nome.capitalize()}")
        print(f"{Color.cyan}       SURNAME {Color.violet}>>  {Color.reset}{cognome.capitalize()}")            
        print(f"{Color.cyan}    BIRTH DATE {Color.violet}>>  {Color.reset}{giorno}/{mese}/{anno}\n")    
        selezione = input(f"{Color.yellow} Are you sure? {Color.gray}(Y or N)\n{Color.red}  >>  {Color.reset}").lower()
        if selezione == 'y':
            return True
        elif selezione == 'n':
            return False
        

def nomeFile():
    def chiediNomeFile():
        intro(dynamic=False)
        file = input(Color.yellow + f" Give a name to the file to generate (without .txt)\n{Color.red}  >>  {Color.reset}")
        if not len(file) > 0:
            return chiediNomeFile()
        return file
    def confermaNomeFile(file):
        intro(dynamic=False)
        print(f"{Color.cyan} FILE {Color.violet}>> {Color.reset}{file}{Color.gray}.txt{Color.reset}\n")
        selezione = input(f"{Color.yellow} Are you sure? {Color.gray}(Y or N)\n{Color.red}  >>  {Color.reset}").lower()
        if selezione not in ('y', 'n'):
            return confermaNomeFile(file)
        return selezione
    file = chiediNomeFile()
    selezione = confermaNomeFile(file)
    if selezione == 'y':
        return file + ".txt"
    else:
        return nomeFile()


def precisione():
    while True:
        intro(dynamic = False)
        print(f"{Color.yellow} Enter the file size:")
        print(f"{Color.green}  1){Color.reset} Small {Color.gray}{Color.italic} more than 10 thousand passwords")
        print(f"{Color.green}  2){Color.reset} Normal {Color.gray}{Color.italic} more than 350 thousand passwords")
        print(f"{Color.green}  3){Color.reset} Big {Color.gray}{Color.italic} more than 11 million passwords\n")
        sel = input(f"{Color.red}  >>  {Color.reset}")
        if sel.isnumeric() and 1 <= int(sel) <= 3: 
            return int(sel) + 3


def generazione(file, combinazioni, dimensione):
    intro(dynamic = False)
    print (f"{Color.gray} Data calculation...   {Color.reset}")
    totale = 0
    for length in range(2, dimensione):
        totale += len(list(itertools.permutations(combinazioni, length)))
    intro(dynamic = False)
    cont = 0
    print(Color.green, end='')
    with tqdm(total = totale, desc = '', unit = 'B', leave = False, bar_format = '  {percentage:3.0f}% |{bar}|  ', ncols = 35) as pbar:
            with open(file, 'w') as f:
                for length in range(2, dimensione): 
                    for combo in itertools.permutations(combinazioni, length):
                        if len(''.join(combo)) >= 6:
                            f.write(''.join(combo) + "\n")
                            cont += 1
                            pbar.update(1)
    print(Color.reset, end='')
    return cont

    
def fine(file, paroleGenerate):
    intro(dynamic = False)
    print(f" The file {Color.green}{file}{Color.reset} has been created!\n")
    input(f" Lines: {Color.cyan}{paroleGenerate}{Color.reset}\n\n")
    clear()


# main
if __name__ == "__main__":
    intro(dynamic = True)
    while True:
        nome = getName().lower()
        cognome = getSurname().lower()
        nascita = getNascita()
        giorno = str(nascita[:2])
        mese = str(nascita[2:4])
        anno = str(nascita[4:])
        if current(nome, cognome, giorno, mese, anno):
            break
    file = nomeFile()  
    combinazioni = [
        nome, cognome, 
        nome.capitalize(), cognome.capitalize(),
        nome.swapcase(), nome.swapcase(), 
        giorno, mese, anno, anno[-2:], 
        '.', ',', '?', '@', '#', '_', '-', '!',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ]
    paroleGenerate = str(generazione(file, combinazioni, precisione()))
    fine(file, paroleGenerate)

