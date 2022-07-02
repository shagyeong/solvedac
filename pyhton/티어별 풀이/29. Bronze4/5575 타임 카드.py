Ah1, Am1, As1, Ah2, Am2, As2 = input().split()
Bh1, Bm1, Bs1, Bh2, Bm2, Bs2 = input().split()
Ch1, Cm1, Cs1, Ch2, Cm2, Cs2 = input().split()

Ah1 = int(Ah1)
Am1 = int(Am1)
As1 = int(As1)
Ah2 = int(Ah2)
Am2 = int(Am2)
As2 = int(As2)
Bh1 = int(Bh1)
Bm1 = int(Bm1)
Bs1 = int(Bs1)
Bh2 = int(Bh2)
Bm2 = int(Bm2)
Bs2 = int(Bs2)
Ch1 = int(Ch1)
Cm1 = int(Cm1)
Cs1 = int(Cs1)
Ch2 = int(Ch2)
Cm2 = int(Cm2)
Cs2 = int(Cs2)

def totalsecond(h, m , s):
    return h * 3600 + m * 60 + s

def printtime(totalsecond):
    hour = totalsecond // 3600
    totalsecond = totalsecond % 3600

    minute = totalsecond // 60
    totalsecond = totalsecond % 60

    second = totalsecond

    print(hour, minute, second)

Aperiod = totalsecond(Ah2, Am2, As2) - totalsecond(Ah1, Am1, As1)
Bperiod = totalsecond(Bh2, Bm2, Bs2) - totalsecond(Bh1, Bm1, Bs1)
Cperiod = totalsecond(Ch2, Cm2, Cs2) - totalsecond(Ch1, Cm1, Cs1)

printtime(Aperiod)
printtime(Bperiod)
printtime(Cperiod)
