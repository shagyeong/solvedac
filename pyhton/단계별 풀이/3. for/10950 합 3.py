t = int(input())
results = []

for i in range(0, t):
    a, b = map(int, input().split())
    results.append(a + b)

for i in results:
    print(i)
