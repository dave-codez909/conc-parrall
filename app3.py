import threading
import time

def non_demon_task():
    for i in range(1,11):
        print(f'Non-demon thread: {i}')
        time.sleep(2)


def daemon_task():
    while True:
        print('Demon running....')
        time.sleep(1)

daemon_thread = threading.Thread( target=daemon_task)
daemon_thread.daemon = True

non_daemon_thread = threading.Thread(target=non_demon_task)

daemon_thread.start()
non_daemon_thread.start()


time.sleep(5)

print('Main program terminating...')

