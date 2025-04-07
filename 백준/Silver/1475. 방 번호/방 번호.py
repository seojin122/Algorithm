number = input()
num = list(map(int, number))
count = [0] * 10 #0~9

for i in num:
    count[i] += 1

same = count[6] + count[9]
count[6] = count[9] = (same + 1) // 2

print(max(count))