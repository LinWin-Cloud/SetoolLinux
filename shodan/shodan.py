#shodan search 
#run in the linux options system
from operator import truediv
from pickletools import read_uint1

print("")
print("=============================================")
print("           SetoolLinux-->Shodan_Search       ")
print("=============================================")
print("[*]https://www.shodan.io")
print("[*]shodan search ")
#the start logo
print("")
def list():
    print("Server Form https://www.shodan.io/")
    print("List Of The Shodan Search -->")
    print("    -1:Shodan Command")

def back():
    print("enter the key exit t back")
list()
#to run the list 

th = input("enter the command of the shodan_>")

if th == "exit":
    def os1():
        import os
        os.system("python3 ../setoollin.py")
        return True
    os1()

if th == "":
    def os2():
        import os
        os.system("python3 shodan.py") 
        return truediv
    os2()

else:
    def el():
        print(th)
        url = "https://www.shodan.io/"+"search?query="+th
        import webbrowser
        webbrowser.open(url)
        import os
        os.system("python3 shodan.py")
        return True
    el()
