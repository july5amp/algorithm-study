k = int(input())
n = 1
count = -1

while k > n:
    n *= 2

print(n, end=' ')

while k != 0:
    if k >= n:
        k -= n
    n //= 2
    count += 1

print(count)