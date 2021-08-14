n = int(input())
count = 0
s = input()
for i in range (1,n):   
    if s[i] == s[i-1]:
        count += 1
print(count)