s = input()
count_upper = 0
count_lower = 0
for c in s:
    if c.isupper():
        count_upper += 1
    if c.islower():
        count_lower += 1
if count_upper > count_lower:
    print(s.upper())
else:
    print(s.lower())