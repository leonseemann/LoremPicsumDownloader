import urllib.request
import os

clear = lambda: os.system('cls')

url = str(input("Url: "))

howMuch = int(input("Wie viele bilder? "))

for x in range(1, howMuch + 1):
    urllib.request.urlretrieve(url, "background-" + str(x) + ".jpg")
    clear()
    print(str(x / howMuch * 100))
