binary_a = input()

denary_a = 0

for i in range(0, len(binary_a)):
    if binary_a[i] == "1":
        index_2 = len(binary_a) - 1 - i
        denary_a = denary_a + 2 ** index_2

denary_a *= 17

binary_a = ""

while denary_a != 1:
    binary_a = str(denary_a % 2) + binary_a
    denary_a = denary_a // 2
    
binary_a = "1" + binary_a
print(binary_a)
