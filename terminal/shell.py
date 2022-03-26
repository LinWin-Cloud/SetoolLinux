
from os import system


a =input("Shell_>")
if a == "#exit" :
    import os
    os.system(a)
    os,system("python3 terminal/terminal.py")

else:
    import os
    os.system(a)
    os.system("python3 terminal/shell.py")