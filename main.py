import urllib.request
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


url = str(input("Url: "))
nameOfFiles = str(input("Name of files: "))
howMuch = int(input("How much: "))

cls()

for x in range(1, howMuch + 1):
    urllib.request.urlretrieve(url, nameOfFiles + "-" + str(x) + ".jpg")
    cls()
    print(str(x / howMuch * 100))
