#소의 개체 수를 주는 이유
#공간 개수가 소 보다 많으면
#소 개체 수 출력
#문제 전달력 개쓰레기

n, w, h, l = input().split()

n = int(n)
w = int(w)
h = int(h)
l = int(l)

haus = (w // l) * (h // l)

if haus >= n:
    print(n)
else:
    print(haus)
