import time
import requests
from threading import *
from gui_stuff.init_gui import init_frame








# max_t=0
# min_t=1
# avg=0
# for i in range(2):
#
#     time_alt=time.time()
#     try:
#         response = requests.get("http://192.168.178.152",timeout=1)
#     except:
#         pass
#     delta=time.time()-time_alt
#     print(delta)
#     avg=avg+delta
#     if(delta>max_t):
#         max_t=delta
#     if (delta < min_t):
#         min_t = delta
#    # print(response.text)
# print("-------")
# avg=avg/500
# print(avg)
# print(min_t)
#print(max_t)

def get_data(adress):
    adress="http://"adress
    try:
        response = requests.get(adress,timeout=1)
    except requests.exceptions.ConnectTimeout:
        return "timeout"
    return response
