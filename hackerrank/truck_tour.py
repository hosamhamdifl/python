 # Initialize variables
    start = 0
    deficit = 0
    surplus = 0

    # Iterate over each petrol pump
    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        surplus += petrol - distance

        # If surplus is negative, move the starting point to the next pump
        # and add the deficit to the surplus
        if surplus < 0:
            start = i + 1
            deficit += surplus
            surplus = 0

    # If the total surplus (including deficit) is non-negative,
    # the truck can complete the tour, so return the starting point.
    # Otherwise, return -1.
    return start if surplus + deficit >= 0 else -1