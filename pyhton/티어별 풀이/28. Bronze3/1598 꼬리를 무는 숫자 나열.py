def qupos(n):
    if n % 4 != 0:
        return [n % 4, n // 4 + 1]
    else:
        return [4, n // 4]

a, b = map(int, input().split(' '))
qupos_a = qupos(a)
qupos_b = qupos(b)

print(abs(qupos_a[0] - qupos_b[0]) + abs(qupos_a[1] - qupos_b[1]))
