x = int(input())

y1 = int(input())   #기본요금
y2 = int(input())   #기본요금 청구 상한 사용량
y3 = int(input())   #기본요금 초과 할증

p = int(input())

fee_x = p * x

if p <= y2:
    fee_y = y1
else:
    fee_y = y1 + (p - y2) * y3

if fee_x > fee_y:
    print(fee_y)
else:
    print(fee_x)
