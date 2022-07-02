a = []

for i in range(0, 10):
    change = int(input()) % 42
    
    if len(a) == 0:
        a.append(change)
    else:
        case = 0
        j = 0

        while j < len(a) and case != 1:
            if change == a[j]:
                case = 1
            j = j + 1

        if case == 0:
            a.append(change)
print(len(a))
