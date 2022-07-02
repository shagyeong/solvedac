n, m = map(int, input().split())

floor = []

for i in range(0, n, 1):
    row = list(map(str, input()))
    floor.append(row)

h_tile = 0  #horizontal tile 가로 타일
v_tile = 0  #vertical tile 세로 타일

#가로 타일 탐색
for i in range(0, n, 1):
    
    p_tile = '|'    #previous tile

    for j in range(0, m, 1):

        c_tile = floor[i][j]

        if c_tile == '-' and  p_tile == '|':
                h_tile += 1

        p_tile = c_tile

#세로 타일 탐색
for i in range(0, m, 1):
    
    p_tile = '-'    #previous tile

    for j in range(0, n, 1):

        c_tile = floor[j][i]

        if c_tile == '|' and  p_tile == '-':
                v_tile += 1

        p_tile = c_tile

print(h_tile + v_tile)
