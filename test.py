import threading
import datetime
import time

class myThread (threading.Thread):
   def __init__(self, name, counter):
       threading.Thread.__init__(self)
       self.threadID = counter
       self.name = name
       self.counter = counter
   def run(self):
       print("Starting " + self.name)
       for i in range(10):
           print(f"thread {self.counter} say {i}\n")
           time.sleep(1)
       print("Exiting " + self.name)

def print_date(threadName, counter):
   datefields = []
   today = datetime.date.today()
   datefields.append(today)
   print(
      "%s[%d]: %s" % ( threadName, counter, datefields[0] )
   )

# Создать треды
thread1 = myThread("Thread", 1)
#thread2 = myThread("Thread", 2)

# Запустить треды
thread1.start()
#thread2.start()

for i in range(10):
    print(f"from main: {i}")
    time.sleep(0.5)

thread1.join()
#thread2.join()
print("Exiting the Program!!!")