import math

result = math.e == math.exp(1)
print(ord('c')-ord('a'))
try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")
