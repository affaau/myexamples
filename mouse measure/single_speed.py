'''
Measureeasure speed and displacement of mouse in 2D
in terms of pixel and second

When console is in focus, press 'S' to start

Display the highest speed achieved in x, y directions
'''
import time
import sys
import win32api

while True:
    while not win32api.GetAsyncKeyState(ord('S')):
        pass

    print('Start...')
    initial = win32api.GetCursorPos()
    distance = 0.0
    threshold = 270.0    # pixel
    start = time.time()

    while distance < threshold:
        current = win32api.GetCursorPos()   
        delta_x = current[0] - initial[0]
        delta_y = current[1] - initial[1]
        distance = (delta_x**2 + delta_y**2)**0.5

    tick = time.time() - start
    print('duration: {} sec'.format(tick))
    # monitor is 27 pixel/cm
    print('distance travel: {} cm'.format(distance/27.0))
    print('speed: {} cm/sec'.format(distance/27.0/tick))
    print()
