#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# Copyright (c) 2020 Jolanda de Koff | Bulls Eye
# Revised by Nightmare-De9 | GitHub: https://github.com/Nightmare-De9

from __future__ import print_function
try:
    from googlesearch import search
except ImportError:
    print("[Error] Google search module not found.")
    exit()

import sys
import time

class Colors:
    RED = "\33[91m"
    BLUE = "\33[94m"
    ENDC = "\033[0m"

banner = ("""

██████╗  ██████╗ ██████╗ ██╗  ██╗     ██████╗  ██████╗ ██╗
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝     ██╔══██╗██╔═══██╗██║
██║  ██║██║   ██║██████╔╝█████╔╝█████╗██████╔╝██║   ██║██║
██║  ██║██║   ██║██╔══██╗██╔═██╗╚════╝██╔══██╗██║   ██║██║
██████╔╝╚██████╔╝██║  ██║██║  ██╗     ██████╔╝╚██████╔╝██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚═╝

""")

for char in banner:
    print(Colors.RED + char, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

def logger(data, filename):
    with open(f"{filename}.txt", "a") as file:
        file.write(str(data) + "\n")

def dorks():
    while True:
        try:
            dork = input("\n[+] Enter The Dork Search Query: ").strip()
            amount = input("[+] Enter The Number Of Websites To Display: ").strip()
            if not amount.isdigit():
                print("[Error] Please enter a valid number.")
                continue
            amount = int(amount)

            save_output = input("[+] Save the output to a file? (Y/N): ").strip().lower() == 'y'
            filename = input("[~] File name: ") if save_output else None

            counter = 0
            for result in search(dork, tld="com", lang="en", num=amount, stop=amount, pause=2):
                counter += 1
                print(f"[+] {counter}: {result}")
                if save_output:
                    logger(f"{counter}: {result}", filename)

            retry = input("\n[?] Search again? (Y/N): ").strip().lower()
            if retry != 'y':
                break

        except KeyboardInterrupt:
            print("\n[!] User interruption detected.")
            break
        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    dorks()
