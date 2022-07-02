#별찍기3
#n = int(input())
#
#a = int(n)
#b = int(n)
#
#for i in range(0, a):
#    for j in range(0, b):
#        print("*", end = "")
#    print("\n", end = "")
#    b = b - 1

#별찍기4
#n = int(input())
#
#a = int(n)
#b = int(n)
#
#for i in range(0, a):
#    for j in range(0, a - b):
#        print(" ", end = "")
#    for j in range(0, b):
#        print("*", end = "")
#    print("\n", end = "")
#    b = b - 1

#별찍기5
#n = int(input())
#
#space = int(n - 1)
#stars = 1
#
#for i in range(0, n):
#    for i in range(0, space):
#        print(" ", end = "")
#    for i in range(0, stars):
#        print("*", end = "")
#    print("\n", end = "")
#    space -= 1
#    stars += 2

#별찍기6
#n = int(input())
#
#space = 0
#stars = int(2 * n - 1)
#
#for i in range(0, n):
#    for i in range(0, space):
#        print(" ", end = "")
#    for i in range(0, stars):
#        print("*", end = "")
#    print("\n", end = "")
#    space += 1
#    stars -= 2

#별찍기7
#5, 6을 함수로 정의해 재사용
#
#def stampstar_5(n):
#    space = int(n - 1)
#    stars = 1
#
#    for i in range(0, n):
#        print(" ", end = "")
#        for i in range(0, space):
#            print(" ", end = "")
#        for i in range(0, stars):
#            print("*", end = "")
#        print("\n", end = "")
#        space -= 1
#        stars += 2
#
#def stampstar_6(n):
#    space = 0
#    stars = int(2 * n - 1)
#
#    for i in range(0, n):
#        print(" ", end = "")
#        for i in range(0, space):
#            print(" ", end = "")
#        for i in range(0, stars):
#            print("*", end = "")
#        print("\n", end = "")
#        space += 1
#        stars -= 2
#    
#n = int(input())
#
#stampstar_5(n - 1)
#print("*" * (2 * n - 1))
#stampstar_6(n - 1)

#별찍기8
#def stampspace_5(n):
#    space = n * 2
#    stars = 1
#
#    for i in range(0, n):
#        for i in range(0, stars):
#            print("*", end = "")
#        for i in range(0, space):
#            print(" ", end = "")
#        for i in range(0, stars):
#            print("*", end = "")
#        print("\n", end = "")
#        space -= 2
#        stars += 1
#
#def stampspace_6(n):
#    space = 2
#    stars = n
#
#    for i in range(0, n):
#        for i in range(0, stars):
#            print("*", end = "")
#        for i in range(0, space):
#            print(" ", end = "")
#        for i in range(0, stars):
#            print("*", end = "")
#        print("\n", end = "")
#        space += 2
#        stars -= 1
#    
#n = int(input())
#
#stampspace_5(n - 1)
#print("*" * (2 * n))
#stampspace_6(n - 1)

#별찍기9
n = int(input())

for i in range(-(n - 1), (n - 1) +1):
    for j in range(0, -1 * abs(i) + n - 1):
        print(" ", end = "")
    for k in range(0, abs(i) * 2 + 1):
        print("*", end = "")
    print("\n", end = "")

