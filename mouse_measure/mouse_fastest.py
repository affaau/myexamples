'''
Measure the speed achieved when mouse move about 100 pixels from stop

When console is in focus, press 'Q' to terminate

Display the highest speed achieved
'''
import time
import sys
import win32api

position = win32api.GetCursorPos()
pre_x = position[0]
pre_y = position[1]
last_time = time.time()
max = 0
movement = 270.0 # pixel
movement_sqr = movement**2

while True:
    if win32api.GetAsyncKeyState(ord('Q')):
        print('max speed: {}'.format(max))
        sys.exit()
        
    position = win32api.GetCursorPos()
    delta_x = position[0] - pre_x
    delta_y = position[1] - pre_y
    distance_sqr = (delta_x**2 + delta_y**2)   
        
    if distance_sqr==0.0:
        last_time = time.time()
        time.sleep(0.001)
        continue
        
    # move less than 100 pixels
    if distance_sqr < movement_sqr:
        continue
     
    current = time.time()
    tick = current - last_time
    pre_x = position[0]
    pre_y = position[1]   

    distance = distance_sqr**0.5
    speed = distance/tick
    if speed > max:
        max = speed
    print('duration: {}'.format(tick))
    print('distance: {}'.format(distance))
    print('speed: {}'.format(speed))
    print()
