import win32api
import time
import numpy as np
import matplotlib.pyplot as plt
#
# Adjust the mouse sensitivity to slow
# until the cusor moves almost the same speed as the physical mouse
#
xarray = [0]
yarray = [0]
velx = [0]
vely = [0]
(wasx, wasy) = win32api.GetCursorPos()
n = [0]
duration = 0.0
was = time.time()
#factor = 28.5/1080             # cm/pixel for my ASUS monitor
factor = 17.4/768              # cm/pixel for my Acer PC

# experiment in my PC shows ~16 msec per cycle
# max. reading freq. is ~60 times/sec 
while duration < 3000.0:
    # to prevent divide by zero error
    time.sleep(0.0001)
    #
    now = time.time()   
    (x, y) = win32api.GetCursorPos()
    delta = (now - was)*1000  # milli-sec
    duration += delta
    n.append(duration)
    was = now
    # xarray.append(x-wasx)
    # velx.append((x-wasx)/delta*1000.0*factor/100)   # m/sec
    # yarray.append(y-wasy)
    # vely.append((y-wasy)/delta*1000.0*factor/100)
    xarray.append((x-wasx)*factor)                    # cm
    velx.append((x-wasx)/delta*1000.0*factor/100)     # m/sec
    yarray.append((y-wasy)*factor)
    vely.append((y-wasy)/delta*1000.0*factor/100)
    wasx = x
    wasy = y

print(len(n))

narray = np.asarray(n)

plt.subplot(2, 2, 1)
plt.plot(narray, np.asarray(xarray), 'r.-')
plt.title('position of x')
#plt.ylabel('delta movement(pixels)')
plt.ylabel('delta movement(cm)')

plt.subplot(2, 2, 2)
plt.plot(narray, np.asarray(velx), 'g.-')
plt.title('velocity of x')
plt.ylabel('speed (m/s)')

plt.subplot(2, 2, 3)
plt.plot(narray, np.asarray(yarray), '.-')
plt.title('position of y')
plt.xlabel('time (ms)')
#plt.ylabel('delta movement(pixels)')
plt.ylabel('delta movement(cm)')

plt.subplot(2, 2, 4)
plt.plot(narray, np.asarray(vely), 'b.-')
plt.title('velocity of y')
plt.xlabel('time (ms)')
plt.ylabel('speed (m/s)')

plt.tight_layout()   # ensure sufficient space between plots
plt.show()