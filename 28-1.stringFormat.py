#str format() = optional method that gives users
# more control when displaying output
# 유저에게 주는 optional 메소드이다.
# 출력을 낼때 더 많이 컨트롤 할 수 있다.

animal = 'cow'
item = 'moon'

#print("The "+animal+' jumped over the '+item)
print("The {} jumped over the {}".format(item,animal))
print("The {1} jumped over the {0}".format(item,animal)) # positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) # keyword argument

text = "T!he {} jumped over the {}"
print(text.format(animal, item))



