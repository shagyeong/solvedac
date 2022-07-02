from operator import index


n_octal = "!"
n_octals = []
n_denarys = []

while n_octal != ["#"]:
    n_octal = list(input())
    for i in range(0, len(n_octal)):
        if n_octal[i] == "-":
            n_octal[i] = "0"
        elif n_octal[i] == "\\":
            n_octal[i] = "1"
        elif n_octal[i] == "(":
            n_octal[i] = "2"
        elif n_octal[i] == "@":
            n_octal[i] = "3"
        elif n_octal[i] == "?":
            n_octal[i] = "4"
        elif n_octal[i] == ">":
            n_octal[i] = "5"
        elif n_octal[i] == "&":
            n_octal[i] = "6"
        elif n_octal[i] == "%":
            n_octal[i] = "7"
        elif n_octal[i] == "/":
            n_octal[i] = "-1"
        else:
            i = "#"
    n_octals.append(n_octal)
        
n_octals.remove(["#"])

def octtoden(array):
    index8 = 0
    n_octal = 0
    for i in range((len(array) - 1), -1, -1):
        n_octal = n_octal + 8 ** index8 * int(array[i])
        index8 +=1
    return n_octal

for i in n_octals:
    print(octtoden(i))

