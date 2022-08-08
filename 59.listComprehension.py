# list comprehension = a way to create a new list with less syntax
#   can mimic certain lambda functions, easier to read
#   list = [expression for item in iterable]
#   list = [expression for item in iterable if conditional]
#   list = [expression (if/else) for item in iterable]
# 적은 문장으로 새로운 리스트를 만드는 방법
# 특정 lambda 함수를 모방할 수 있음. 읽기 쉬움.
# 반복 가능한 아이템을 위한 식
# 조건문일때, 반복가능한 아이템을 위한 식
# 반복가능한 아이템을 위한 if문

squares = []                #빈 배열 생성
for i in range(1,11):       #for 루프
    squares.append(i * i)   #각 루프 반복이 해야할 일을 정의
print(squares)

squares = [i*i for i in range(1,11)]
print(squares)

###################################
students = [100,90,80,70,60,50,40,30,0]
passed_students = list(filter(lambda x: x >=60, students))

print(passed_students)
#####################################
students = [100,90,80,70,60,50,40,30,0]

passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)
