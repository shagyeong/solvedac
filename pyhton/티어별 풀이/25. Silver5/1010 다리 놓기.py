case = int(input())

bri_cases = []

for i in range(0, case):
    n, m = map(int, input().split())
    
    bri_case = 1
    for i in range(0, n):
        bri_case = bri_case * (m - i)
    for i in range(0, n):
        bri_case = bri_case // (n - i)
    bri_cases.append(int(bri_case))

for i in bri_cases:
    print(i)
