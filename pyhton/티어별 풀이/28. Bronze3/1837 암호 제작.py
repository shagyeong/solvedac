'''
#암호가 두 소수의 곱임이 보장됨
pwd, key = input().split(' ')

pwd = int(pwd)
key = int(key)

i = 2   

#2 * 소수 형태인 경우 while문 넘어감
#아닌 경우 3부터 시작

while pwd % i != 0:
    i = i + 1
p = i   #반드시 p < q
q = pwd // i

if p >= key:
    print("GOOD")
else:
    print("BAD", p)
#오류는 없으나
#공개 암호가 커지면 효율성이 떨어짐
#"시간 초과"로 틀림
'''
#key보다 작은 소수를 먼저 구함
pwd, key = input().split(' ')

pwd = int(pwd)
key = int(key)

primeunderkey = [2]
#유일한 짝수 소수라는 특수성으로 인해
#미리 추가해둠

for i in range(3, key):
    j = 2
    while i % j != 0:
        j = j + 1
    if j == i:
        primeunderkey.append(i)

result = "GOOD"

for i in primeunderkey:
    if pwd % i == 0:
        result = "BAD"
        break
if result == "GOOD":
    print(result)
else:
    print(result, i)
