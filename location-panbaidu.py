#the location-panbaidu

#load the file
#the start logo
print("")
print("finish the file :location-panbaidu.py...")
print("finish the file :location.js...")
print("finish the file :index.html...")
print("finish the file :index.js...")
print("finish the file : setoollin.py...")
print("")
print("=========================================")

#to import os 
import os
#use linux command to del index.html
#use linux command to del index.js
os.system("rm -f index.html")
os.system("rm -f index.js")
#then copy the file to the content
os.system("cp pan.baidu/index.html ./")
os.system("cp pan.baidu/index.js ./ ")
os.system("cp GPS/location.js ./")

#=================================================
import os
#start the 8080 port
print("start the port on http://127.0.0.1:8080 or http://localhost:8080")
print("")
os.system("python3 -m http.server 8080")