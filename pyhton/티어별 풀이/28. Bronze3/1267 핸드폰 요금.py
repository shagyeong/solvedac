#스토리텔링 적당히하고 문제전달이나 제대로했으면 좋겠음
def ysf(array):
    fee = 0
    for i in array:
        fee = fee + 10 * (i // 30 + 1)
    return fee

def msf(array):
    fee = 0
    for i in array:
        fee = fee + 15 * (i // 60 + 1)
    return fee

case = int(input())
calls = list(map(int, input().split(' ')))

ysf = ysf(calls)
msf = msf(calls)

if ysf < msf:
    print("Y", ysf)
elif msf < ysf:
    print("M", msf)
else:
    print("Y M", ysf)
