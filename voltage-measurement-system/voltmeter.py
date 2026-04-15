import time
import serial
import numpy as np

displayformat = "Avg: {:5.3f}V RMS: {:5.3f}V Freq: {:6.1f}Hz\r"
usb_port = '/dev/ttyUSB0'
usb_speed = 115200

def measure(port,nsamples = 100,samplingperiod = 0.1):

    port.write(b'h')
    port.flush()
    while port.out_waiting:
        time.sleep(0.001)
    avg = 0.0
    rms = 0.0
    t1 = t0 = time.perf_counter()
    for valueindex in range(1,nsamples+1):
        port.write(b's') #handshake with Arduino
        port.flush()
        value = port.readline()  # read the reply
        while value in (b'on','off'):
            value = port.readline()  # read the reply
            
            
    
        try:
            number = float(value) / 1024 * 5   #convert received data
        except:
            value = port.readline()
            try:
                number = float(value) / 1024 * 5   #convert received data
            except:
                number = 0
    
        avg += ( number - avg ) / valueindex
        rms += ( number**2 - rms ) / valueindex
        delayed = time.perf_counter() - t1
        time.sleep(samplingperiod-delayed if delayed < samplingperiod else 0.001)
        t1 = time.perf_counter()

    t1 = time.perf_counter()
    return avg,np.sqrt(rms), nsamples / ( t1 - t0 )

def run(usbport,num_samples = 100,period = 0.1, transferrate = 115200,timeout = 0.5):
    try:
        port = serial.Serial(usbport, transferrate, timeout=timeout, write_timeout = timeout,xonxoff = False,parity = serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,)
        command = '.'
        while command not in 'Qq':
            if command != '.':
                print("Auswahl '{}' ungültig\n\n".format(command))
            print('m ... Start der messung')
            print('n ... Anzahl Samples (current: {})'.format(num_samples))
            print('f ... Abtastperiode (current: {:6.3} s'.format(period))
            print('q ... Quit')
            print('-----------------------')
            command = input('Auswahl: ')
            if command in 'Mm':
                command = '.'
                print("\nMessung ...")
                print(displayformat.format(*measure(port,num_samples,period)))
            elif command in 'Nn':
                command = '.'
                try:
                    value = int(input('\nNum samples: '))
                except ValueError:
                    print('Num samples must be a positive integer')
                else:
                    if value < 0:
                        print('Num samples must be a positive integer')
                    else:
                        num_samples = value
            elif command in 'Ff':
                command = '.'
                try:
                    value = float(input('\nSampling period'))
                except ValueError:
                    print('Sampling period must be valid float >=0.001 s')
                else:
                    if value < 0.01:
                        print('Sampling period must be valid float >=0.01 s')
                    else:
                        period = value
    finally:
        print('finishing')
        try:
            print(port.write(b'l'))
            port.flush()
            while port.out_waiting:
                time.sleep(0.01)
            port.close()
        except:
            pass
if __name__ == '__main__':
    run(usb_port,transferrate=usb_speed)
    
 
