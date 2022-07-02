cases = int(input())

prices = []
for i in range(0, cases):
    a = float(input())
    prices.append(a)

for i in range(0, cases):
    a = round(prices[i] * 0.8, 2)
    print("${:.2f}".format(a))
