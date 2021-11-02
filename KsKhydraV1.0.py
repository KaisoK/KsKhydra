import requests

f = open("/home/kaisok/Documentos/Python/KsKhydra/wordlist.txt", "r",encoding="latin-1")
user = f.readlines()

f.close()

passwd = user

for x in user:

    for y in passwd:

        x = x.strip("\n")
        y = y.strip("\n")
        
        print("Testing: {}:{}".format(x.strip("\n"),y.strip("\n")),end="\r")
        
        req = requests.get("http://{}:{}@127.0.0.1/host1/index.html".format(x,y))
        
        if req.status_code == 200:
            
            print("#"*40,end="\r\n")
            print("User: {}\nPassword: {}".format(x,y),end="\n")
            print("#"*40,end="\r\n")
