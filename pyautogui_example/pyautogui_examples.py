#!/usr/bin/python3
import pyautogui
import time

def mouseMovement_abs():
    """move mouse to draw square based on absolute coordinates"""
    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

def mouseMovement_rel():
    """move mouse to draw square relative to present mouse location"""
    for i in range(10):
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)
      
def mouseNow():
    """Displays the mouse cursor's current position"""
    print('Press Ctrl-C to quit.')
    # Get and print the mouse coordinates
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            # Move printing cursor to the back
            # Always pass flush=True to print() calls, otherwise,
            # the screen might not update the text as desired
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print("\nDone.")   

def virtual_mouse_click():
    """pyautogui.click() by default assume 'left key' at current mouse coordinates
    Can pass x- and y-coordinates of the click as optional first and second arguments
    Support button keyword argument, with a value of 'left', 'middle', or 'right'
    e.g. pyautogui.click(100, 150, button='left')
    
    Other functions like simulating pyautogui.mouseDown(), pyautogui.mouseUp() with
    simular argumetns as click()
    
    A wrapper function of mouse left or right click like pyautogui.rightClick(), leftClick()
    x, y arguments apply
    
    Another wrapper function, pyautogui.doubleClick(x,y,interval, button)
    """
    pass

def spiralDraw():
    """When you run this program, there will be a five-second delay 
    for you to move the mouse cursor over the drawing program’s window 
    with the Pencil or Brush tool selected. Then spiralDraw.py will take 
    control of the mouse and click to put the drawing program in focus"""
    time.sleep(5)
    pyautogui.click()    # click to put drawing program in focus
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)    # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)    # move down
        pyautogui.dragRel(-distance, 0, duration=0.2)   # move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2)   # move up

if __name__ == '__main__':
    pyautogui.size()      # return (width, height)
    #mouseMovement_abs()
    #mouseMovement_rel()
    #mouseNow()
    spiralDraw()