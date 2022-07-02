n_octal = list(input())

n_binary = ''

for i in n_octal:
    if i == "0":
        n_binary = n_binary + "000"
    elif i == "1":
        n_binary = n_binary + "001"
    elif i == "2":
        n_binary = n_binary + "010"
    elif i == "3":
        n_binary = n_binary + "011"
    elif i == "4":
        n_binary = n_binary + "100"
    elif i == "5":
        n_binary = n_binary + "101"
    elif i == "6":
        n_binary = n_binary + "110"
    else:
        n_binary = n_binary + "111"
if n_octal[0] == "0":
    n_binary ="0"
elif n_octal[0] == "1":
    n_binary = n_binary[2:]
elif n_octal[0] == "2" or n_octal[0] == "3":
    n_binary = n_binary[1:]

print(n_binary)
