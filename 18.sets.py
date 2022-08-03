# set = collection which is unordered, unindexed. No duplicate values
# 정렬되지 않고 색인화 되지않은 중복값이 없는 컬렉션
# 그렇기때문에 list 보다 퍼포먼스가 빠름. list 보다 요소 컨트롤이 자유로운.

utensils = {"fork", "spoon","knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

utensils.update(dishes)

dinner_table = utensils.union(dishes)

for x in utensils:
    print(x)
    
print(utensils.intersection(dishes))