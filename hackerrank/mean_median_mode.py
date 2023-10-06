# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
m=list(map(int,input().split()))
mean=round(sum(m)/n,1)
print(mean)

median_index=[]
if n%2==0:
    median_index.append(n//2)
    median_index.append((n//2)+1)
else:
    median_index.append(n//2)
x=sorted(m)
if len(median_index)>1:
    print((x[median_index[0]-1]+x[median_index[1]-1])/2)
else:
    print(x[median_index[0]])
    
dict={}
for i in m:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
mode = min(k for k,v in dict.items() if v ==max (dict.values()))
print(mode)

    