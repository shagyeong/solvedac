c, a, b = input().split()

a = int(a)
b = int(b)
c = int(c)

k = (c * c / (a * a + b * b)) ** (1/2)

print(int(a * k), int(b * k))
