i=True
while i:
    user_input=input("enter text,type exit to stop : ")
    user_input=user_input.replace(" ","").lower()
    if len(user_input) > 1 and user_input.upper() == user_input[::-1].upper() and user_input!="exit":
        print("palindorme")
    elif user_input=="exit":
        i=False
    else:
        print("not palindrome")
        