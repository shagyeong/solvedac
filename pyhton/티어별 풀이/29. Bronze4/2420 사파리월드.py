a, b = input().split()

a = int(a)
b = int(b)

gap = a - b

if gap < 0:
    print(gap * (-1))
else:
    print(gap)
