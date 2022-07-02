ab = input()

if len(ab) == 4:
    print("20")
elif len(ab) == 2:
    print(int(ab[0]) + int(ab[1]))
else:
    if ab[1] == "0":
        print(10 + int(ab[2]))
    else:
        print(10 + int(ab[0]))
