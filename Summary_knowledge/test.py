import threading
import time
lock = threading.Lock()
counter = 0
def race_condition():
    global counter
    # with lock:
    counter += 1
    time.sleep(0.0001)
    print(threading.current_thread().name, counter)
thread = []
for i in range(1,10):
    t = threading.Thread(target=race_condition,)
    t.start()