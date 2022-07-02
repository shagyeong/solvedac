a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if b > c:
    print(int(a * b / c))
else:
    print(int(a  /b * c))
