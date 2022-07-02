a, b = input().split()
if len(a) > len (b):
    a = "0" + a
    for i in range(len(a) - len(b)):
        b = "0" + b
elif len(a) < len (b):
    b = "0" + b
    for i in range(len(b) - len(a)):
        a = "0" + a
else:
    a = "0" + a
    b = "0" + b

c = ''

upper_1 = 0     #자리 올림 수-처음엔 0

for i in range(0, len(a)):
    index_current = len(a) - 1 - i

    current_a = a[index_current]
    current_b = b[index_current]

    #자리올림 1, 처리 자리 값을 더함
    current_sum = (int(current_a) +
                  int(current_b) +
                  upper_1)

    if current_sum >= 10:
        upper_1 = 1
        c = str(current_sum)[1] + c
    else:
        upper_1 = 0
        c = str(current_sum) + c

if c[0] == "0":
    c = c[1:]

print(c)
