n = int(input())

paper = []

for n in range(0, n):
    row = list(map(int, input().split()))
    paper.append(row)
print(paper)