n = int(input())

k = n // 3

#0! = 1이므로 k=3일땐 그냥 1을 출력

a = k - 3 + 2
b = a - 2

case = 1

for i in range(0, b):
    case = case * a
    a = a - 1

for i in range(0, b):
    case = case // b
    b = b - 1

print(case)
