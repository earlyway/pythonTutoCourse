#return statement = Functions send Python values/objects back to the caller.
    #These values/objects are known as the function's return value.
# 함수가 '함수의 return값이라 불리는 python 값, 객체들'을 호출자에게 다시 보낸다.

# def multiply(number1, number2):
#     result = number1 * number2
#     return result
# print(multiply(6,8))
#---------이렇게 하면 48이 출력되고 아래와 같은 방법으로도 48을 출력할 수 있음.

def multiply(number1, number2):
    return number1 * number2

x = multiply(6,8)
print(x)

