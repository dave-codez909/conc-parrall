import threading

def my_function(arg1, arg2):

    print(f"Processing with arguments: {arg1}, {arg2}")


thread = threading.Thread(target=my_function, args=(10, 20))


thread.start()
thread.join()