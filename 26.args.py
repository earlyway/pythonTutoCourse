# args = parameter that will pack all arguments into a tuple.
# useful so that a function can accept a varying amount of arguments.
# 모든 인수를 튜플에 대입하는 매개변수이다.
# 많은 인수들을 함수에 쓸 수 있기에 적절하다.

# def add(*args):
#     sum = num1 + num2
#     return sum

# print(add(3,3))
#인수가 자동으로 파라미터로 들어가 num1, num2에 배분됨.



def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(3,4,5,6))     #3,4,5,6 인수가 args로 들어가고 for문이 되서 0+3+4+5+6




