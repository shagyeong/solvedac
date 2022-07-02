n = input()
n = n[:-2]
n += "00"
f = input()

n = int(n)
f = int(f)

if n % f == 0:
    print("00")
else:
    if f * (n // f + 1) - n < 10:
        print("0" + str(f * (n // f + 1) - n))
    else:
        print(f * (n // f + 1) - n)
