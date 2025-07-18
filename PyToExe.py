import subprocess
import time
from colorama import Fore,init
init(autoreset=True)



def InstallRequirements():
    InstallReq = ["pip", "install", "pyinstaller"]
    subprocess.run(InstallReq)

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


try:
    NameOfFile = input(Fore.GREEN + "Enter File Name: ")
    IsLogo = input(Fore.GREEN + "Is there a logo? (Y/N): ")

    if IsLogo.upper() == "Y":
        try:
            InstallRequirements()
            clear_terminal()

            IconName = input(Fore.GREEN + "Icon Name: ")
            CompileWLogo = ["pyinstaller", "--onefile", "--icon", IconName, NameOfFile]
            subprocess.run(CompileWLogo)
            print(Fore.GREEN + "Py to Exe completed successfully!")

        except:
            print(Fore.RED + "Error ocurred, Try again.")


    elif IsLogo.upper() == "N":
        try:
            InstallRequirements()
            clear_terminal()

            CompileWOLogo = ["pyinstaller", "--onefile", NameOfFile]
            print(Fore.GREEN + "Py to Exe completed successfully!")

        except:
            print(Fore.RED + "Error ocurred, Try again.")

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
