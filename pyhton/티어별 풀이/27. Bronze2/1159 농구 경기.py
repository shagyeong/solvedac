n = int(input())

init_letters = []

for i in range(0, n):
    name = list(input())
    init_letters.append(name[0])

letters_over5 = []

while len(init_letters) != 0:
    c_letter = init_letters[0]  #current letter
    count = 0

    while c_letter in init_letters:
        init_letters.remove(c_letter)
        count += 1
    if count >= 5:
        letters_over5.append(c_letter)


if len(letters_over5) == 0:
    print("PREDAJA")
else:
    letters_over5.sort()
    for i in letters_over5:
        print(i, end = "")
    print("\n", end = "")
