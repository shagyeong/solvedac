n, m = map(int, input().split())
matrix1 = []
for i in range(0, n):
    row = list(map(int, input().split()))
    matrix1.append(row)

m, k = map(int, input().split())
matrix2 = []
for i in range(0, m):
    row = list(map(int, input().split()))
    matrix2.append(row)

matrix3 = []#행렬곱 결과

for i in range(0, n):

    row = []

    for j in range(0, k):
        sum = 0
        for h in range(0, m):
            sum = sum + matrix1[i][h] * matrix2[h][j]
        row.append(sum)
    matrix3.append(row)

for i in range(0, len(matrix3)):
    for j in range(0, len(matrix3)):
        print(matrix3[i][j], end = '')
        if j == len(matrix3) - 1:
            print('\n', end = '')
        else:
            print(' ', end = '')
