test_cases = int(input())

for _ in range(test_cases):
    try:
        values = input()
        a = int(values.split(" ")[0])
        b = int(values.split(" ")[1])
        print(a//b)
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")