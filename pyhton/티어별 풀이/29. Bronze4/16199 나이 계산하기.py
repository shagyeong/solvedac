def date():
    year, m, d = input().split()

    if len(m) == 1:
        m = "0" + m
    if len(d) == 1:
        d = "0" + d

    date = m + d

    return [year, date]

m1 = date()
m2 = date()

age = int(m2[0]) - int(m1[0])

age2 = age + 1
age3 = age

if int(m1[1]) <= int(m2[1]):
    age1 = age
else:
    age1 = age - 1

print(age1, age2, age3, sep = "\n")
