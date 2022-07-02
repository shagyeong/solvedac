n = ["1"]
a = []

while n != ["0"]:
    n = list(input())
    a.append(n)
del a[len(a) - 1]

def wideofplate(array):
    wideofplate = 1
    for i in array:
        if i == "0":
            wideofplate += 5
        elif i == "1":
            wideofplate += 3
        else:
            wideofplate += 4
    return wideofplate

for i in a:
    print(wideofplate(i))
