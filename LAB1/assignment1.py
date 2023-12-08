from serial import Serial
import struct
import matplotlib.pyplot as plt
import os
import numpy as np
import keyboard  
from scipy.signal import find_peaks

ser_arc = Serial('COM3',38400,bytesize=8)#Check the COM port in your computer and chage
data=[]
data1=[]
sampling_rate = 330
#####################################Make sure the connect
while True:
    data_raw = ser_arc.read(size=1)
    if data_raw==b'c':
        data_raw = ser_arc.read(size=4)
        for i in range(1):                  
            ba = bytearray()
            ba.append(data_raw[i*3+3])    
            ba.append(data_raw[i*3+2])      
            ba.append(data_raw[i*3+1])
            ba.append(data_raw[i*3+0])
            data.append(struct.unpack("!f",ba)[0])     
            data_array = np.array(data)
            peaks, _ = find_peaks(data_array,height = 250)
            print(peaks)
            peaks_ans = np.diff(peaks)
            print(peaks_ans)
            if len(peaks_ans)>0:
                print('Pulse Rate is : ',round(60/(peaks_ans[-1]/sampling_rate),1)," BPM")

    data_raw = ser_arc.read(size=1)
    if data_raw==b'c':
        data_raw = ser_arc.read(size=4)
        for i in range(1):                  
            ba = bytearray()
            ba.append(data_raw[i*3+3])     
            ba.append(data_raw[i*3+2])      
            ba.append(data_raw[i*3+1])
            ba.append(data_raw[i*3+0])
            data1.append(struct.unpack("!f",ba)[0])     
    if keyboard.is_pressed('esc'):
        break



