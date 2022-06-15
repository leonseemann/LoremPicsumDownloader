import os
import urllib.request
from pathlib import Path


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


url = str(input("Url: "))
nameOfFiles = str(input("Name of files: "))
howMuch = int(input("How much: "))

Path(nameOfFiles).mkdir(parents=True, exist_ok=True)

for x in range(1, howMuch + 1):
    urllib.request.urlretrieve(url, nameOfFiles + "/" + nameOfFiles + "-" + str(x) + ".jpg")
    cls()
    print(str(x / howMuch * 100))