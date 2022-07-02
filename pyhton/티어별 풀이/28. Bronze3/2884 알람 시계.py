h, m = map(int, input().split(' '))
total_time =  h * 60 + m - 45

if total_time < 0:
    total_time += 1440

print(total_time // 60, total_time % 60)
