bes = list(map(int, input().split()))
dai = list(map(int, input().split()))
jon = list(map(int, input().split()))

bes_n = abs(jon[0] - bes[0])
bes_m = abs(jon[1] - bes[1])
dai_n = abs(jon[0] - dai[0])
dai_m = abs(jon[1] - dai[1])

bes_time = max([bes_n, bes_m])
dai_time = dai_n + dai_m

if bes_time > dai_time:
    print("daisy")
elif bes_time < dai_time:
    print("bessie")
else:
    print("tie")
