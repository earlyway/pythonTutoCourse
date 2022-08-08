# sort() method   = used with lists
# sort() function = used with iterables

students = ['Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Krabs']
#students.sort(reverse=True)
sorted_students = sorted(students,reverse=True)

for i in sorted_students:
    print(i)



studen = [
            ('Squidward', 'F', 60),
            ('Sandy','A',33),
            ('Patrick','D',36),
            ('Spongebob','B',20),
            ('Krabs','C',78)]

age = lambda ages:ages[2]
#studen.sort(key=grade,reverse=True)
sorted_studen = sorted(studen, key=age)

for i in studen:
    print(i)