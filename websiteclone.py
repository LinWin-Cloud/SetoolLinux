#the web site clone file
#use the html with iframe to clone the web site


def load():
    print("")
    print("")
    print("finish the file websiteclone.py...")
    print("finish the file set.py...")
    print("finish the file setoollin.py...")
    print("finish the file index.html...")

#to run the load()
load()

print("")
print("")

print("1:Html5 clone")
print("")
ch = input("Chose The Content_>")

if ch == "1":
    url = input("Enter The Clone Url:")

    surl = "'" + url + "'"
    import os
    os.system("rm -f index.html")

    print("")
    print("loading...")
    print("clone the web site now...")
    print("")

    with open("index.html","a") as f:
    #write the html file
        f.write("<html>")
        f.write("<head>")
        f.write("</head>")
        f.write("<body>")
        f.write("<iframe style='width:100%;height:100%;background-color:aliceblue' src="+surl+"></iframe")
        f.write("</body>")
    f.close()

    import os
    print("start the http port 8080 on http://localhost:8080 and http://127.0.0.1:8080")
    print("")
    os.system("python3 -m http.server 8080")
    #start the 8080 port

if ch == "exit":
    import os
    os.system("python3 setoollin.py")
else :
    import os
    os.system("python3 websiteclone.py")