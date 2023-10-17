def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            kevin_score += score
        else:
            stuart_score += score

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)