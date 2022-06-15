import os
import urllib.request
from pathlib import Path

from tqdm import tqdm


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


url = str(input("Url: "))
nameOfFiles = str(input("Name of files: "))
howMuch = int(input("How much: "))

Path(nameOfFiles).mkdir(parents=True, exist_ok=True)

pictureCount = len(os.listdir(nameOfFiles))

for x in tqdm(range(1, howMuch + 1)):
    urllib.request.urlretrieve(url, nameOfFiles + "/" + nameOfFiles + "-" + str(pictureCount + x) + ".jpg")
