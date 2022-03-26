#get ip file 
#========================
print("finish the file : getip.py...")
print("finish the file : set.py...")
print("finish the file : setoollin.py")
print("finish the file : IP.html")


def logo():
    print("")
    print("")
    print("===============================")
    print("SetoolLinux-->Get IP Adress")
    print("===============================")
    print("")
    print("")

def list():
    print("1:-Blank File")
    print("--------------------------")
    print("Enter The Key 2 To Back")

logo()

list()

th = input("SetoolLinux>>Get IP Adress_>")

if th == "method get ip 1":
    import os
    os.system("rm -f index.html")
    os.system("rm -f index.js")
    os.system("rm -f location.js")
    os.system("cp formwork/IP/index.html ./")
    print("start the port 8080 on http://127.0.0.1 and http://localhost:8080")
    import os
    os.system("python3 -m http.server 8080")

if th == "2" :
    import os
    os.system("python3 setoollin.py")
else :
    print("The Input Null")
    import os
    os.system("python3 getip.py")