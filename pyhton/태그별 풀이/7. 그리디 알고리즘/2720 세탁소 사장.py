#쿼터 25센트 - q
#다임 10센트 - d
#니켈  5센트 - n
#페니  1센트 - p

def coinchange(cent : int):
    change = cent

    q = change // 25
    change %= 25

    d = change // 10
    change %= 10

    n = change // 5
    change %= 5

    p = change #//1은 생략

    print(q, d, n, p, sep = ' ', end = '\n')

n = int(input())

for i in range(0, n):
    change = int(input())
    coinchange(change)
