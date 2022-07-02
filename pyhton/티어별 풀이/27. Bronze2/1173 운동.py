minute, bpm_min, bpm_max, bpm_sum, bpm_sub = map(int, input().split())

#최소운동시간 : 
min_exercise = (bpm_max - bpm_min) // bpm_sum
