GNU nano 6.3                                                     Doxpone.py
import requests
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")


banner = BLUE + '''
╭━━━┳━━━┳━╮╭━╮╭━━━┳━━━┳━╮╱╭┳━━━╮
╰╮╭╮┃╭━╮┣╮╰╯╭╯┃╭━╮┃╭━╮┃┃╰╮┃┃╭━━╯
╱┃┃┃┃┃╱┃┃╰╮╭╯╱┃╰━╯┃┃╱┃┃╭╮╰╯┃╰━━╮
╱┃┃┃┃┃╱┃┃╭╯╰╮╱┃╭━━┫┃╱┃┃┃╰╮┃┃╭━━╯
╭╯╰╯┃╰━╯┣╯╭╮╰╮┃┃╱╱┃╰━╯┃┃╱┃┃┃╰━━╮
╰━━━┻━━━┻━╯╰━╯╰╯╱╱╰━━━┻╯╱╰━┻━━━╯
'''
print(banner)


print("\033[33m--------------------------------------")
print(YELLOW+"Autor    : TiagoXxYt")
print("--------------------------------------")
print("INSTAGRAM: Tiaguito_004")
print("--------------------------------------")
print(GREEN+"escribe el numero de telefono junto\ncon el prefijo, ejemplo: +54911845076\n")

api_key = '48d04397c36551c48eced6a4304b66f6'

number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))
