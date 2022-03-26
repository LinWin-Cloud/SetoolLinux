#use python3 to finish the optioning
#auther : window observer
#file name : terminal.py
#making in china
from binhex import openrsrc
from curses import intrflush
from distutils.util import strtobool
from operator import truediv
from pdb import line_prefix
from re import I
from socket import INADDR_ALLHOSTS_GROUP
from traceback import print_tb


inputth = input("LinWin Terminal For Linux_>")

if inputth == "exit" :
    import os
    os.system("python3 setoollin.py")

if inputth == "terminal" :
    print("===================================")
    print("Terminal")
    print("   -Vistion : 1.0")
    print("   -For System : Linux")
    print("   -Command : Linux command , other")
    print("===================================")
    import os
    os.system("python3 terminal/terminal.py")

#users can us this command to go to the web page
if inputth == "website -goto" :
    url = input("Enter The Url_>")
    import webbrowser
    webbrowser.open(url)
    import os
    os.system("python3 terminal/terminal.py")
    #===============================================================
    #users can use this command to change the web page

if inputth == "port start":
    startport = input("The Port_>")
    import os
    command = "python3 -m http.server"+" "+startport
    os.system(command)
    os.system("python3 terminal/terminal.py")

if inputth == "shodan_search":
    print("use shodan_search")
    import webbrowser
    webbrowser.open("https://www.shodan.io")
    #users can goto https://www.shodan.io to get some information
    import os
    os.system("python3 terminal/terminal.py")

if inputth == "setool --chat software" :
    print("SetoolLinux-->")
    print("[*]These Software is advice you to use!")
    print("")
    print("   -1:Wechat  download=https://www.weixin.com/")
    print("   -2:QQ      download=https://im.qq.com/")
    print("==============================================")
    import os
    os.system("python3 terminal/terminal.py")

if inputth == "setool -all":
    print("command:"+inputth)
    #to show the set tool 
    print("Setool -->")
    print("   -bring your own ")
    print("     -1:Setool masterplate")
    print("     -2:Get location masterplate")
    print("     -3:Get Ip masterplate")
    print("     -4:Shodan_search formwork")
    print("     -5:Website clone")
    print("     -6:Virus Attack")
    print("     -7:Terminal")
    print("     -8:Web Console")
    print("   -other->")
    print("[*]Other you can to have a think")
    print("     -1:Github      https://github.com")
    print("     -2:metasploit  https://www.metasploit.com")
    import os
    os.system("python3 terminal/terminal.py")

if inputth == "add command":
    print("Input : 'exit' to exit")
    inth = input("Input The command's name_>")
    if inth == "exit" :
        import os
        os.system("python3 terminal/terminal.py")
    else:
        print("Command="+inth)
        print("You can write the shell script or python's code")
        con = input("Chose Shell Script or Python_>")
        if con == "1" :
            print("shell")
            with open("terminal/terminal.py","a") as write:
                write.write("\r\n")
                write.write("\r\n")
                write.write('if inputth =='+'"'+inth+'"' + ":")
                write.write("\r\n")
                write.write("    import os\r\n")
            a = 1
            while a == 1:
                code = input("Shell Script_>")
                codefile = inth + ".txt"
                with open(codefile,"a") as f:
                    f.write(code+"\r")
                with open("terminal/terminal.py","a") as f:
                    f.write("    os.system('"+code+"')"+"\r")
                    f.write("    os.sytem('python3 terminal/terminal.py')\r")

        if con == "2":
            print("python")
            with open("terminal/terminal.py","a") as f:
                f.write("\r\n")
            a1 = 'if inth ==' + '"' + inth + '"' + ":"+"\r"
            codefile = inth
            with open(codefile,"a") as f:
                f.write(a1)
            with open("terminal/terminal.py","a") as f:
                f.write(a1)
                a = 1
            while a == 1 :
                code = input("Python Script_>")
                file = inth
                wcode = "    " + code
                with open(file,"a") as f:
                    f.write(wcode + "\r")
                f.close()
                with open("terminal/terminal.py","a") as f:
                    f.write(wcode)
                if code == "#":
                    with open("terminal/terminal.py","a") as f:
                        f.write("\r")
                        f.write("    os.sytem('python3 terminal/terminal.py')\r")
                        f.write("    print('')\r")
                    import os
                    os.system("python3 terminal/terminal.py")
        else :
            import os
            os.system("python3 terminal/terminal.py")
#
if inputth == "shell" :
    import os
    os.system("python3 terminal/shell.py")
