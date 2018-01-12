print('Enter no of case : ')
N = int(input())
list = []
for i in range(N):
    print('Enter command : ')
    cmd = input()
    s = cmd.split(' ')
    fn = s[0]
    op = s[1: ]
    if fn == 'insert':
        list.insert(int(op[0]), int(op[1]))
    elif fn == 'remove':
        list.remove(int(op[0]))
    elif fn == 'append':
        list.append(int(op[0]))
    elif fn == 'sort':
        list.sort()
    elif fn == 'pop':
        list.pop()
    elif fn == 'reverse':
        list.reverse()
    elif fn == 'print':
        print(list)
