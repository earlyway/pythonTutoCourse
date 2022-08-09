# thread = a flow of execution. Like a separate order of instructions.
#   However each thread takes a turn running to achieve concurrency.
#   GIL = (Global interpreter lock),
#   allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program / task spends most of it's time waiting for internal events (CPU intensive )
#   use multiprocessing

# io bound = program / task spends most of it's time waiting for external events (user input, web scraping)
#   use multithreading

# 스레드 = 실행 흐름. 설명의 분리 순서같은
# 그러나 각 스레드는 동시성을 달성하기 위해 실행된다.
# GIL은 스레드 하나만 허용한다. 단 한번에 파이썬의 컨트롤을 유지하기위해서

# cpu bound = 프로그램이나 태스크는 내부 이벤트를 위해 시간대기의 대부분을 사용 cpu 집약적
# io bound = 프로그램이나 태스크는 외부 이벤트를 위해 시간대기의 대부분을 사용 

from concurrent.futures import thread
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print('You eat breakfast')
    
def drink_coffe():
    time.sleep(4)
    print('You drank coffee')
    
def study():
    time.sleep(5)
    print('You finish studying')
    
x = threading.Thread(target= eat_breakfast, args=())
x.start()

y = threading.Thread(target= drink_coffe, args=())
y.start()

z = threading.Thread(target= study, args=())
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffe()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())