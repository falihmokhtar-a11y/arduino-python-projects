import serial
import time


ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  

THRESHOLD = 500  

while True:
    line = ser.readline().decode().strip()
    if line.isdigit():
        value = int(line)

        if value > THRESHOLD:
            print("hell")
        else:
            print("dunkel")

    time.sleep(1)
