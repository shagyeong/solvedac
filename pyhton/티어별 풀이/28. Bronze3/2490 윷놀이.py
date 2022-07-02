for i in range(0, 3):
    x, y, z, w = map(int, input().split(' '))
    youth = x + y + z + w

    if youth == 0:
        print("D")#"윷"
    elif youth == 1:
        print("C")#"걸"
    elif youth == 2:
        print("B")#"개"
    elif youth == 3:
        print("A")#"도"
    elif youth == 4:
        print("E")#"모"
