def print_formatted(number):
    # your code goes here
    num = []
    num_o = []
    num_h = []
    num_b = []
    for i in range(1, number+1):
        num.append(i)
        num_o.append(oct(i)[2:])
        num_b.append(bin(i)[2:])
        num_h.append(hex(i)[2:])

    for i in range(len(num)):
        print(
            str(num[i]).rjust(len(num_b[-1])),
            str(num_o[i]).rjust(len(num_b[-1])),
            str(num_h[i]).rjust(len(num_b[-1])).upper(),
            str(num_b[i]).rjust(len(num_b[-1]))
        )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
