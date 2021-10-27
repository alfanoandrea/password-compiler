
from os import system, name

from time import sleep
import os


def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

sleep(0.5)

clear()

import time

print("\u001b[92m██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░")
time.sleep(0.05)
print("\u001b[92m██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗")
time.sleep(0.05)
print("\u001b[92m██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║")
time.sleep(0.05)
print("\u001b[92m██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║")
time.sleep(0.05)
print("\u001b[92m██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝")
time.sleep(0.05)
print("\u001b[92m╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░")
time.sleep(0.05)
print("")
print("\u001b[92m░█████╗░░█████╗░███╗░░░███╗██████╗░██╗██╗░░░░░███████╗██████╗░")
time.sleep(0.05)
print("\u001b[92m██╔══██╗██╔══██╗████╗░████║██╔══██╗██║██║░░░░░██╔════╝██╔══██╗")
time.sleep(0.05)
print("\u001b[92m██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║██║░░░░░█████╗░░██████╔╝")
time.sleep(0.05)
print("\u001b[92m██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║██║░░░░░██╔══╝░░██╔══██╗")
time.sleep(0.05)
print("\u001b[92m╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║███████╗███████╗██║░░██║")
time.sleep(0.05)
print("\u001b[92m░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝")
print("")
time.sleep(0.6)
print("")
print("\u001b[31m▒█▀▀█ █░░█ 　 █▀▀█ █░░ █▀▀ █▀▀█  　 █▀▀█ █▀▀▄ █▀▀▄ 　 █░░ █▀▀█ █▀▀█ █▀▀ █░█ ")
print("\u001b[31m▒█▀▀▄ █▄▄█ 　 █▄▄█ █░░ █▀▀ █▄▄█  　 █▄▄█ █░░█ █░░█ 　 █░░ █░░█ █▄▄▀ █▀▀ ▄▀▄ ")
print("\u001b[31m▒█▄▄█ ▄▄▄█ 　 ▀░░▀ ▀▀▀ ▀░░ ▀░░▀  　 ▀░░▀ ▀░░▀ ▀▀▀░ 　 ▀▀▀ ▀▀▀▀ ▀░▀▀ ▀▀▀ ▀░▀")
print("")
print("")



time.sleep(0.9)
print("\033[93mselect your language\033[0m")
print("1. \033[94mENGLISH\033[0m")
print("2. \033[94mITALIAN\033[0m")
print("3. \033[94mRUSSIAN\033[0m")
language = int(input())
print("")

while (language >= 4 or language <= 0):
	print("\u001b[31mERROR, invalid number")
	for i in range(5):
		print(".", end='')
		time.sleep(0.3)
	time.sleep(0.15)
	print(" ")
	print("\033[93mselect your language:\033[0m")
	print("\033[94m1. ENGLISH\033[0m")
	print("\033[94m2. ITALIAN\033[0m")
	print("\033[94m3. RUSSIAN\033[0m")
	language = int(input())
	print("")


if language==1:
	print("\033[93mwrite your name (lowercase)\033[0m")
	nome = input()
	print("")
	print("\33[93mwrite your surname (lowercase)\033[0m")
	cognome = input()
	print("")
	print("\033[93mwrite your birth year\033[0m")
	anno = input()
elif language==2:
	print("\033[93mscrivi il nome (minuscolo)\033[0m")
	nome = input()
	print("")
	print("\033[93mscrivi il cognome (minuscolo)\033[0m")
	cognome = input()
	print("")
	print("\033[93mscrivi l'anno di nascita\033[0m")
	anno = input()
else:
	print("\033[93mнапишите имя (строчная буква)\033[0m")
	nome = input()
	print("")
	print("\033[93mнапиши фамилию (строчная буква)\033[0m")
	cognome = input()
	print("")
	print("\033[93mнапиши год рождения\033[0m")
	anno = input()


punto = "."
zero = "0"
abbrevanno = anno[-2:]


maiuscnome = (nome.capitalize())
maiusccognome = (cognome.capitalize())
fullmaiuscnome = (nome.swapcase())
fullmaiusccognome = (cognome.swapcase())


print("")
print("")
time.sleep(0.5)
print("\033[91m----------------------------------------------------------------------")


print("")
print("")
if language==1:
	print("\u001b[92mthe file \033[93mpassword.txt \u001b[92mhas been created here: \033[0m", end='')
elif language==2:
	print("\u001b[92mil file \033[93mpassword.txt \u001b[92mè stato creato qui: \033[0m", end='')
else:
	print("\u001b[92mв этой папке был создан файл \033[93mpassword.txt: \033[0m", end='')
directory = os.getcwd()


print(directory, end='')

print("/password.txt")

f = open("password.txt", "w")


combinazioni = [nome, cognome, anno, abbrevanno, ".", maiuscnome, maiusccognome, fullmaiuscnome, fullmaiusccognome]
for i in range(9):
    for j in range(9):
        for k in range(9):
            f.write(combinazioni[i] + combinazioni[j] + combinazioni[k] + "\n")

for l in range(9):
	for m in range(9):
		for n in range(9):
			for o in range(9):
				f.write(combinazioni[l] + combinazioni[m] + combinazioni[n] + combinazioni[o] + "\n")



f.close()


print("")
print("")
print("\033[91m----------------------------------------------------------------------")
print("")
print("")
