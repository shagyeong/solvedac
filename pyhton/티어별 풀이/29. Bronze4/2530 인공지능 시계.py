a, b, c = input().split()
d = input()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

totalsecond = a * 3600 + b * 60 + c + d

hour = totalsecond // 3600
totalsecond = totalsecond % 3600
hour = hour % 24

minute = totalsecond // 60
totalsecond = totalsecond % 60

second = totalsecond

print(hour, minute, second)
