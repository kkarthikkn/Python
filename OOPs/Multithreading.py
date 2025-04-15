# allows multiple threads to be created within the same process
# technique where multiple threads run concurrently within a single process
# Threads can handle waiting for I/O without blocking other threads, improving throughput

import threading
import time
import datetime as dt

start_time=dt.datetime.now().strftime("%I:%M:%S")
print(f"Starting Time: {start_time}")

def walk():
    time.sleep(8)
    print("Walking Finished")

def eating():
    time.sleep(5)
    print("Finished Eating")

def study():
    time.sleep(10)
    print("Now Sleeping")

# these below method executes by the order of calling, this process takes more time.
# To overcome this multithreading introduced
''' walk()
    eating()
    study()  '''


task1=threading.Thread(target=walk)
task1.start()

task2=threading.Thread(target=eating)
task2.start()

task3=threading.Thread(target=study)
task3.start()

# .join() used to block the next step until the thread to complete otherwise the nxt-step will be executed first
task1.join()       # to block the calling thread until the thread
task2.join()       # on which it was called has finished its execution.
task3.join()       # It'll wait until the thread finishes

end_time=dt.datetime.now().strftime("%I:%M:%S")
print(f"Ending Time: {end_time}")

print("****** Tasks Completed ******")