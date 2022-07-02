fibonacci = [0, 1]

n = int(input())

if   n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    for i in range(0, n - 1):
        next = 0
        next = next + fibonacci[0 + i]
        next = next + fibonacci[1 + i]
        fibonacci.append(next)
    print(fibonacci[n])
