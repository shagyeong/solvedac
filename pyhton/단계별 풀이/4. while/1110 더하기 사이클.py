def newnumber(n):
    if len(n) == 1:
        n = "0" + n
    
    newnumber = int(n[0]) + int(n[1])
    newnumber %= 10
    
    if n[1] != "0":
        newnumber = n[1] + str(newnumber)
    else:
        newnumber = str(newnumber)

    return newnumber

n = input()
nn = newnumber(n)

t = 1

while nn != n:
    nn = newnumber(nn)
    t += 1

print(t)
