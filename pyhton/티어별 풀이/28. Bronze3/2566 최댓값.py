list_9x9 = []

for i in range(0, 9):
    list_1x9 = list(map(int, input().split()))
    list_9x9.append(list_1x9)

list_1x9_max = []   #1x9배열에서 최댓값들
for i in range(0, 9):
    list_1x9_max.append(max(list_9x9[i]))

maxi = max(list_1x9_max)
row = list_1x9_max.index(maxi)
col = list_9x9[row].index(maxi)

print(maxi)
print(row + 1, col + 1, sep = " ")
