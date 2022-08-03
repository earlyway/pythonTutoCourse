# # 2D lists = a list of lists

# drinks = ['coffee', 'soda', 'tea']
# dinner = ['pizza', 'hamburger', 'hotdog']
# dessert = ['cake', 'ice cream']

# food = [drinks, dinner, dessert]

# print(food[0])
# print(food[0][0])
# print(food[0][2]) #2차원 배열 ,행렬. 


a = ['1','2','3']
b = ['4','5','6']
c = ['7','8','9']
d = ['10','11','12']

AA = [a,b]
BB = [c,d]

AAA = [AA, BB]

print(AAA[0][0][0])
print(AAA[1][0][0])
print(AAA[0][1][0])
print(AAA[1][1][0])

print(AAA[0][0][1]) #2
print(AAA[0][0][2]) #3
print(AAA[1][0][1]) #8
print(AAA[1][0][2]) #9