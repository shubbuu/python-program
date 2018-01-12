print('enter number of students : ')
n = int(input())
std_d = {}
i = 0
while i < n:
    print('Enter name of student : ')
    x = input()
    print('Enter marks for physics, Maths, History : ')
    
    marks = []
    p = int(input())
    m = int(input())
    h = int(input())
    marks.append(p)
    marks.append(m)
    marks.append(h)
    std_d.setdefault(x, marks)
    i += 1
for i in std_d.items():
    print(i)
    
