import string


def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    l = []
    for i in range(size):
        s = '-'.join(alpha[i:size])
        l.append((s[::-1]+s[1:]).center(4*size-3, "-"))

    s = '\n'.join(l[:0:-1]+l)
    print(s)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
