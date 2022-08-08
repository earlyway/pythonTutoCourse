#zip(*iterable) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#       creates a zip object with paired elements stored in tuples for each elements
# 요소를 집계한다. 2개 이상의 반복가능한 요소를
# zip 오브젝트를 생성한다. (어떤 zip 오브젝트?) 각 요소들을 위해 튜플에 저장되어있는 요소들을 짝지어서

from multiprocessing.sharedctypes import Value


usernames = ['Dude', "bro", 'Mister']
passwords = ['p@ssword', 'abc123', 'guest']

# users = dict(zip(usernames, passwords))

# print(type(users))

# for key, value in users.items():
#     print(key+' : '+value)

login_date = ['1/1/2021',"1/2/2021",'1/3/2021']

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)