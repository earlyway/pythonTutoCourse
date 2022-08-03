#index operator [] = gives access to a sequence's element(str, list, tuple)

name = "bro Code!"

# if(name[0].islower()):
#     name = name.capitalize()
#print(name)
#이렇게 하면 b만 B로 바뀌고 Bro Code 가 출력됨.

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)