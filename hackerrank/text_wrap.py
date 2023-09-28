import textwrap


def wrap(string, max_width):
    l = textwrap.wrap(string, max_width)
    s = ''
    for i in range(0, len(l)):
        s += l[i]+'\n'
    return s


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
