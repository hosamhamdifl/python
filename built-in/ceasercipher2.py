# Caesar cipher.
text = input("Enter your message: ")
shift = int(input("Enter Shift Value: "))
cipher = ''
for char in text:
    if char.isspace():
        code = ord(char)
    if char.isnumeric():
        code = ord(char)
    if char.isalpha():
        if char.isupper():
            code = (ord(char) + shift - 65) % 26 + 65

        elif char.islower():
            code = (ord(char) + shift - 97) % 26 + 97

    cipher += chr(code)

print(cipher)
