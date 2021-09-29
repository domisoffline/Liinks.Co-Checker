import requests
from colorama import *
from threading import Thread
import time
init()
names = []
good = []
for line in open("names.txt", "r"):
    names.append(line)

def check(number):
    r = requests.get(f"https://liinks.co/{names[int(number)]}")
    if r.url == "https://www.liinks.co/i/not-found?type=NO_USER":
        print(f"{Fore.GREEN}[AVAILABLE] liinks.co/{names[int(number)]}{Fore.RESET}")
        good.append(names[int(number)])
    else:
        print(f"{Fore.RED}[TAKEN] liinks.co/{names[int(number)]}{Fore.RESET}")
bruh = 0



for i in names:
    x = Thread(target=check, args=(bruh,))
    bruh = bruh+1
    x.start()
    time.sleep(0.02)

for i in names:
    x.join()

with open("good.txt", "w+") as f:
    for i in good:
        f.write(i)