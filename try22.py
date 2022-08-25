for i in range(0,3):
    name = input()
    score = float(input())
    lis = []
    lis2 = []
    lis.append(name)
    lis.append(score)
    lis2.append(lis)
    s = []
print(lis2)
for i in lis2:
    for i in lis:
        s.append(lis[1])

#
print(s)
'''for i in lis2:
    for i in lis:
        if lis[1] == mini:
            print(lis)'''