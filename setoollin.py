#the setoollin for linux 
#language:English

#the start logo


#==================================================
from http.client import IM_USED
from re import I

import time
time.sleep(0.5)
print("")
print("")
print("""
    [*]===================================[*]
                  -SetoolLinux-
                 For Linux 2022
        https://github.com/LinWin-Cloud
    [*]===================================[*]
""")
print("")
print("[*]The Vistion For Linux 2022")
print("[*]Social Engineering Tool Linux")
print("[*]Shodan Server , you can more information form https://www.shodan.com")
print("[*]Making In China")
print("")
print("")
#==================================================
#write the date to the date.txt
with open("date.txt","a") as f :
    f.write("-----------start the setoollin.py")
f.close()


with open("date.txt","a") as f:
    f.write("/N")
    f.write("----the main procedure")
f.close()

import time
#end the write
#for to view the content
con1 = "Social Engineering    (use pishing site to attack)" #finish
con2 = "Virus Attack    (use virus to attack)" #finish
con3 = "Web Site Clone    (use Html5 to clone a website)" #finish 
con4 = "Global Positioning    (use GPS to get location)" #finish 
con5 = "Get IP Adress    (use Js and Html5 to get IP Adress)" #finish 
con6 = "The Help    (tell you how to optioning)" #finish
con7 = "Shodan Search    (use Shodan's command to get information)" #finish
print("SetoolLinux --> Main Module")
print("")
print("-1:"+con1)
print("-2:"+con2)
print("-3:"+con3)
print("-4:"+con4)
print("-5:"+con5)
print("-6:"+con6)
print("------------------------------------")
print("SetoolLinux --> Auxiliary Module")
print("")
print("-7:"+con7)
con8 = "Terminal (use Terminal to auxiliary your attack)" #finish
print("-8:"+con8)
print("------------------------------------")
print("SetoolLinux --> Web Attack Module")
print("")
print("-9:"+"Web Console  (use web console to attack)") #finish 
print("------------------------------------")
print("[*]Input 'exit' to exit")
#to enter the content


a=input("__Pass The Content>")



if a == "1":
    print("Chose The Content:"+a)
    print("content:"+con1)
    import os
    os.system("python3 set.py")
    #if the file in the same place can use the 'os.system'


if a == "2":
    def os2():
        print("Chose The Content:"+a)
        print("content:"+con2)
        import os
        os.system("python3 virusattack.py")
        return True
    os2()
        #if the users enter the 2 key then goto  "virusattack page"
        #use linux os

if a == "3":
    print("Chose The Content:"+a)
    print("content:"+con3)
    import os
    os.system("python3 websiteclone.py")
    #start the websiteclone.py
    #the function a = 1 or 2 or 3 or 4
    #but don't = onther

if a == "4":
    print("Chose The Content:"+a)
    print("content:"+con4)
    import os
    os.system("python3 GPS.py")
    #use GPS 

if a == "5":
    print("Chose The Content:"+a)
    print("content:"+con5)
    import os
    os.system("python3 getip.py")

if a == "6" :
    print("Chose The Content:"+a)
    print("content:"+con5)
    import os
    os.system("python3 help.py")

if a == "7":
    import os
    os.system("python3 shodan/shodan.py")
    #shodan search 
    #

if a == "8" :
    print("use terminal")
    #this terminal use python 
    #and you can run some linux command on the linwin terminal for linux
    #and you also can run some anther windows command and other useful command
    import os
    os.system("python3 terminal/start.py")

if a == "9" :
    print("use Web Console")
    import webbrowser
    webbrowser.open("ter.html")
    #start the web console to attack
    import os
    os.system("python3 setoollin.py")
    #attacker can use web console to send sms , send e-mail , goto web site , tel and so on 

if a == "exit" :
    import os
    os.system("bash") #to exit the setoolLinux

else :
    import os
    os.system("python3 setoollin.py")
