# dictionary = A changeable, unoredered collection of unique key:value pairs.
    # Fast because they use hashing, allow us to access a value quickly
# 바꿀 수 있고 순서가 정해지지않은 고유의 키값 쌍을 가진 컬렉션.
# 해쉬를 사용하기때문에 빠르게 값에 액세스할 수 있다.

capitals = {'USA' : 'Washington DC',
            'India' : 'NewDehli',
            'China' : 'Beijing',
            'Russia' : 'Moscow'
            }
print(capitals['Russia'])
#print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())


#capitals.update({'Germany' : 'Berlin'}) #key:value 추가도 가능.

for key,value in capitals.items():
    print(key, value)
    