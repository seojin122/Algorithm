N = int(input(""))
A = list(map(int,input("").split(" ")))  # 1 1 1 6 0 
B = list(map(int, input("").split(" "))) # 2 7 8 3 1

A = sorted(A, reverse= True) # 6 1 1 1 0

sum = 0

for j in range(len(A)):
    min_B = min(B)
    B.remove(min_B)
    sum = (min_B * A[j]) + sum
print(sum)