lis = []
n = int(input())
while n>0:
    lis.append(input(),input())
    n = n-1

m = max(lis)
lis.remove(m)

print(max(lis))