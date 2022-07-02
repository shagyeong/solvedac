date = input()
c0, c1, c2, c3, c4 = input().split()

cars = [c0, c1, c2, c3, c4]

number = 0

for i in cars:
    if i == date:
        number +=1

print(number)
