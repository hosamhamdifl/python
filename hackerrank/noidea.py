# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
x = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
r=0
for i in x:
    if i in a:
        r+=1
    elif i in b:
        r-=1
print(r)
