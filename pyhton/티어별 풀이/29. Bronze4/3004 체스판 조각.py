a = int(input())

if a % 2 != 0:
    print(int(((a + 1) / 2 + 1) * ((a + 1) / 2)))
else:
    print(int((a / 2 + 1) ** 2))
