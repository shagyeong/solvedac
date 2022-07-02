import sys

n, x = sys.stdin.readline().split()
a = list(map(int, sys.stdin.readline().split()))

x = int(x)

for i in a:
    if i < x:
        print(i, end = " ")
