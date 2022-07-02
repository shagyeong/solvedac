a = int(input())
b = int(input())
c = int(input())
d = int(input())

total_time = a + b + c + d
minute = total_time // 60
second = total_time % 60

print(minute, end = "\n")
print(second, end = "\n")
