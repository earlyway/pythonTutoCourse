import time

# for loop = a statement that will execute it's block of code a limited amount of times
    #횟수가 정해져있는 코드블럭을 실행
# while문은 제한없음
# for문은 제한있음

#for i in range(10) :
#    print(i+10)


#for i in range(96, 100+3):
#    print(i)


#for i in "Bro Code":
#    print(i)

for seconds in range(10, 0 , -1): #10에서 0까지. 1씩 줄어드는.
    print(seconds)
    time.sleep(1)                   #1초 간격.
print("Happy new Year!")