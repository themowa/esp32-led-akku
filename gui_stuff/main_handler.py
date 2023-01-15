import time
import requests
from threading import *
from gui_stuff.init_gui import start
from gui_stuff.main_window import start_main
import os
import subprocess
import ast
import json

class storage():
    anzahl=3
    ip_val="www.zeilqwar.de"
    list_latenz=["x","x","x"]
    list_loss = [0, 0, 0]
    list_spannung = ["x", "x", "x"]
    terminate=False
    go=False


def get_data(adress):
    adress="http://"+adress+"/spannung"
    try:
        response = requests.get(adress,timeout=1)
    except requests.exceptions.ConnectTimeout:
        return "timeout"

    return ast.literal_eval(response.text)

def threading_everithing_else():
    # Call work function
    t1 = Thread(target=none_gui,args=(storage, ))  #
    t1.start()

def get_ping(ip_val,number,cl):
    w=ip_val.split(".")
    w[-1]=str(int(w[-1])+number)
    if(int(w[-1]) >255):
        w[-1]=str(int(w[-1])-255)
        w[-2]=str(int(w[-2])+1)
    ip_val=w[0]+"."+w[1]+"."+w[2]+"."+w[3]
    a=subprocess.run("ping "+ip_val+" -n 1",capture_output=True,shell=True)
    print(a)
    if("Zielhost nicht erreichbar" in str(a) or "Verloren = 1" in str(a)):
        cl.list_latenz[number]="-"
        cl.list_loss[number] = cl.list_loss[number]+1
    else:
        for i in str(a).split(" "):
            if("Zeit=" in i):
                cl.list_latenz[number]=i.replace("Zeit=","").replace("ms","")
                a=get_data(ip_val)
                if(a=="timeout"):
                    cl.list_loss[number] = cl.list_loss[number] + 1
                    cl.list_spannung[number] = "x"
                else:
                    cl.list_spannung[number] =a["spannung"]


def none_gui(x):
    for i in range(1000):
        if(storage.terminate):
            break
        time.sleep(3)
        for j in range(storage.anzahl):
            t2 = Thread(target=get_ping, args=(storage.ip_val,j,storage,))  #
            t2.start()
            #get_ping(storage.ip_val,j,storage)

        print(storage.list_latenz)



# print("start")
# start(storage)
#
# print(storage.anzahl)


# start_main(storage)

#threading_main_gui()


try:
    with open('settings.json') as f:
       dict_in= json.load(f)

    storage.ip_val=dict_in["ip_val"]
    storage.anzahl=dict_in["anzahl"]
except:
    pass


start(storage)
if(storage.ip_val=="ddos"):
    for q in range(1):
        storage.ip_val="192.168.178.151"
        storage.anzahl=30000

if(storage.go):
    threading_everithing_else()
    start_main(storage)

    dict_save={"ip_val":storage.ip_val,"anzahl":storage.anzahl}
    with open('settings.json', "w") as f:
        json.dump(dict_save, f)


