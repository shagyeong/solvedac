c_temp = int(input())#current temperatur
a_temp = int(input())#aim temperature
under0 = int(input())#영 아래에서 소요시간
exact0 = int(input())#영에서 해동
overr0 = int(input())#영 위에서 데움

time = 0

if c_temp <= 0:
    time = time + (-1) * c_temp * under0
    time = time + exact0
    time = time + a_temp * overr0
else:
    time = time + (a_temp - c_temp) * overr0

print(time)
