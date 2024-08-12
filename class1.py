import threading
import time

# Shared resource and lock
shared_list = []
lock = threading.Lock()

def append_to_list(num):
    global shared_list
    with lock:
        shared_list.append(num)
        print(f'Thread {threading.current_thread().name} appended {num} to the list')
        time.sleep(1)

# Create and start threads with arguments
thread1 = threading.Thread(target=append_to_list, args=(1,), name='Thread-1')
thread2 = threading.Thread(target=append_to_list, args=(2,), name='Thread-2')

thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print('Final list:', shared_list)
