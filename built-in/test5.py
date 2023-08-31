x = "--..,..--,.-.-,.--.,..--"
y=""
odash=0
odot=0

# if x[0]=="-":
#     y+="."

for i in x:
    if i =="-":
       y+="."
    elif i==".":
       y+="-"
        
    else:
        y+=","

# y=x.replace("--","..")
    
print(y)