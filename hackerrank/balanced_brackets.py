stack = []
bracket_map = {"(": ")", "[": "]",  "{": "}"}

for bracket in s:
    if bracket in bracket_map:
        stack.append(bracket)
    elif stack and bracket == bracket_map[stack[-1]]:
                stack.pop()
    else:
        return "NO"
return "YES" if not stack else "NO"