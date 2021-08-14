n, h= map(int, input().split())
s = list(map(int,input().split()))
r = 0
for i in range(n):
    if s[i] <= int(h):
        r += 1
    else:
        r += 2
print(r)