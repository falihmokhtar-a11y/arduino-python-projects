import time
import matplotlib.pyplot as plt
#from drawnow import *
import serial
val = [0.0] * 50
freq = 0

#create the serial port object
port = serial.Serial('/dev/cu.usbserial-14440',115200,timeout = 0.01)
t0 = time.time()
valueindex = 0
cnt = 0
#starttime = t0


#plt.ion()

title = "Osciloscope sampling at {:3.1f} Hz"
#create the figure function
def makeFig():
    ax = plt.subplot(1,1,1)
    fhnd = ax.figure
    ax.set_ylim(-0,5000)
    ax.title.set_text(title.format(freq))
    ax.grid(True)
    ax.set_ylabel('data (mV)')
    signal_line = ax.plot(val, 'ro-', label='Channel 0')#,ylim=[-0,3500])
    ax.legend(loc='lower right')
    return fhnd,signal_line,ax.title

fig,signal,fig_title = makeFig()


started = False

def update_figure():
    global freq, t0, cnt, starttime, valueindex, started
    if not started:
        port.write(b'h')
        port.flush()
        if port.out_waiting:
            return
        started = True
    port.write(b's') #handshake with Arduino
    port.flush()
    while port.in_waiting:
        value = port.readline()  # read the reply
        if value == b'on':
            continue
        try:
            number = float(value) / 1024 * 5000   #convert received data
        except:
            number = 0
        
        val[valueindex] = number #val.append((number)
        signal[0].set_ydata(val)
        valueindex += 1
        if valueindex >= len(val):
            valueindex = 0
        cnt += 1
        #val.pop(0)#keep the plot fresh by deleting the data at position 0
        if cnt >= 99:
            cnt = 0
            t1 = time.time()
            freq = 100 / (t1-t0)
            fig_title.set_text(title.format(freq))
            t0 = t1
    fig.canvas.draw_idle()
update_timer = fig.canvas.new_timer(interval=50)
update_timer.add_callback(update_figure)
def on_first_draw(ev):
    fig.canvas.mpl_disconnect(on_first_draw_id)
    update_timer.start()
on_first_draw_id = fig.canvas.mpl_connect('draw_event',on_first_draw)
while not port.isOpen():
    time.sleep(1)
plt.show(block=True)
port.write(b'l')
port.flush()
time.sleep(0.1)
port.close()
 
