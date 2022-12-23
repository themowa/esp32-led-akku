import time
import requests
from threading import *
from gui_stuff.init_gui import start

class storage():
    anzahl=1
    ip_val="0"

# def threading():
#     # Call work function
#     t1 = Thread(target=start,args=(storage, ))  #
#     t1.start()
#
# threading()
# for i in range(10):
#     print(storage.anzahl)
#     time.sleep(3)

print("start")
start(storage)

print(storage.anzahl)