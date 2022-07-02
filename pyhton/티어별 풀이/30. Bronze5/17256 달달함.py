ax, ay, az = input().split()
cx, cy, cz = input().split()

ax = int(ax)
ay = int(ay)
az = int(az)
cx = int(cx)
cy = int(cy)
cz = int(cz)

bx = cx - az
by = cy // ay
bz = cz - ax
print(bx, by, bz)
