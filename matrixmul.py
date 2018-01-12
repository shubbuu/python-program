# matrix multiplication
print('Enter order of matrix : ')
n = int(input())
span = []
for k in range(n):
    print('Enter value in matrix :')
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(int(input()))
        a.append(b)
    span.append(a)
A, B = span[0], span[1]
C = [[0, 0], [0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

for i in C:
    print(i)
