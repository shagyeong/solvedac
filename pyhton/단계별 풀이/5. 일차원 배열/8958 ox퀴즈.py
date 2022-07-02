def oxox(array):
    score = 0
    streak = 0

    for i in array:
        if i == "O":
            streak += 1
        else:
            streak = 0
        score = score + streak
    return score

t = int(input())
for i in range(0, t):
    print(oxox(input()))
