a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

scores = [a, b, c, d, e]
for i in range(0, len(scores)):
    if scores[i] < 40:
        scores[i] = 40

print(sum(scores) // 5)
