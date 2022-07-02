#크기별 정사각형 탐색 함수

def square_search(s, array):
    n = len(array)
    m = len(array[0])
    result = 0

    for i in range(0, (n - s)):
        for j in range(0, (m - s)):
            if ((array[i][j] == array[i][j + s]) and
                (array[i][j + s] == array[i + s][j]) and
                (array[i + s][j] == array[i + s][j + s])
                ):
                result = 1
                break
    if result == 1:
        return 1
    else:
        return 0

array0 = []
n, m = map(int, input().split())
for i in range(0, n):
    array1 = list(map(int, input()))
    array0.append(array1)

if n < 2 or m <2:
    print("1")
else:
    the_result = 0
    for i in range(min([n, m]), 0, -1):
        if square_search(i, array0) == 1:
            the_side = i
            the_result = 1
            break
    if the_result == 1:
        print((i + 1) ** 2)
    else:
        print("1")
