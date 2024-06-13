import os
import time
import itertools
import subprocess
import urllib
import urllib.request
import urllib.error
try:
    from tqdm import tqdm
except ImportError:
    subprocess.run(["pip", "install", "tqdm"])
    from tqdm import tqdm
try:
    import webbrowser
except ImportError:
    subprocess.run(["pip", "install", "webbrowser"])
    import webbrowser


debug = False
version = "3.3.1"
versionURL = "https://github.com/alfanoandrea/password-compiler/raw/main/version.txt"
repository = "https://github.com/alfanoandrea/password-compiler"


class Color:
    violet = "\033[35m"
    red = "\u001b[31m"
    cyan = "\u001b[36m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    gray = "\033[90m"
    italic = "\033[3m"
    reset = "\u001b[0m"


def internet():
    try:
        urllib.request.urlopen('https://www.google.com', timeout=5)
        return True
    except urllib.error.URLError:
        return False


class graphics:
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def intro(dynamic):
        graphics.clear()
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
            f"       by alfanowski     {Color.reset}version: {version}\n\n"
        ]
        for i in logo:
            for j in i:
                print(j, end='', flush=True)
                time.sleep(0.01) if dynamic else None
        time.sleep(0.4) if dynamic else None
        input(f"{Color.gray}                [PRESS ENTER]{Color.reset}\n\n") if dynamic else None
        print(f"{Color.red} ------------------------------------------\n{Color.reset}")

    def selezione():
        while True:
            graphics.intro(dynamic = False)
            print(f"{Color.yellow} What do you want to do?\n")
            print(f"  {Color.gray}[{Color.cyan}1{Color.gray}]{Color.reset} Generate")
            print(f"  {Color.gray}[{Color.cyan}2{Color.gray}]{Color.reset} About")
            print(f"  {Color.gray}[{Color.cyan}3{Color.gray}]{Color.reset} Update")
            print(f"\n  {Color.gray}[{Color.red}X{Color.gray}]{Color.red} Exit{Color.reset}\n")
            sel = input(f"{Color.red}  >>  {Color.reset}").lower()
            if sel in ['1', '2', '3', 'x']:
                return sel


def dictionary():
    def getName():
        if debug:
            return "babbo"
        while True:
            graphics.intro(dynamic = False)
            nome = input(f"{Color.yellow} Write the name\n{Color.red}  >>  {Color.reset}")
            if all(char.isalpha() for char in nome) and len(nome) > 1:
                return nome

    def getSurname():
        if debug:
            return "natale"
        while True:
            graphics.intro(dynamic = False)
            cognome = input(f"{Color.yellow} Write the surname\n{Color.red}  >>  {Color.reset}")
            if all(char.isalpha() for char in cognome) and len(cognome) > 1:
                return cognome

    def getNascita():
        if debug:
            return "25122000"
        while True:
            graphics.intro(dynamic = False)
            nascita = input(f"{Color.yellow} Write the birth year (DDMMYYYY)\n{Color.red}  >>  {Color.reset}")
            if len(nascita) == 8 and nascita.isdigit():
                return nascita

    def current(nome, cognome, giorno, mese, anno):
        if debug:
            return True
        while True:
            graphics.intro(dynamic = False)
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
            graphics.intro(dynamic=False)
            file = input(Color.yellow + f" Give a name to the file to generate (without .txt)\n{Color.red}  >>  {Color.reset}")
            if not len(file) > 0:
                return chiediNomeFile()
            return file
        
        def confermaNomeFile(file):
            graphics.intro(dynamic=False)
            print(f"{Color.cyan} FILE {Color.violet}>> {Color.reset}{file}{Color.gray}.txt{Color.reset}\n")
            selezione = input(f"{Color.yellow} Are you sure? {Color.gray}(Y or N)\n{Color.red}  >>  {Color.reset}").lower()
            if selezione not in ('y', 'n'):
                return confermaNomeFile(file)
            return selezione
        
        if debug:
            return "debug.txt"
        file = chiediNomeFile()
        selezione = confermaNomeFile(file)
        if selezione == 'y':
            return file + ".txt"
        else:
            return nomeFile()

    def precisione():
        while True:
            graphics.intro(dynamic = False)
            print(f"{Color.yellow} Enter the file size:")
            print(f"{Color.green}  1){Color.reset} Small {Color.gray}{Color.italic} more than 15 thousand passwords")
            print(f"{Color.green}  2){Color.reset} Big {Color.gray}{Color.italic} more than 500 thousand passwords")
            print(f"{Color.green}  3){Color.reset} Huge {Color.gray}{Color.italic} more than 19 million passwords\n")
            sel = input(f"{Color.red}  >>  {Color.reset}")
            if sel.isnumeric() and 1 <= int(sel) <= 3: 
                return int(sel) + 3

    def generazione(file, combinazioni, dimensione):
        graphics.intro(dynamic=False)
        print(f"{Color.gray} Data calculation... {Color.reset}")
        totale = 0
        for length in range(2, dimensione):
            totale += len(list(itertools.permutations(combinazioni, length)))
        graphics.intro(dynamic=False)
        cont = 0
        print(Color.green, end='')
        with tqdm(total=totale, desc='', unit='B', leave=False, bar_format='  {percentage:3.0f}% |{bar}|  ', ncols=35) as pbar:
            with open(file, 'w') as f:
                for length in range(1, dimensione):
                    for combo in itertools.permutations(combinazioni, length):
                        password = ''.join(combo)
                        if len(password) >= 6 and any(name in password.lower() for name in combinazioni[:6]):
                            f.write(password + "\n")
                            cont += 1
                            pbar.update(1)
        print(Color.reset, end='')
        return cont
    
    def fine(file, paroleGenerate):
        graphics.intro(dynamic = False)
        print(f" The file {Color.green}{file}{Color.reset} has been created!\n")
        input(f" Lines: {Color.cyan}{paroleGenerate}{Color.reset}\n\n")
        graphics.clear()

    def folder():
        if not os.path.exists("dictionaries"):
            os.makedirs("dictionaries")

    while True:
        nome = getName().lower()
        cognome = getSurname().lower()
        nascita = getNascita()
        giorno = str(nascita[:2])
        mese = str(nascita[2:4])
        anno = str(nascita[4:])
        if current(nome, cognome, giorno, mese, anno):
            break
    file = "dictionaries/" + nomeFile()  
    combinazioni = [
        nome, cognome, 
        nome.capitalize(), cognome.capitalize(),
        nome.upper(), nome.upper(), 
        giorno, mese, anno, anno[-2:], 
        '.', ',', '?', '@', '#', '_', '-', '!', '$', '%', '[', ']', '(', ')'
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ]
    folder()
    paroleGenerate = str(generazione(file, combinazioni, precisione()))
    fine(file, paroleGenerate)


def about():
    def openLink(browser = 'default'):
        url = 'https://github.com/alfanoandrea/password-compiler/blob/main/README.md'  
        try:
            if browser == 'default':
                webbrowser.open(url)
            else:
                browser_controller = webbrowser.get(browser)
                browser_controller.open_new(url)
            print(f"{Color.green} Link opened successfully!{Color.reset}")
        except Exception as e:
            print(f"{Color.red} Error opening link!{Color.reset}")

    def info():
        if internet():
            openLink()
        else:
            try:
                with open("README.md", 'r') as file:  
                    if os.name == 'nt':
                        os.system("type README.md")
                    else:
                        os.system("cat README.md")            
            except FileNotFoundError:
                print(f"{Color.red} File 'README.md' not found{Color.reset}")
            except IOError:
                print(f"{Color.red} Error reading the file 'README.md'.{Color.reset}")
    
    graphics.intro(dynamic = False)
    info()
    input("\n\n")


def update():
    graphics.intro(dynamic = False)
    def checkVersion():
        try:
            with urllib.request.urlopen(versionURL, timeout=5) as f:
                latestVersion = f.read().decode('utf-8').strip()    
            if version != latestVersion:
                print(f"{Color.yellow} A new version {Color.green}({latestVersion}){Color.yellow} is available. {Color.gray}Updating...{Color.reset}\n")
                performUpdate()
            else:
                print(f"{Color.gray} The script is already up to date!{Color.reset}")
        except urllib.error.URLError as e:
            print(f"{Color.red} Error checking version!{Color.reset}")
        except Exception as e:
            print(f"{Color.red} Error during version check!{Color.reset}")

    def performUpdate():
        try:
            subprocess.run(["git", "pull", "origin", "main"])
            print(f"{Color.green} Update completed! Please run the script again.{Color.reset}")
            exit()
        except Exception as e:
            print(f"{Color.red} Error updating the script!{Color.reset}")

    if internet():
        checkVersion()
    else:
        print(f"{Color.red} No internet connection!{Color.reset}")
    input('\n')


#   M - A - I - N 
if __name__ == "__main__":
    with open("version.txt", 'w') as f:
        f.write(version)
    f.close()
    if not debug:
        graphics.intro(dynamic = True)
    while True:
        opt = graphics.selezione()
        if opt == '1':
            dictionary()
        elif opt == '2':
            about()
        elif opt == '3':
            update()
        elif opt == 'x':
            print("\n\n")
            break
            

'''
    In realtà ho creato questo programma perché mi stavo annoiando,
    poi ho visto che stava uscendo qualcosa di carino e allora ho
    continuato a lavoraci...
'''    

