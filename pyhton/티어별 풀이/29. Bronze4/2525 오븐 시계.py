a, b = input().split()
c = input()

a = int(a)
b = int(b)
c = int(c)

hour = a
minute = b + c

hour = hour + minute // 60
hour %= 24  #24시 초과 고려

minute %= 60

print(hour, minute)
