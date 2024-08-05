import threading
import time

def function_a():
    print("Function A starting")
    time.sleep(2)
    print("Function A finished")

def function_b():
    print("Function B starting")
    time.sleep(3)
    print("Function B finished")

def function_c():
    print("Function C starting")
    time.sleep(1)
    print("Function C finished")

# Create threads for each function
thread_a = threading.Thread(target=function_a)
thread_b = threading.Thread(target=function_b)
thread_c = threading.Thread(target=function_c)

# Start the threads
thread_a.start()
thread_b.start()
thread_c.start()

# Wait for all threads to complete
thread_a.join()
thread_b.join()
thread_c.join()

print("All functions completed!")
