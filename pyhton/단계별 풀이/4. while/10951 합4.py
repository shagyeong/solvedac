import sys

while True:
    try:
        a, b = sys.stdin.readline().split()
    except:
        break
    print(int(a) + int(b))
