case = int(input())
cases = []

for i in range(0, case):
    a, b = input().split(' ')
    a = int(a[len(a) - 1])
    b = int(b)
    if a == 0:
        cases.append("10")
    elif a == 1:
        cases.append("1")
    elif a == 2:
        if b % 4 == 1:
            cases.append("2")
        elif b % 4 == 2:
            cases.append("4")
        elif b % 4 == 3:
            cases.append("8")
        else:
            cases.append("6")
    elif a == 3:
        if b % 4 == 1:
            cases.append("3")
        elif b % 4 == 2:
            cases.append("9")
        elif b % 4 == 3:
            cases.append("7")
        else:
            cases.append("1")
    elif a == 4:
        if b % 2 == 1:
            cases.append("4")
        else:
            cases.append("6")
    elif a == 5:
        cases.append("5")
    elif a == 6:
        cases.append("6")
    elif a == 7:
        if b % 4 == 1:
            cases.append("7")
        elif b % 4 == 2:
            cases.append("9")
        elif b % 4 == 3:
            cases.append("3")
        else:
            cases.append("1")
    elif a == 8:
        if b % 4 == 1:
            cases.append("8")
        elif b % 4 == 2:
            cases.append("4")
        elif b % 4 == 3:
            cases.append("2")
        else:
            cases.append("6")
    elif a == 9:
        if b % 2 == 1:
            cases.append("9")
        else:
            cases.append("1")

for i in cases:
    print(i)
