cs1, ma1, sc1, en1 = input().split()
cs2, ma2, sc2, en2 = input().split()

cs1 = int(cs1)
ma1 = int(ma1)
sc1 = int(sc1)
en1 = int(en1)
cs2 = int(cs2)
ma2 = int(ma2)
sc2 = int(sc2)
en2 = int(en2)



p1 = cs1 + ma1 + sc1 + en1
p2 = cs2 + ma2 + sc2 + en2

if p1 > p2:
    print(p1)
elif p1 < p2:
    print(p2)
else:
    print(p1)
