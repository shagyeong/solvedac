#별찍기 12
#n = int(input())
#
#for i in range(-(n - 1), (n -1) + 1):
#    space = abs(i)
#    stars = n - space
#
#    for i in range(0, space):
#        print(" ", end = "")
#    for i in range(0, stars):
#        print("*", end = "")
#    print("\n", end = "")
#

#별찍기 13
n = int(input())

for i in range(-(n - 1), (n -1) + 1):
    space = abs(i)
    stars = n - space

    for i in range(0, stars):
        print("*", end = "")
    
    print("\n", end = "")
