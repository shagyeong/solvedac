#지능형 기차 1, 2
extraindata = []
entraindata = []

for i in range(0, 10):
    extrain, entrain = map(int, input().split(' '))
    extraindata.append(extrain)
    entraindata.append(entrain)

pit = 0     #passengerintrain
pis = []    #passengerinsections

for i in range(0, len(extraindata) - 1):
    pit = pit - extraindata[i]
    pit = pit + entraindata[i]
    pis.append(pit)
print(max(pis))