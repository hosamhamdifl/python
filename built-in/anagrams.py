x = input("Enter first Text: ")
y = input("Enter second Text: ")
x = x.replace(" ", "")
y = y.replace(" ", "")
x1 = sorted(x.upper())
y1 = sorted(y.upper())
if len(x) > 1 and len(y) > 1 and len(x) == len(y) and x1 == y1:
    print("anagram")
else:
    print("not anagram")
