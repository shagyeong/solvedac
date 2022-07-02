fixed_cost, float_cost, price = input().split()
fixed_cost = int(fixed_cost)
float_cost = int(float_cost)
price = int(price)

if float_cost >= price :#손익분기점이 없음
    print("-1")
else:                   #손익분기점 있음
    print(fixed_cost // (price - float_cost) + 1)
