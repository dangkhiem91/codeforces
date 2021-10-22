n, m , a = map(int, input().split())
if m % a == 0:
    num1 = m // a
else: 
    num1 = m // a + 1
if n % a == 0:
    num2 = n // a
else:
    num2 = n // a + 1
print (num1 * num2)