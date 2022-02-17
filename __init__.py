import psutil
import time
from colorama import Fore

VERSION = "1.0.1"
BUILD = "2022-02-17"

def libinfo():
    print(f"{Fore.RED}StrawLib{Fore.RESET} {Fore.GREEN}{VERSION}{Fore.RESET}")
    print(f"{Fore.RED}Build{Fore.RESET} {BUILD}")
    print(f"{Fore.CYAN}Copyright (C) 2022 Strawberry Software Industries{Fore.RESET}")

def version():
    print(f"{VERSION}")

def build():
    print(f"{BUILD}")