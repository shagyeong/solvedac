a, b, c, d, e = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

print((a * a + b * b + 
           c * c + d * d + e * e) % 10)
