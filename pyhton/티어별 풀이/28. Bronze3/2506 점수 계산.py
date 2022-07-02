n = int(input())
cur_answers = list(map(int, input().split()))

streak_score = 0
score = 0

for i in range(0, n):
    cur_ans = cur_answers[i]
    
    if cur_ans == 0:
        streak_score = 0
    else:
        streak_score += 1

    score = score + streak_score

print(score)
