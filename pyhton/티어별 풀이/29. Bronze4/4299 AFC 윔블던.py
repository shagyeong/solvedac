#축구 좋아하는 사람이
#코딩도 좋아해서 주접을 떨어놓은 문제
#문제 전달이 안됨
#축구 내용 늘어놓을 시간에
#쓸만한 예시 하나라도 더 써라
#예시 부족

a, b = input().split()

a = int(a)
b = int(b)

if (int((a + b) % 2) != 0) or (a < b):
    print("-1")
else:
    print(int((a + b) / 2), int((a - b) / 2))
