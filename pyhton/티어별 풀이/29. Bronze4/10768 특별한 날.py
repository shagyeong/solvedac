mon = input()
day = input()

if len(day) == 1:
    day = "0" + day

date = mon + day

if int(date) == 218:
    print("Special")
elif int(date) < 218:
    print("Before")
else:
    print("After")
