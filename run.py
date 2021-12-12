import pywhatkit
import numpy as np

def send_mssg_personal(ph_num, mssg, hr, min_):
    return pywhatkit.sendwhatmsg(str(ph_num), str(mssg), time_hour=np.squeeze(hr), time_min=np.squeeze(min_))

def squeeze(elem):
    return np.squeeze(elem)

