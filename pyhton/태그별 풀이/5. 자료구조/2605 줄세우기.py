n = int(input())
papers = list(map(int, input().split()))

students = []
for i in range(1, n + 1):
    students.append(i)

for i in range(0, n):
    paper = papers[i]
    student = students[i]
    studentindex = i - paper

    students.remove(student)
    students.insert(studentindex, student)

for i in range(0, len(students) - 1):
    print(students[i], end = ' ')
print(students[len(students) - 1])
