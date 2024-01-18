'''
Author: jeffliu123 jeffliuhappy0228@gmail.com
Date: 2023-12-09 00:58:35
LastEditors: jeffliu123 jeffliuhappy0228@gmail.com
LastEditTime: 2024-01-18 21:58:10
FilePath: /Biomedical_assignment/LAB1/assignment1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from serial import Serial
import numpy as np
from scipy import stats
import struct
import os
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy.signal import find_peaks
from matplotlib.animation import FuncAnimation
from scipy.interpolate import interp1d
from scipy.signal import medfilt

w=0
read=0
first=0
count=0
data_len=0
ser_arc = Serial('COM5',115200,bytesize=8)

ekg_fil=[]
ekg_org=[]
ppg_fil=[]
ppg_org=[]

start_time=time.time()
print(start_time)

while (1):
    data_len += 1
    if time.time()-start_time>1:
        # print(count)
        start_time=time.time()
        count=0
    data_raw = ser_arc.read(size=1)
    # print(data_raw)
    if data_raw==b'c':
        check_byte = ser_arc.read(size=1)
        # print(struct.unpack("B",data_raw)[0])
        data_raw = ser_arc.read(size=4)
        for i in range(1):
            ba = bytearray()
            ba.append(data_raw[i*3+3])
            ba.append(data_raw[i*3+2])
            ba.append(data_raw[i*3+1])
            ba.append(data_raw[i*3+0])
            ekg_org.append(int(struct.unpack("!f",ba)[0]))
            print('ekg_org : ', struct.unpack("!f",ba)[0])
        data_raw = ser_arc.read(size=4)
        
        for i in range(1):
            ba = bytearray()
            ba.append(data_raw[i*3+3])
            ba.append(data_raw[i*3+2])
            ba.append(data_raw[i*3+1])
            ba.append(data_raw[i*3+0])
            ppg_org.append(int(struct.unpack("!f",ba)[0]))
            print('ppg_org : ', struct.unpack("!f",ba)[0])
        count=count+1
    if len(ekg_org)>=2000 and len(ppg_org)>=2000:
        break
'''
here
'''