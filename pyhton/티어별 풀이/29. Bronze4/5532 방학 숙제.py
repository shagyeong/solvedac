l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

def min_period(load, able):
    if load % able == 0:
        return load // able
    else:
        return load // able + 1

hw_period = max([min_period(a, c), min_period(b, d)])

print(l - hw_period)
