def read_int(prompt, min, max):
    ok = False
    while not ok:  # ---> True
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: Wrong Input")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: The value is not within range(" +
                  str(min) + ".." + str(max) + ")")
    return value


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
