import time
import os
from logger import *

while 1:
    hostname = "URL"
    response = os.system("wget " + hostname)
    if response == 0:
        pingstatus = "Network Active"
        print pingstatus
        setInfo()
        info("Connection successful")
    else:
        pingstatus = "Network Error"
        setDebug()
        error( " NO Connection" )
	time.sleep(10)
