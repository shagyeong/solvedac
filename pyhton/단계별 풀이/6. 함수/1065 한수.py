#반드시 세 자리 이상의 "한수"가 들어온다고 가정함
#문제에서 범위를 1000이하로 줬기 때문에 열 자리 초과는 고려하지 않았음
def nexthansu(hansu:int):
    hansu = list(str(hansu))
    for i in range(0, len(hansu)):
        hansu[i] = int(hansu[i])
    
    digit = len(hansu)      #자릿수
    d = hansu[1] - hansu[0]#공차

    if hansu[0] == 9 and d == 0:#자릿수가 바뀌는 경우 9999, 11111
        nexthansu = "1" * (digit + 1)
        nexthansu = int(nexthansu)
        return nexthansu
    else:
        nexthansu = []
        nexthansu.append(hansu[0])
        d += 1
        result = 0
        for i in range(0, len(hansu) - 1):
            if nexthansu[i] + d >= 10:
                result = 1#백의자리가 바뀌는 경우
                break
            else:
                nexthansu.append(nexthansu[i] + d)

        if result == 1:
            nexthansu = []
            nexthansu.append(hansu[0] + 1)
            d = (hansu[0] + 1) // (digit - 1) * (-1)
            for i in range(0, len(hansu) - 1):
                nexthansu.append(nexthansu[i] + d)
        #다시 정수형으로
        nexthansu2 = ""
        for i in nexthansu:
            nexthansu2 = nexthansu2 + str(i)
        
        nexthansu2 = int(nexthansu2)

        return nexthansu2


tri_hansusunder1000 = [111] #세자리 이상, 천 이하의 한수들
hansu = 111
for i in range(0, 44):
    hansu = nexthansu(hansu)
    tri_hansusunder1000.append(hansu)

#한 자리, 두 자리 수는 반드시 "한수"

n = int(input())

if n <= 99:
    print(n)
elif n <= 110:
    print("99")
else:
    if n in tri_hansusunder1000:
        print(99 + tri_hansusunder1000.index(n) + 1)
    else:
        tri_hansusunder1000.append(n)
        tri_hansusunder1000.sort()
        print(99 + tri_hansusunder1000.index(n))
