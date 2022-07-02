import sys
input = sys.stdin.readline

case = int(input())

a = 0

for i in range(0, case):
    plug = int(input())
    a += plug
print(a - case + 1)
