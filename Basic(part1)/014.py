date1 = (input("The first day. ex:(yyyy,mm,dd): "))
date2 = (input("The second day. ex:(yyyy,mm,dd): "))

lista1 = date1.split(",")
lista2 = date2.split(",")

y1 = int(lista1[0])
y2 = int(lista2[0])
yss = 0
if (y1 >= y2):
    ys = y1 - y2
    yss = ys
else:
    ys = y2 - y1
    yss = ys

m1 = int(lista1[1])
m2 = int(lista2[1])
mss = 0
if (m1 >= m2):
    ms = m1 - m2
    mss = ms
else:
    ms = m2 - m1
    mss = ms

d1 = int(lista1[2])
d2 = int(lista2[2])
dss = 0
if (d1 >= d2):
    ds = d1 - d2
    dss = ds
else:
    ds = d2 - d1
    dss = ds

print(f"That's {yss} years, {mss} months and {dss} days apart")