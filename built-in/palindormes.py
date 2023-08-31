x = input("Enter Text: ")
y = "Eleven animals I slam in a net"
x = x.replace(" ", "")
if len(x) > 1 and x.upper() == x[::-1].upper():
    print("palindorme")
else:
    print("not palindrome")
