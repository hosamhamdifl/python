def mysplit(strng):
  
    r=[]
    s=""
    for char in strng:
            if char !=" ":
               s+=char
            elif s:
                r.append(s)
                s=""
    r.append(s)
    for item in r:
        if item=="":
            r.remove(item)
    return r


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))