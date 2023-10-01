# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_welcome_mat(n, m):
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


if __name__ == '__main__':
    n, m = map(int, input().split())
    print_welcome_mat(n, m)
