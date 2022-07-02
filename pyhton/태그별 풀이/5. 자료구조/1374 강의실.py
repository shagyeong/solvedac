#메모리초과
n = int(input())

timetable = []
lens = []

for i in range(0, n):
    object = []
    o, s, e = map(int, input().split())
    for i in range(0, s, 1):
        object.append(0)
    for i in range(s, e, 1):
        object.append(1)

    timetable.append(object)
    lens.append(len(object))

lenmax = max(lens)
for i in timetable:
    for j in range(0, lenmax - len(i)):
        i.append(0)

counts = []
for i in range(0, lenmax):
    count = 0
    for j in range(0, len(timetable)):
        if timetable[j][i] == 1:
            count = count + 1
    counts.append(count)

print(max(counts))
