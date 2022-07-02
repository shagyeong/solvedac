import sys

t = int(input())

for i in range(0, t):
    a, b = sys.stdin.readline().split()

    print("Case #", i + 1, ": ", a, " + ", b, " = ", int(a) + int(b), sep = '', end = '\n')
