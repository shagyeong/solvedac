n, k = map(int, input().split())

divisors = [] #divisors 약수들

for i in range(1, n // 2 + 1):
    if n % i == 0:
        divisors.append(i)
divisors.append(n)

if k <= len(divisors):
    print(divisors[k - 1])
else:
    print("0")
