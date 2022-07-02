sc1 = int(input())
sc2 = int(input())
sc3 = int(input())
sc4 = int(input())
so1 = int(input())
so2 = int(input())

sc = sc1 + sc2 + sc3 + sc4 - min([sc1, sc2, sc3, sc4])
so = max([so1, so2])

print(sc + so)
