def candyteacher(candys : list):
    if sum(candys) % len(candys) == 0:
        return "YES"
    else:
        return "NO"


k = int(input())
for i in range(0, k):

    a = input()#공백입력으로 줄넘김
    case = int(input())
    candys = []

    for i in range(0, case):
        candy = int(input())
        candys.append(candy)
    
    print(candyteacher(candys))
