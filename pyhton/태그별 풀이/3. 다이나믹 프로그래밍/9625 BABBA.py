ab = [1, 0]
def button(ab:list):
    na = ab[0]  #number of a
    nb = ab[1]  #number of b
    
    ab[0] = na + na * (-1) + nb * 1
    ab[1] = nb + na * 1 + nb * 0

    return ab

n = int(input())

for i in range(0, n):
    ab = button(ab)

print(ab[0], ab[1], sep = ' ')
