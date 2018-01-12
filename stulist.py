from operator import itemgetter
students = []
for i in range(3):
    name = input()
    score = float(input())
    students.append([name, score])

students.sort(key = itemgetter(1,0))

print(students)
