odds = []

for i in range(0, 7):
    n = int(input())

    if n % 2 != 0:
        odds.append(n)

if len(odds) == 0:
    print("-1")
else:
    print(sum(odds))
    print(min(odds))
