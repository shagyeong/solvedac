n, m = input().split()

n = int(n)
m = int(m)

if m >= 1 and m <= 2:
    print("NEWBIE!")
elif m >= 3 and m <= n:
    print("OLDBIE!")
else:
    print("TLE!")
