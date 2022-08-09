# daemon thread = a thread tha runs in the background, not important for program to run.
#   your program will not wait for daemon threads to complete before exiting.
#   non-deamon threads can't normally be killed, stay alive until task is complete.
#   ex : background tasks, garbage collection, waiting for input, long running process.
# 데몬 스레드 = 백그라운드에서 실행하는 스레드, 프로그램을 실행하는데에 중요하지않음.
# 프로그램은 데몬 스레드들이 완료되기까지 기다리지 않는다. 종료하기 전에
# 보통 비데몬 스레드는 죽일 수 없다, 일이 완료될때까지 살아라.
# ex ; 백그라운드 태스크, 가비지 컬렉션, 입력 대기, 긴 실행 프로세스

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('logged in for : ', count, 'seconds')

x = threading.Thread(target=timer, daemon=True)
x.start()

#x.setDaemon(True)
#print(x.isDaemon())

answer = input('Do you wish to exit?')