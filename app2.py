import threading
import time

shared_variable = 0
lock = threading.Lock()
def increment_shared_variable():
    global shared_variable
    for _ in range(100):
        with lock:
            shared_variable += 1
            time.sleep(0.5)


thread1 = threading.Thread(target=increment_shared_variable)
thread2 = threading.Thread(target=increment_shared_variable)


thread1.start()
thread2.start()


thread1.join()
thread2.join()


print(f"final value of shared_variable: {shared_variable}")