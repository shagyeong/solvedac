a, b, c, d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

gap = a + d - (b + c)

if gap < 0:
    print(-gap)
else:
    print(gap)
