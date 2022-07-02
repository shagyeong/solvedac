def sod(n:int):
    sum1 = 0
    
    center = n ** 0.5
    if center - int(center) == 0.0:
        sum1 -= int(center)
    
    center = int(center)


    for i in range(2, center + 1):
        if n % i == 0:
            sum1 += i
            sum1 += (n // i)
            sum1 %= 1000000

    return sum1


n = int(input())


csod = 0

for i in range(1, n + 1):
    csod = csod + sod(i)
    csod %= 1000000

print(csod + 1)#첫 조건에 의해 sod(1)이 -1이므로 1을 더해줌
