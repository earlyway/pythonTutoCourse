# nested functions calls = function calls inside other function calls
    #innermost function calls are resolved first
    #returned value is used as argument for the next outer function
# 다른 함수 호출 내부의 함수 호출이다. 중첩 함수 호출
# 가장 안쪽 함수 호출이 먼저 해결된다.
# 반환된 값은 다음 외부 함쉥 대한 인수로 사용된다.

# num = input('Enter a whole positive number : ')
# num = float(num)
# num = abs(num)
# num = round(num)

# print(num) #input 받은 값을 float화, abs화, round화 하고 출력함.


print(round(abs(float(input('Enter a whole positive number : ')))))