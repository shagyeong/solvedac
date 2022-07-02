summer, harvest, slot, price = input().split()

summer = int(summer)
harvest = int(harvest)
slot = int(slot)
price = int(price)

if (summer % harvest) == 0:
    times = summer // harvest -1
else:
    times = summer // harvest

print(times * slot * price)
