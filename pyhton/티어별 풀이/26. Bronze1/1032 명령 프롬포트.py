case = int(input())

fname1 = list(input())

for i in range(0, case - 1):

    fname_comp = list(input())

    for i in range(0, len(fname1)):
        if fname1[i] != fname_comp[i]:
            fname1[i] = "?"

print(''.join(fname1))
