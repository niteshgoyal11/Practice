from threading import Thread, current_thread
from time import sleep

def abc():
    i = 0
    while True:
        if i == 10:
            break
        i += 1
        print(current_thread().name)
        sleep(2)

def abc1():
    i = 0
    while True:
        if i == 20:
            break
        i += 1
        print(current_thread().name)
        sleep(2)


def abc2():
    i = 0
    while True:
        print("Going in While loop")
        if i == 1:
            sleep(20)
        print("Wait of 20 seconds ended")
        i += 1
        print(current_thread().name)
        sleep(2)


t1 = Thread(target=abc2, args=[], name="T1")
t2 = Thread(target=abc1, args=[], name="T2")
t1.start(); t2.start(); t1.join(); t2.join()