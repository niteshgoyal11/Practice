import polling
from time import sleep

def abc():
    print("in ABC")
    sleep(50)
    return 0


polling.poll(target=abc, step=10, timeout=100)