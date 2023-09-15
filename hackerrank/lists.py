if __name__ == '__main__':
    N = int(input())
    x = []
    read = []
    for i in range(N):
        read.append(input().split())
    for i in range(len(read)):
        if read[i][0] == 'insert':
            x.insert(int(read[i][1]), int(read[i][2]))
        elif read[i][0] == 'print':
            print(x)
        elif read[i][0] == 'pop':
            x.pop()
        elif read[i][0] == 'remove':
            x.remove(int(read[i][1]))
        elif read[i][0] == 'sort':
            x.sort()
        elif read[i][0] == 'reverse':
            x.reverse()
        elif read[i][0] == 'append':
            x.append(int(read[i][1]))
