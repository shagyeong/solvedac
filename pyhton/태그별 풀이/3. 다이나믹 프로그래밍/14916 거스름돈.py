n = int(input())

if (n == 1 or
    n == 3):
    print("-1")
else:
    quo5 = n // 5
    mod5 = n % 5

    if   mod5 == 0:
        print(quo5)
    elif mod5 == 1:
        print(quo5 - 1 + 3)
    elif mod5 == 2:
        print(quo5 - 0 + 1)
    elif mod5 == 3:
        print(quo5 - 1 + 4)
    elif mod5 == 4:
        print(quo5 - 0 + 2)
