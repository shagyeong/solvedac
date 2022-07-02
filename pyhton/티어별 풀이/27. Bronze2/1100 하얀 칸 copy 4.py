chesspiece = 0

for i in range(0, 8, 1):
    row1 = list(input())    

    if i % 2 == 0:  #첫 번째 칸이 하얀색
        for j in range(0, 6 + 1, 2):
            if row1[j] == "F":
                chesspiece += 1

    else:           #첫 번째 칸이 검정색
        for k in range(1, 7 + 1, 2):
            if row1[k] == "F":
                chesspiece += 1
print(chesspiece)
