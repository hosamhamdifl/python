# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    i = int(input())
    if i <= 1:
        print('Not prime')

    elif i <= 3:
        print('Prime')

    elif i % 2 == 0 or i % 3 == 0:
        print('Not prime')
    else:
        n = 5
        while n*n <= i:
            if i % n == 0 or i % (n+2) == 0:
                print('Not prime')
                break
            n += 6
        else:
            print('Prime')
