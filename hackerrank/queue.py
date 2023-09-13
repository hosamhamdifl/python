first=[]
second=[]
for i in range(int(input())):
    l=list(map(int,input().split()))
    if l[0]==1:
        first.append(l[1])
    elif l[0]==2:
        second=first[::-1]
        second.pop()
        first=second[::-1]
        second=[]
    else:
        print(first[0])