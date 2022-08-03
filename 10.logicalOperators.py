# logical operators(and, or, not) = used to check if two or more conditional statements is true.
# 만약 2개나 그 이상의 상태에 진실을 체크하고 싶을때 논리 연산자를 씀

temp = int(input("What is the temperature outside? : "))

if temp >= 0 and temp <=30:
    print("the temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")
    
    
    