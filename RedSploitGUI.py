from tkinter import *
import time
import subprocess





def Rust():
    rust_repo = "https://github.com/Simit6155/rust-client.git"
    rust_clone = ["git", "clone", rust_repo]
    subprocess.run(rust_clone)


def Bash():
    bash_repo = "https://github.com/Simit6155/client.bat.git"
    bash_clone = ["git", "clone", bash_repo]
    subprocess.run(bash_clone)


def Powershell():
    powershell_repo = "https://github.com/Simit6155/revshell-pwrshell.git"
    powershell_clone = ["git", "clone", powershell_repo]
    subprocess.run(powershell_clone)


def Python():
    python_repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
    python_clone = ["git", "clone", python_repo]
    subprocess.run(python_clone)


def PythonListener():
    python_listener_repo = "https://github.com/Simit6155/python-listenerd.git"
    python_listener_clone = ["git", "clone", python_listener_repo]
    subprocess.run(python_listener_clone)
    print(Fore.GREEN + "Installed successfully!")


window = Tk()
window.geometry("300x300")
window.title("RedSploit")

icon = PhotoImage(file="logoblue.png")
window.iconphoto(True,icon)
window.config(background="#000b1f")

label = Label(window,
              text="Payloads",
              font=("Arial", 15),
              fg="#3b7df7",
              bg="#000b1f"
             )
label.place(x=101,y=10)

python_button = Button(window,
                       text="Python",
                       font=("Arial", 10),
                       command=Python,
                       fg="#3b7df7",
                       bg="#000b1f"
                      )
python_button.place(x=90,y=50)

python_button = Button(window,
                       text="Rust",
                       font=("Arial", 10),
                       command=Rust,
                       fg="#3b7df7",
                       bg="#000b1f"
                      )
python_button.place(x=160,y=50)

python_button = Button(window,
                       text="Powershell",
                       font=("Arial", 10),
                       command=Powershell,
                       fg="#3b7df7",
                       bg="#000b1f"
                      )
python_button.place(x=70,y=100)

python_button = Button(window,
                       text="Batch",
                       font=("Arial", 10),
                       command=Bash,
                       fg="#3b7df7",
                       bg="#000b1f"
                      )
python_button.place(x=160,y=100)

label = Label(window,
              text="Listeners",
              font=("Arial", 15),
              fg="#3b7df7",
              bg="#000b1f"
             )
label.place(x=101,y=150)

python_button = Button(window,
                       text="Python",
                       font=("Arial", 10),
                       command=PythonListener,
                       fg="#3b7df7",
                       bg="#000b1f"
                      )
python_button.place(x=120,y=190)

window.mainloop()
