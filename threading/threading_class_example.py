#!/usr/bin/python3

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print(threading.currentThread())
        print(threading.activeCount())
        print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            #threadName.exit()   # what's this?!
            return               # complete the task
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

print(threading.activeCount())     # How many thread is running
print(threading.currentThread())   # Present thread
print(threading.enumerate())       # List of all active threads

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print(threading.activeCount())
print(threading.currentThread())
print(threading.enumerate())
print ("Exiting Main Thread")
