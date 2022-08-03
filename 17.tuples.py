# tuple = collection which is ordered and unchangeable used to group together related data
# 관련 데이터를 모아서 사용되는 순서와 변경할 수 없는 컬렉션.
# 요소를 일렬로 저장하지만 저장된 요소를 변경, 추가, 삭제할 수 없음(readonly)

student = ("Bro", 21, "male") # student = "Bro", 21, "male"  로 해도 튜플이 됨.

print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Bro" in student:
    print("Bro is here")