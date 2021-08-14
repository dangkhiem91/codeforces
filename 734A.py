n = int(input())
g = input()
win_A = 0
win_D = 0
for i in range(n):
    if g[i] == "A":
        win_A += 1
    else:
        win_D += 1
if win_A > win_D:
    print("Anton")
elif win_A < win_D:
    print("Danik")
else:
    print("Friendship")