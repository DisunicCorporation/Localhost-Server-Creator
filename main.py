import random
import sys
from multiprocessing.connection import wait
import os
from DIOS.DIOS_Colored import cl
from DIOS.res import socketserver
from DIOS.res import webbrowser
from DIOS.res.http import server as sv
# 
backCl  =     cl("#2196f3")
helpcl  =     cl("#31ff79") 
inputCl =     cl("#20b2aa")
urlCl   =     cl("#ff9800")
pathCl  =     cl("#3f51b5")
pyvCl   =     cl("#e91e63")
# 
def logo():
    print(backCl+"""

    ░█▀▀▄ ▀█▀ ░█▀▀▀█ ░█▀▀▀█   ░█─── █▀▀█ █▀▀ █▀▀█ █──   ░█─░█ █▀▀█ █▀▀ ▀▀█▀▀ 
    ░█─░█ ░█─ ░█──░█ ─▀▀▀▄▄   ░█─── █──█ █── █▄▄█ █──   ░█▀▀█ █──█ ▀▀█ ──█── 
    ░█▄▄▀ ▄█▄ ░█▄▄▄█ ░█▄▄▄█   ░█▄▄█ ▀▀▀▀ ▀▀▀ ▀──▀ ▀▀▀   ░█─░█ ▀▀▀▀ ▀▀▀ ──▀──

    |`````````````````````````````````````````````````````````````````````````|
    |  From Disunic Corporation                       Creator - Souvik Nandi  |
    |                                                                         |
    ```````````````````````````````````````````````````````````````````````````    """)
logo()
def helping():print(helpcl+"""
        # Help Section :

        Type : " 1 " , to start local host in random port.

        Type : " 2 " , to start local host,in the port number which typed by you.
    """)
helping()
def start():
    print("")
    Disunic = input(" DIOS: ")
    print("")
    if (Disunic == "exit"):
        exit()
    elif (Disunic == "help"):
        helping()
        return(start())
    elif (Disunic == "1"):
        rand()
    elif (Disunic == "2"):
        mannual()
    elif (Disunic == "clear"):
        os.system('cls')
        logo()
        rand(start())
    else:
        print(" Error command found 🤔!")
        return(start())
def rand():
    # global PORT1
    print("")
    DIRECTORY = input(inputCl+" Path :  ")
    PORT1 = random.randint(1, 10000)
    S1 = "http://127.0.0.1"
    OJ = S1+':'+str(PORT1)
    class Handler(sv.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)
    with socketserver.TCPServer(("", PORT1), Handler) as httpd:
                print("""                                       """)
                print(urlCl+" Url  :", OJ                          )
                print("                                           ")
                print(pathCl+" Path : ", DIRECTORY                 )
                print("                                           ")
                print(pathCl+" Server Hosted Succesfully.         ")
                print("                                           ")
                webbrowser.open(OJ                                 )
                print("Browser Loaded Succesfully. "               )
                print(pyvCl+"| Python Version - ", sys.version, "|")
                print("                                           ")
                print("                                           ")
                httpd.serve_forever()

def mannual():
    print("")
    # print(PORT1)
    DIRECTORY = input(inputCl+" Path :  ")
    PORT = int(input(" PORT : "))
    if (PORT>60000):
        print("")
        print(" Port Must Be 0 to 60000 ")
        return(mannual())
    else:pass
    S1 = "http://127.0.0.1"
    OJ = S1+':'+ str(PORT) 
    class Handler(sv.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print("""                                       """)
                print(urlCl+" Url  :", OJ                          )
                print("                                           ")
                print(pathCl+" Path : ", DIRECTORY                 )
                print("                                           ")
                print(pathCl+" Server Hosted Succesfully.         ")
                webbrowser.open(OJ                                 )
                print("                                           ")
                print("Browser Loaded Succesfully. "               )
                print(pyvCl+"| Python Version - ", sys.version, "|")
                print("                                           ")
                print("                                           ")
                httpd.serve_forever()
mannual(start())
rand(start())
