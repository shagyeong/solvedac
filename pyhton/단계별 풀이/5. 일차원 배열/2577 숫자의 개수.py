a = int(input())
b = int(input())
c = int(input())

d = a * b * c

d = list(str(d))

arr = [0] * 10

for i in d:
    arr[int(i)] += 1

for i in arr:
    print(i)
