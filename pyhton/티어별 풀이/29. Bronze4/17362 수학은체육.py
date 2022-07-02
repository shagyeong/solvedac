n = int(input())
key = n % 8

if key == 1:
    print("1")
elif key == 2 or key == 0:
    print("2")
elif key == 3 or key == 7:
    print("3")
elif key == 4 or key == 6:
    print("4")
else:
    print("5")
