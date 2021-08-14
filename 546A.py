k, n, w = map(int, input().split())
tongtien = 0
 
for i in range(1, w+1):
    tongtien = tongtien + i * k
 
tienmuon = tongtien - n
if tienmuon < 0:
    tienmuon = 0
 
print(tienmuon)