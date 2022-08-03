# list = used to store multiple items in a single variable
# 하나의 변수에 여러개의 아이템을 저장하는 방법

food = ['pizza', 'hamburger', 'hotdog', 'spaghetti']

# print(food)
# print(food[3])

food.append('ice Cream')
food.remove("hotdog")
food.pop() #pop 은 마지막 인덱스넘버를 가진 요소를 삭제함.
food.insert(0,'cake')
# food.sort() #name 순서대로 정렬
# food.clear() #리스트의 모든 요소를 삭제.


for x in food:
    print(x)