def averageper(array, c):
    average = sum(array) / c
    
    overaverage = 0

    for i in array:
        if i > average:
            overaverage += 1
    
    return overaverage / c * 100

t = int(input())

for i in range(0, t):
    array = list(map(int, input().split()))
    c = array[0]
    array = array[1:]
    print("{:.3f}%".format(averageper(array, c)))
