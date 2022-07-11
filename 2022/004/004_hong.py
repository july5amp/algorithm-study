k = int(input())
min_chocolate = 1

while k>min_chocolate:
    min_chocolate*=2

a=min_chocolate
b=0
cnt=0
while k>0:
    if k>=a:
        k-=a
    else:
        a=int(a/2)
        cnt+=1
print(min_chocolate,cnt)
