# filter() = creates a collection of elements from an iterable for which a function returns true.
# filter(function, iterable)
# 요소들의 콜렉션을 생성한다. (어떤 요소들?) 함수가 true를 반환하는 반복가능한

friends = [
    ('Rachel', 19),
    ('Monica', 18),
    ('Phoebe', 17),
    ('Joey', 16),
    ('Chandler', 21),
    ('Ross', 20)
    ]

age = lambda data:data[1] >= 18
drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)