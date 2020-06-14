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
      print_time(self, self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(thread, threadName, delay, counter):
   while counter:
      if exitFlag:
         print("Exit")
         break
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
print("Thread 2 name: {}".format(thread2.getName()))
## Set flag to terminate the running thread
exitFlag = 1
##
thread2.join()
print(threading.activeCount())
print ("Exiting Main Thread")