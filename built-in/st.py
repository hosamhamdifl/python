
x="ABbBNmnoa"
s=""
for i in range(0,len(x)):
    if x[i].lower() in x and x[i].upper() in x:
        s+=x[i]
print(s)        
    
