#if Statement = a block of code that will execute if it's condition is true
# 그 코드블럭이 만약 참이라면 실행할 것이다.

age = int(input('How old are you? : '))

if age >= 18:
    print('You are an adult')
elif age < 0:
    print("You haven't been born yet")
else:
    print('You are a young')