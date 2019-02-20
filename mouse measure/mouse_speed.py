'''
Measureeasure speed and displacement of mouse in 2D
in terms of pixel and second

When console is in focus, press 'Q' to terminate

Display the highest speed achieved in x, y directions
'''
import time
import sys
import win32api

position = win32api.GetCursorPos()
pre_x = position[0]
pre_y = position[1]
last_time = time.time()
max_x = 0
max_y = 0

while True:
    time.sleep(0.0001)
    if win32api.GetAsyncKeyState(ord('Q')):
        print('max vel x: {},\tmax vel y:{}'.format(max_x, max_y))
        sys.exit()
        
    current = time.time()
    tick = current - last_time
    last_time = current
    
    position = win32api.GetCursorPos()
    delta_x = position[0] - pre_x
    delta_y = position[1] - pre_y
    pre_x = position[0]
    pre_y = position[1]
    
    vel_x = delta_x/tick
    vel_y = delta_y/tick
    
    # print nothing if not moving
    if vel_x!=0.0 and vel_y!=0.0:
        print('duration: {}'.format(tick))
        print('delta x: {},\tdelta y: {}'.format(delta_x, delta_y))
        print('vel x: {},\tvel y: {}'.format(vel_x, vel_y))
        if abs(vel_x) > max_x:
            max_x = abs(vel_x)
        if abs(vel_y) > max_y:
            max_y = abs(vel_y)
        print()
