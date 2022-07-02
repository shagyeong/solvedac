import sys

t = int(input())
sums = []

for i in range(0, t):
    a, b = sys.stdin.readline().split()
    sums.append(int(a) + int(b))

for i in sums:
    print(i)
