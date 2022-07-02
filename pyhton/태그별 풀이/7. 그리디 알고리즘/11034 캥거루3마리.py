def kangaroo(a:int, b:int, c:int):
    gap1 = b - a - 1
    gap2 = c - b - 1

    if  gap1 > gap2:
        print(gap1)
    elif gap1 < gap2:
        print(gap2)
    else:   #gap1 = gap2
        print(gap1)

while True:
    try:
        a, b, c = map(int, input().split())
        kangaroo(a, b, c)
    except:
        break
