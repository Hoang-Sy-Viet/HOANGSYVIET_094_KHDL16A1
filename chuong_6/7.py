import threading
from datetime import datetime
import  time

def Google():
    print("Starting Google")
    time.sleep(1)

    print('Google: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                     "%Y-%m-%d %H:%M:%S")))
    time.sleep(1)

    print('Google: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                     "%Y-%m-%d %H:%M:%S")))
    time.sleep(1)
    print('Google: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                     "%Y-%m-%d %H:%M:%S")))
    time.sleep(2)
    print('Google: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                     "%Y-%m-%d %H:%M:%S")))
    time.sleep(1)
    print("Exiting Google")

    # time.sleep(1)


def Yahoo():
    print("Starting Yahoo")
    time.sleep(2)
    print('Yahoo: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                    "%Y-%m-%d %H:%M:%S")))
    time.sleep(3)
    print('Yahoo: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                    "%Y-%m-%d %H:%M:%S")))
    time.sleep(2)
    print('Yahoo: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                    "%Y-%m-%d %H:%M:%S")))
    time.sleep(2)
    print('Yahoo: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                    "%Y-%m-%d %H:%M:%S")))
    print("Exiting Yahoo")
def Facebook():
    print("Starting Facebook")
    time.sleep(3)
    print('Facebook: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                       "%Y-%m-%d %H:%M:%S")))
    time.sleep(5)
    print('Facebook: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                       "%Y-%m-%d %H:%M:%S")))
    time.sleep(3)
    print('Facebook: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                       "%Y-%m-%d %H:%M:%S")))
    time.sleep(3)
    print('Facebook: Web {}'.format(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
                                                       "%Y-%m-%d %H:%M:%S")))
    
    time.sleep(1)
    print("Exiting Facebook")
    
def main_task():
    print("Starting Main Task")
    time.sleep(1)
    t1 = threading.Thread(target=Google)
    t2 = threading.Thread(target=Yahoo)
    t3 = threading.Thread(target=Facebook)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("Exiting Main Task")
if __name__ == '__main__':
    main_task()