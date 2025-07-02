num1, num2, num3 = map(int, input().split())

if (num1 == num2 == num3):
    price = 10000 + num1 * 1000
elif(num1 == num2) or  (num3 == num1):
    price = 1000 + num1 * 100
elif(num2 == num3):
    price = 1000 + num2 * 100
else:
    M = max(num1, num2, num3)
    price = M * 100

print(price)