cups = [1, 2, 3]
def swap(a, b, array):
    a = a - 1
    b = b - 1
    c = array[b]
    array[b] = array[a]
    array[a] = c
    return array

case = int(input())

for i in range(0, case):
    a, b = map(int, input().split(' '))
    cups = swap(a, b, cups)
print(cups.index(1) + 1)
