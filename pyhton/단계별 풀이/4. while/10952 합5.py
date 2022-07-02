import sys

a = "1"
b = "1"

while a != "0" and b != "0":
    a, b = sys.stdin.readline().split()
    if a != "0" and b != "0":
        print(int(a) + int(b))
