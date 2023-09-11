def minimumBribes(q):
    count = 0
    x = sorted(q)
    for i in range(len(q)):
        if q[i] - i - 1 > 2:
            print("Too chaotic")
            return
        for j in x:
            if j != q[i]:
                count += 1
            else:
                break
        x.remove(q[i])
    
    print(count)