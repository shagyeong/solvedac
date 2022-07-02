a, b = input().split()

c = int(a)
d = int(b)
a = abs(int(a))
b = abs(int(b))

q = a // b
r = a % b

if c >= 0:
    if d >= 0:
        q = q
        r = r        
    else:
        q *= -1
        r = r
else:
    if d >= 0:
        q = (-1) * (q + 1)
        r = b - r
    else:
        q = q + 1
        r = b - r
    
print(q)
print(r)
