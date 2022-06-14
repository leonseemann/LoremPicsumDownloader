import urllib.request
import os

clear = lambda: os.system('cls')

url = str(input("Url: "))

wie_viele = int(input("Wie viele bilder? "))

for x in range(1, wie_viele + 1):
    urllib.request.urlretrieve(url, "hintergrund-" + str(x) + ".jpg")
    clear()
    print(str(x / wie_viele * 100))
