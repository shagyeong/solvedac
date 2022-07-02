list0 = []
for i in range(0, 3):
    n = int(input())
    list1 = []
    for i in range(0, n):
        a = int(input())
        list1.append(a)
    list0.append(list1)

for i in list0:
    if sum(i) > 0:
        print("+")
    elif sum(i) < 0:
        print("-")
    else:
        print("0")
