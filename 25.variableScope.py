#scope = The region that a variable is recognized.
#   A variable is only available from inside the region it is created.
#   A global and locally scoped versions of a variable can be created.
# 변수가 인식되는 영역이다. Scope
# 변수는 만들어진 영역 안에서만 사용 할 수있다.
# 변수의 전역, 로컬 범위 버전을 만들 수 있다.


name = "Bro"        #global scope(available inside & outside functions)

def display_name():
    name = "Code"   #local scope(available only inside this function)
    print(name)
    
    
display_name()
print(name)

