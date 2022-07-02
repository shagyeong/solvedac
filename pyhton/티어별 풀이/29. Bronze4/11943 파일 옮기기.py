app1, ora1 = input().split()
app2, ora2 = input().split()

app1 = int(app1)
ora1 = int(ora1)
app2 = int(app2)
ora2 = int(ora2)

if app1 + ora2 > app2 + ora1:
    print(app2 + ora1)
else:
    print(app1 + ora2)
