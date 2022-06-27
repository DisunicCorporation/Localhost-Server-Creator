import http.server
from multiprocessing.connection import wait
from colored import fg
import socketserver
import random
import sys
back = fg("#2196f3")
print(back+"""


░█▀▀▄ ▀█▀ ░█▀▀▀█ ░█▀▀▀█   ░█─── █▀▀█ █▀▀ █▀▀█ █──   ░█─░█ █▀▀█ █▀▀ ▀▀█▀▀ 
░█─░█ ░█─ ░█──░█ ─▀▀▀▄▄   ░█─── █──█ █── █▄▄█ █──   ░█▀▀█ █──█ ▀▀█ ──█── 
░█▄▄▀ ▄█▄ ░█▄▄▄█ ░█▄▄▄█   ░█▄▄█ ▀▀▀▀ ▀▀▀ ▀──▀ ▀▀▀   ░█─░█ ▀▀▀▀ ▀▀▀ ──▀──
                                                                                __________________________________
                                                                               |                                  |
                                                                               |     From Disunic Corporation     |
                                                                               |__________________________________|
                                                                               """)
inp = fg("#20b2aa")
ul = fg("#ff9800")
pa = fg("#3f51b5")
py = fg("#e91e63")
def et():
    Disunic = input(">>>")
    if (Disunic == "exit"):
        exit()
    else:
        print("Error")
        return(et())
def main():
    DIRECTORY = input(inp+" Path :  ")
    PORT = random.randint(1, 10000)
    S1 = "http://127.0.0.1"
    OJ = S1+':'+str(PORT)
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print("""                                       """)
                print(ul+" Url  :", OJ                             )
                print("                                           ")
                print(pa+" Path : ", DIRECTORY                     )
                print("                                           ")
                print(pa+" Server Hosted Succesfully.")
                print("                                           ")
                print(py+"| Python Version - ", sys.version, "|   ")
                print("                                           ")
                # print("Type ' exit ' to EXIT Window"             )
                print("                                           ")
                httpd.serve_forever()
                # return(et())         
 
main()

