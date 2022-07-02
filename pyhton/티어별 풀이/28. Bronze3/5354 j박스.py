#조건부족

def jbox(n):
    if n == 1:
        print("#", end = "")
    elif n == 2:
        print("##")
        print("##", end = "")
    else:
        for i in range(0, n):
            print("#", end = "")

        print("")

        for i in range(0, n - 2):
            print("#", end = "")
            for i in range(0, n - 2):
                print("j", end = "")
            print("#", end = "\n")

        for i in range(0, n):
            print("#", end = "")
    print("\n")

case = int(input())
cases = []
for i in range(0, case):
    cases.append(int(input()))

for i in cases:
    jbox(i)
