k, d, a = input().split('/')

k = int(k)
d = int(d)
a = int(a)

if k + a < d or d == 0:
    print("hasu")
else:
    print("gosu")
