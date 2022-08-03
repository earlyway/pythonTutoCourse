# while loop = a statement that will execute it's block of code, as long as it's condition remains true
# 코드블럭의 상태가 참으로 남아 있는 한, 그 코드블럭은 실행할 것이다.

#while 1 == 1 :
#    print('Help! im stuck in a loop!')

name = ""
while len(name) < 3:       #len 은 문자열 길이를 파악.
    name = input("Enter your name : ")
    
print("Hello "+name)