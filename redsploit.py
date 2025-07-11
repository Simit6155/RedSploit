import time
import subprocess
import os
from colorama import Fore,init
init(autoreset=True)



def intro():
    print(Fore.CYAN + """
                         ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄   ▄▀▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄    ▄▀▀▀▀▄   ▄▀▀█▀▄    ▄▀▀▀█▀▀▄ 
                        █   █   █ ▐  ▄▀   ▐ █ ▄▀   █ █ █   ▐ █   █   █ █    █    █      █ █   █  █  █    █  ▐ 
                        ▐  █▀▀█▀    █▄▄▄▄▄  ▐ █    █    ▀▄   ▐  █▀▀▀▀  ▐    █    █      █ ▐   █  ▐  ▐   █     
                         ▄▀    █    █    ▌    █    █ ▀▄   █     █          █     ▀▄    ▄▀     █        █      
                        █     █    ▄▀▄▄▄▄    ▄▀▄▄▄▄▀  █▀▀▀    ▄▀         ▄▀▄▄▄▄▄▄▀ ▀▀▀▀    ▄▀▀▀▀▀▄   ▄▀       
                        ▐     ▐    █    ▐   █     ▐   ▐      █           █                █       █ █         
                                   ▐        ▐                ▐           ▐                ▐       ▐ ▐         
                                                       @Redsimit
    """)
    print(Fore.CYAN + """                   
                                           Available Reverse shell clients:
                                             [1] Python     [3] Powershell
                                             [2] Rust       [4] Bash 
                                             
                                           Available Reverse shell Listeners: 
                                                         Python         
         """)


def Python():
    python_repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
    python_clone = ["git", "clone", python_repo]
    subprocess.run(python_clone)
    print(Fore.GREEN + "You need to change the ip in the file")
    print(Fore.GREEN + "Installed successfully!")


def Rust():
    rust_repo = "https://github.com/Simit6155/rust-client.git"
    rust_clone = ["git", "clone", rust_repo]
    subprocess.run(rust_clone)
    print(Fore.GREEN + "You need to change the ip in the file")
    print(Fore.GREEN + "Installed successfully!")


def Powershell():
    powershell_repo = "https://github.com/Simit6155/revshell-pwrshell.git"
    powershell_clone = ["git", "clone", powershell_repo]
    subprocess.run(powershell_clone)
    print(Fore.GREEN + "You need to change the ip in the file")
    print(Fore.GREEN + "Installed successfully!")


def Bash():
    bash_repo = "https://github.com/Simit6155/client.bat.git"
    bash_clone = ["git", "clone", bash_repo]
    subprocess.run(bash_clone)
    print(Fore.GREEN + "You need to change the ip in the file")
    print(Fore.GREEN + "Installed successfully!")


def PythonListener():
    python_listener_repo = "https://github.com/Simit6155/python-listenerd.git"
    python_listener_clone = ["git", "clone", python_listener_repo]
    subprocess.run(python_listener_clone)
    print(Fore.GREEN + "Installed successfully!")

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def kali_update():
    clear_terminal()

    update = ["sudo", "apt", "update", "&&", "sudo", "apt", "upgrade", "-y"]
    subprocess.run(update)

try:
    intro()
    command = ""
    while command != "q":
        command = input(Fore.CYAN + "| > ")

        if command == "1":
            kali_update()
            clear_terminal()
            Python()

        elif command == "2":
            kali_update()
            clear_terminal()
            Rust()

        elif command == "3":
            kali_update()
            clear_terminal()
            Powershell()

        elif command == "4":
            kali_update()
            clear_terminal()
            Bash()

        elif command == "q":
            break

        elif command == "python".lower():
            kali_update()
            clear_terminal()
            PythonListener()

        else:
            print(Fore.GREEN + "[~] Unknown command.")


except KeyboardInterrupt:
    clear_terminal()

    print(Fore.RED + """
[!] Keyboard interrupt detected. Closing in 2""")

    time.sleep(1)

    print(Fore.RED + """
[!] Closing in 1""")

    time.sleep(0.5)

    print(Fore.RED + """
closing program...""")
