def relate(society:list):

    count = 0   #하루에 생성되는 관계의 수
    new_relations = []

    for i in range(0, len(society) - 1):
        c_relation = society[i]
        for j in range(i + 1, len(society)):
            n_relation = society[j]

            if   c_relation[1] == n_relation[0]:
                new_relation = [c_relation[0], n_relation[1]]
                if (new_relation not in society and
                    new_relation not in new_relations):
                    count = count + 1
                    new_relations.append(new_relation)

            elif c_relation[0] == n_relation[1]:
                new_relation = [n_relation[0], c_relation[1]]
                if (new_relation not in society and
                    new_relation not in new_relations):
                    count = count + 1
                    new_relations.append(new_relation)

            elif c_relation[0] == n_relation[0]:
                new_relation = [n_relation[1], c_relation[1]]
                new_relation.sort()
                if (new_relation not in society and
                    new_relation not in new_relations):
                    count = count + 1
                    new_relations.append(new_relation)

            elif c_relation[1] == n_relation[1]:
                new_relation = [n_relation[0], c_relation[0]]
                new_relation.sort()
                if (new_relation not in society and
                    new_relation not in new_relations):
                    count = count + 1
                    new_relations.append(new_relation)


    
    for i in new_relations:
        society.append(i)

    return [society, count]


n, m = map(int, input().split())

society = []

for i in range(0, m):
    relation = list(map(int, input().split()))
    society.append(relation)

counts = []
k = 0#관계가 완성되는데 걸리는 기간

while len(society) != n * (n - 1) // 2:
    result = relate(society)
    society = result[0]
    counts.append(result[1])
    k = k + 1

print(k)
for i in counts:
    print(i)
