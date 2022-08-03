#slicing = create a substring by extracting elements from another string
#또다른 str으로부터 요소를 추출하여 하위문자열을 만든다 
# indexing[start:stop:step] or slice()

# name = "Bro Code"

# first_name = name[0:2]
# last_name = name[4:8]
# funkey_name = name[0:8:2]


# print(first_name)
# print(last_name)
# print(funkey_name)

website1 = "http://google.com"
webstie2 = "http://wikipedia.com"

slice = slice(10,-4)

print(website1[slice])
print(webstie2[slice] )