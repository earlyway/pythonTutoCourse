# lambda function = function written in 1 line using lambda keyword.
#               accepts any number of arguments, but only has one expression.
#               (useful if needed for a short period of time, throw-away)
#   lambda parameters : expression
#   함수는 1줄로 쓰여진다. lambda 키워드를 사용하면서
#   하나의 식이다. 어느 인수도 허용한다.
#   만약 단기간에 필요하다면 lambda가 유용하며 폐기한다.

# def double(x):
#     return x * 2

# print(double(5))

from xmlrpc.client import FastParser


double = lambda x : x * 2
multiply = lambda x, y : x * y
add = lambda x, y, z : x + y + z
print(double(5))
print(multiply(4,6))
print(add(1,2,2))

full_name = lambda first_name, last_name : first_name + " "+last_name
age_check = lambda age:True if age >= 18 else False
print(full_name("bro","code"))
print(age_check(18))