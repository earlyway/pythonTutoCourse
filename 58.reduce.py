# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#   performs function on first two elements and repeats process until 1 value remains
# reduce(function, iterable)
# 함수를 반복가능한지 확인하고 그것을 단일 누적값으로 줄인다.
# 1,2 번째 요소를 실행하고 값이 1개가 남을때까지 프로세스를 반복한다.

# import functools
# letters = ['H','E','L','L','O']
# word = functools.reduce(lambda x,y,:x+y, letters)
# print(word)  ->H E L L O ->HE L L O ->HEL L O ->HELL O ->HELLO

import functools
from math import factorial


factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y,:x*y,factorial)
print(result)   #->5 4 3 2 1 ->20 3 2 1 -> 60 2 1 -> 120 1-> 120