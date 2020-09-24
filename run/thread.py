import threading
import time
  
class RunCaseInBroswer (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, broswerName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.broswerName = broswerName

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        print("Starting: ", self.broswerName)
        self.print_time(self.broswerName, 5)
        print("Exiting: " + self.broswerName)
 
    def print_time(self, threadName, counter, delay):
        while counter:
            # if exitFlag:
            #     threading.Thread.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
 
# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 7)
 
# 开启线程
thread1.start()
thread2.start()
 