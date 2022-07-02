a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a == b:
    if b == c:
        print(10000 + 1000 * a)
    else:
        print(1000 + a * 100)
else:
    if b == c:
        print(1000 + b * 100)
    else:
        if c == a:
            print(1000 + c * 100)
        else:
            print((max([a, b, c])) * 100)
