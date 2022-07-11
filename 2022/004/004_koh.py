k = int(input())
a = 1
cnt = 0
for i in range(1000000):
    a = a * 2
    if a >= k:
        break
list = list(bin(k)[2:])

for i in range(len(list) - 1, 0, -1):
    if list[i] == '1':
        cnt = i + 1
        break

print(a, cnt)
