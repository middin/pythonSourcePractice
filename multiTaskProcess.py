#-*- coding: utf-8 -*-
# multiTaskProcess.py
# @author John Doe
# @description 
# @created Wed Dec 05 2018 15:08:11 GMT+0800 (CST)
# @last-modified Wed Dec 05 2018 16:24:41 GMT+0800 (CST)
#

'''
import time

def demo1():
    for i in range(5):
        print("----1----")
        time.sleep(1)

def demo2():
    for i in range(5):
        print("----2----")
        time.sleep(1)

def main():
    demo1()
    demo2()

if __name__ == "__main__":
    main()
'''

'''
import threading
import time
def say_hello():
    print("hello world")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=say_hello)
        t.start()
'''
'''
import threading
from time import sleep, ctime

def sing():
    for i in range(3):
        print("---sing---")
        sleep(1)

def dance():
    for i in range(3):
        print("---dance---")
        sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    
    t1.start()
    t2.start()

    sleep(5)
    print("---end---")
'''

import threading
import time

class myThread(threading.Thread):
    def run(self):
        for l in range(3):
            time.sleep(1)
            msg = "I'm"+self.name+"@"+str(l)
            print(msg)

def test():
    for i in range(5):
        t = myThread()
        t.start()

if __name__ == "__main__":
    test()
